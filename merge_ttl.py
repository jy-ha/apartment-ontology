#!/usr/bin/env python3
"""
TTL 파일들을 하나로 합쳐서 통합된 TTL 파일을 생성하는 스크립트

사용법:
    python merge_ttl.py                    # 모든 TTL 파일 합치기
    python merge_ttl.py --only-schema      # individuals.ttl과 test_data.ttl 제외하고 합치기

결과:
    - merged_ontology.ttl 파일이 생성됩니다.
    - --only-schema 옵션을 사용하면 merged_ontology_schema.ttl 파일이 생성됩니다.
"""

import os
import glob
import argparse
from collections import OrderedDict

def merge_ttl_files(only_schema=False):
    """TTL 파일들을 하나로 합치는 함수

    Args:
        only_schema (bool): True이면 individuals.ttl과 test_data.ttl을 제외
    """

    # TTL 폴더 경로
    ttl_dir = "/home/blonix/hw/ontology/ttl"

    # 모든 .ttl 파일 찾기
    ttl_files = glob.glob(os.path.join(ttl_dir, "*.ttl"))

    # --only-schema 옵션이면 individuals.ttl과 test_data.ttl 제외
    if only_schema:
        exclude_files = ["individuals.ttl", "test_data.ttl"]
        ttl_files = [f for f in ttl_files if os.path.basename(f) not in exclude_files]
        output_file = "/home/blonix/hw/ontology/merged_ontology_schema.ttl"
    else:
        output_file = "/home/blonix/hw/ontology/merged_ontology.ttl"

    # core.ttl을 가장 먼저 처리하기 위해 정렬
    ttl_files.sort()
    if "core.ttl" in [os.path.basename(f) for f in ttl_files]:
        core_file = next(f for f in ttl_files if os.path.basename(f) == "core.ttl")
        ttl_files.remove(core_file)
        ttl_files.insert(0, core_file)

    # @prefix와 @base 선언을 저장할 OrderedDict
    prefixes = OrderedDict()
    base_declaration = None

    # 각 파일의 내용을 저장할 리스트
    file_contents = []

    for ttl_file in ttl_files:
        print(f"처리 중: {os.path.basename(ttl_file)}")

        with open(ttl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 각 파일의 실제 내용을 저장 (헤더 제외)
        content_lines = []
        in_header = True

        for line in lines:
            stripped = line.strip()

            # 빈 줄은 건너뜀 (헤더 구분용)
            if not stripped:
                if in_header:
                    continue
                else:
                    content_lines.append(line)
                continue

            # @prefix 선언 처리
            if stripped.startswith('@prefix'):
                prefix_line = stripped
                # 세미콜론 제거
                if prefix_line.endswith(';'):
                    prefix_line = prefix_line[:-1]
                prefixes[prefix_line] = True
                continue

            # @base 선언 처리
            elif stripped.startswith('@base'):
                if base_declaration is None:
                    base_declaration = stripped
                    if not stripped.endswith('.'):
                        base_declaration += ' .'
                continue

            # 주석이나 실제 내용 시작
            elif stripped.startswith('#') or not stripped.startswith('@'):
                in_header = False
                content_lines.append(line)

        # 파일 내용이 있으면 저장
        if content_lines:
            file_contents.append({
                'filename': os.path.basename(ttl_file),
                'content': content_lines
            })

    # 통합된 파일 생성 (함수 파라미터로 이동)

    with open(output_file, 'w', encoding='utf-8') as f:
        # 1. @prefix 선언들 작성
        for prefix in prefixes.keys():
            f.write(f"{prefix}\n")

        # 2. @base 선언 작성
        if base_declaration:
            f.write(f"\n{base_declaration}\n")

        # 빈 줄 추가
        f.write("\n")

        # 3. 각 파일의 내용 작성
        for file_data in file_contents:
            filename = file_data['filename']
            content = file_data['content']

            # 파일 구분을 위한 헤더 주석 추가
            f.write(f"###############################################################################\n")
            f.write(f"#\n")
            f.write(f"#    Content from: {filename}\n")
            f.write(f"#\n")
            f.write("###############################################################################\n")
            f.write("\n")

            # 파일 내용 작성
            for line in content:
                f.write(line)

    print(f"\n통합 완료! 결과 파일: {output_file}")
    print(f"처리된 파일 수: {len(file_contents)}")
    print(f"수집된 @prefix 선언 수: {len(prefixes)}")

def main():
    parser = argparse.ArgumentParser(description='TTL 파일들을 하나로 합쳐서 통합된 TTL 파일을 생성합니다.')
    parser.add_argument('--only-schema', action='store_true',
                       help='individuals.ttl과 test_data.ttl을 제외하고 스키마만 합칩니다.')

    args = parser.parse_args()
    merge_ttl_files(only_schema=args.only_schema)

if __name__ == "__main__":
    main()
