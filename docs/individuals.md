# 아파트 청약 자격 온톨로지 개체 정의 (Individuals)

본 문서는 아파트 청약 자격 온톨로지에서 사용되는 구체적인 개체(Individual)들을 정의합니다. 이 개체들은 온톨로지의 지식 베이스를 구성하며, 실제 청약 자격 판단에 필요한 기준 데이터를 제공합니다.

**중요 변경사항 (2024-11):**
- **지역 및 기관의 클래스 → Individual 변경**: Seoul, Gyeonggi, Incheon 및 추천 기관들이 Primitive Class에서 Individual로 재정의되었습니다. 이는 온톨로지 설계 원칙에 따라, 유일하고 구체적인 실체는 Individual로 표현해야 한다는 기준을 적용한 결과입니다.

---

## 1. 지역 개체 (Region Individuals)

**설계 변경**: 이전에 Seoul, Gyeonggi, Incheon은 Primitive Class로 정의되어 있었으나, 각 지역은 유일하고 더 이상 세분화될 수 없는 구체적 개체이므로 Individual로 변경되었습니다.

### 1.1 서울특별시

```turtle
Individual: Seoul
    Types: Region, MetropolitanArea
    Facts:
        regionName "서울"^^xsd:string,
        isSpeculativeOverheatedZone true,
        isSubscriptionOverheatedArea true
    Annotations:
        rdfs:label "서울특별시"@ko,
        rdfs:comment "대한민국의 수도이자 최대 도시. 대부분 지역이 투기과열지구 및 청약과열지역으로 지정됨."@ko
```

### 1.2 경기도

```turtle
Individual: Gyeonggi
    Types: Region, MetropolitanArea
    Facts:
        regionName "경기"^^xsd:string,
        isSpeculativeOverheatedZone false,
        isSubscriptionOverheatedArea false
    Annotations:
        rdfs:label "경기도"@ko,
        rdfs:comment "서울을 둘러싼 수도권 지역. 일부 시(과천, 광명 등)는 투기과열지구로 지정될 수 있음."@ko
```

**참고**: 과천, 광명 등 일부 경기도 지역은 별도의 개체로 정의 가능하며, `isSpeculativeOverheatedZone true`로 설정할 수 있습니다.

### 1.3 인천광역시

```turtle
Individual: Incheon
    Types: Region, MetropolitanArea
    Facts:
        regionName "인천"^^xsd:string,
        isSpeculativeOverheatedZone false,
        isSubscriptionOverheatedArea false
    Annotations:
        rdfs:label "인천광역시"@ko,
        rdfs:comment "서해안에 위치한 수도권 항구 도시."@ko
```

---

## 2. 도시근로자 가구당 월평균 소득 개체 (2024년 기준)

2024년도 통계청 고시 기준 도시근로자 가구당 월평균 소득입니다.

### 2.1 1인 가구

```turtle
Individual: UrbanWorker_2024_1person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 1,
        standardAmount 3000000
    Annotations:
        rdfs:label "2024년 1인 가구 도시근로자 월평균 소득"@ko,
        rdfs:comment "생애최초 특공에서 1인 가구는 2인 가구 기준을 적용받음."@ko
```

### 2.2 2인 가구

```turtle
Individual: UrbanWorker_2024_2person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 2,
        standardAmount 5000000
    Annotations:
        rdfs:label "2024년 2인 가구 도시근로자 월평균 소득"@ko
```

### 2.3 3인 가구

```turtle
Individual: UrbanWorker_2024_3person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 3,
        standardAmount 5400000
    Annotations:
        rdfs:label "2024년 3인 가구 도시근로자 월평균 소득"@ko
```

### 2.4 4인 가구

```turtle
Individual: UrbanWorker_2024_4person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 4,
        standardAmount 6200000
    Annotations:
        rdfs:label "2024년 4인 가구 도시근로자 월평균 소득"@ko
```

### 2.5 5인 가구

```turtle
Individual: UrbanWorker_2024_5person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 5,
        standardAmount 6700000
    Annotations:
        rdfs:label "2024년 5인 가구 도시근로자 월평균 소득"@ko
```

### 2.6 6인 가구

```turtle
Individual: UrbanWorker_2024_6person
    Types: UrbanWorkerStandardIncome
    Facts:
        yearOfStandard 2024,
        householdSize 6,
        standardAmount 7200000
    Annotations:
        rdfs:label "2024년 6인 가구 도시근로자 월평균 소득"@ko,
        rdfs:comment "7인 이상 가구는 6인 가구 기준에 1인당 50만원을 추가하여 산정함."@ko
```

---

## 3. 예치금 요건 개체 (Deposit Requirement Individuals)

### 3.1 서울 지역 예치금 요건

#### 3.1.1 서울 - 85㎡ 이하

```turtle
Individual: Seoul_Deposit_Under85
    Types: DepositRequirement
    Facts:
        appliesInRegion Seoul,
        minArea 0.0,
        maxArea 85.0,
        requiredDepositAmount 3000000
    Annotations:
        rdfs:label "서울 85㎡ 이하 예치금 요건"@ko,
        rdfs:comment "서울 지역 전용면적 85㎡ 이하 주택 청약 시 필요한 최소 예치금: 300만원"@ko
```

#### 3.1.2 서울 - 85㎡ 초과 102㎡ 이하

```turtle
Individual: Seoul_Deposit_85to102
    Types: DepositRequirement
    Facts:
        appliesInRegion Seoul,
        minArea 85.0,
        maxArea 102.0,
        requiredDepositAmount 6000000
    Annotations:
        rdfs:label "서울 85~102㎡ 예치금 요건"@ko,
        rdfs:comment "서울 지역 전용면적 85㎡ 초과 102㎡ 이하 주택 청약 시 필요한 최소 예치금: 600만원"@ko
```

#### 3.1.3 서울 - 102㎡ 초과 135㎡ 이하

```turtle
Individual: Seoul_Deposit_102to135
    Types: DepositRequirement
    Facts:
        appliesInRegion Seoul,
        minArea 102.0,
        maxArea 135.0,
        requiredDepositAmount 10000000
    Annotations:
        rdfs:label "서울 102~135㎡ 예치금 요건"@ko,
        rdfs:comment "서울 지역 전용면적 102㎡ 초과 135㎡ 이하 주택 청약 시 필요한 최소 예치금: 1,000만원"@ko
```

#### 3.1.4 서울 - 135㎡ 초과 모든 면적

```turtle
Individual: Seoul_Deposit_Over135
    Types: DepositRequirement
    Facts:
        appliesInRegion Seoul,
        minArea 135.0,
        maxArea 999999.0,
        requiredDepositAmount 15000000
    Annotations:
        rdfs:label "서울 135㎡ 초과 예치금 요건"@ko,
        rdfs:comment "서울 지역 전용면적 135㎡ 초과 모든 주택 청약 시 필요한 최소 예치금: 1,500만원"@ko
```

### 3.2 경기도 지역 예치금 요건

#### 3.2.1 경기 - 85㎡ 이하

```turtle
Individual: Gyeonggi_Deposit_Under85
    Types: DepositRequirement
    Facts:
        appliesInRegion Gyeonggi,
        minArea 0.0,
        maxArea 85.0,
        requiredDepositAmount 2000000
    Annotations:
        rdfs:label "경기 85㎡ 이하 예치금 요건"@ko,
        rdfs:comment "경기도 지역 전용면적 85㎡ 이하 주택 청약 시 필요한 최소 예치금: 200만원"@ko
```

#### 3.2.2 경기 - 85㎡ 초과 102㎡ 이하

```turtle
Individual: Gyeonggi_Deposit_85to102
    Types: DepositRequirement
    Facts:
        appliesInRegion Gyeonggi,
        minArea 85.0,
        maxArea 102.0,
        requiredDepositAmount 3000000
    Annotations:
        rdfs:label "경기 85~102㎡ 예치금 요건"@ko,
        rdfs:comment "경기도 지역 전용면적 85㎡ 초과 102㎡ 이하 주택 청약 시 필요한 최소 예치금: 300만원"@ko
```

#### 3.2.3 경기 - 102㎡ 초과 135㎡ 이하

```turtle
Individual: Gyeonggi_Deposit_102to135
    Types: DepositRequirement
    Facts:
        appliesInRegion Gyeonggi,
        minArea 102.0,
        maxArea 135.0,
        requiredDepositAmount 5000000
    Annotations:
        rdfs:label "경기 102~135㎡ 예치금 요건"@ko,
        rdfs:comment "경기도 지역 전용면적 102㎡ 초과 135㎡ 이하 주택 청약 시 필요한 최소 예치금: 500만원"@ko
```

#### 3.2.4 경기 - 135㎡ 초과 모든 면적

```turtle
Individual: Gyeonggi_Deposit_Over135
    Types: DepositRequirement
    Facts:
        appliesInRegion Gyeonggi,
        minArea 135.0,
        maxArea 999999.0,
        requiredDepositAmount 10000000
    Annotations:
        rdfs:label "경기 135㎡ 초과 예치금 요건"@ko,
        rdfs:comment "경기도 지역 전용면적 135㎡ 초과 모든 주택 청약 시 필요한 최소 예치금: 1,000만원"@ko
```

---

## 4. 소득 기준선 개체 (Income Threshold Individuals)

### 4.1 신혼부부 특별공급 소득 기준

#### 4.1.1 신혼부부 우선공급 (100%)

```turtle
Individual: Newlywed_Income_100pct
    Types: IncomeThreshold
    Facts:
        incomePercentage 100,
        appliesTo NewlywedPrioritySupply
    Annotations:
        rdfs:label "신혼부부 우선공급 소득 기준 (100%)"@ko,
        rdfs:comment "신혼부부 특별공급 우선공급(만 6세 이하 자녀 또는 소득 100% 이하)의 소득 기준"@ko
```

#### 4.1.2 신혼부부 일반공급 - 단독소득 (140%)

```turtle
Individual: Newlywed_Income_140pct_SingleIncome
    Types: IncomeThreshold
    Facts:
        incomePercentage 140,
        appliesTo NewlywedCoupleSupply
    Annotations:
        rdfs:label "신혼부부 일반공급 소득 기준 (140%, 단독소득)"@ko,
        rdfs:comment "신혼부부 특별공급 일반공급에서 단독소득 가구의 소득 기준: 도시근로자 월평균 소득의 140%"@ko
```

#### 4.1.3 신혼부부 일반공급 - 맞벌이 (160%)

```turtle
Individual: Newlywed_Income_160pct_DualIncome
    Types: IncomeThreshold
    Facts:
        incomePercentage 160,
        appliesTo NewlywedCoupleSupply
    Annotations:
        rdfs:label "신혼부부 일반공급 소득 기준 (160%, 맞벌이)"@ko,
        rdfs:comment "신혼부부 특별공급 일반공급에서 맞벌이 가구의 소득 기준: 도시근로자 월평균 소득의 160%"@ko
```

### 4.2 생애최초 특별공급 소득 기준

#### 4.2.1 생애최초 (100%)

```turtle
Individual: FirstTimeHomeBuyer_Income_100pct
    Types: IncomeThreshold
    Facts:
        incomePercentage 100,
        appliesTo FirstTimeHomeBuyerSupply
    Annotations:
        rdfs:label "생애최초 특별공급 소득 기준 (100%)"@ko,
        rdfs:comment "생애최초 특별공급의 기본 소득 기준: 도시근로자 월평균 소득의 100%"@ko
```

#### 4.2.2 생애최초 (130%)

```turtle
Individual: FirstTimeHomeBuyer_Income_130pct
    Types: IncomeThreshold
    Facts:
        incomePercentage 130,
        appliesTo FirstTimeHomeBuyerSupply
    Annotations:
        rdfs:label "생애최초 특별공급 소득 기준 (130%)"@ko,
        rdfs:comment "생애최초 특별공급의 완화 소득 기준: 도시근로자 월평균 소득의 130% (추첨제 적용)"@ko
```

### 4.3 국민주택 일반공급 소득 기준

```turtle
Individual: NationalHousing_Income_100pct
    Types: IncomeThreshold
    Facts:
        incomePercentage 100,
        appliesTo GeneralSupply
    Annotations:
        rdfs:label "국민주택 일반공급 소득 기준 (100%)"@ko,
        rdfs:comment "국민주택 일반공급 1순위 자격의 소득 기준: 도시근로자 월평균 소득의 100% 이하"@ko
```

---

## 5. 자산 기준선 개체 (Asset Threshold Individuals)

### 5.1 국민주택 자산 기준 (2024년)

```turtle
Individual: NationalHousing_AssetThreshold_2024
    Types: AssetThreshold
    Facts:
        maxRealEstateValue 215000000,
        maxVehicleValue 37080000,
        yearOfStandard 2024,
        appliesTo GeneralSupply
    Annotations:
        rdfs:label "국민주택 자산 기준 (2024년)"@ko,
        rdfs:comment "국민주택 1순위 신청 시 세대 전체의 자산 보유 한도. 부동산: 2억 1,500만원 이하, 자동차: 3,708만원 이하"@ko
```

---

## 6. 청약 공급 유형 개체 (Subscription Supply Type Individuals)

### 6.1 일반공급

```turtle
Individual: GeneralSupply_Type
    Types: GeneralSupply
    Annotations:
        rdfs:label "일반공급"@ko,
        rdfs:comment "청약통장 가입자 대상 일반 청약 공급"@ko
```

### 6.2 신혼부부 특별공급

```turtle
Individual: NewlywedCoupleSupply_Type
    Types: NewlywedCoupleSupply
    Annotations:
        rdfs:label "신혼부부 특별공급"@ko,
        rdfs:comment "혼인 기간 7년 이내 또는 만 6세 이하 자녀를 둔 한부모가족 대상 특별공급"@ko
```

### 6.3 생애최초 특별공급

```turtle
Individual: FirstTimeHomeBuyerSupply_Type
    Types: FirstTimeHomeBuyerSupply
    Annotations:
        rdfs:label "생애최초 특별공급"@ko,
        rdfs:comment "세대원 전원이 과거 주택 소유 이력이 없는 생애 최초 주택 구매자 대상 특별공급"@ko
```

### 6.4 다자녀가구 특별공급

```turtle
Individual: MultiChildHouseholdSupply_Type
    Types: MultiChildHouseholdSupply
    Annotations:
        rdfs:label "다자녀가구 특별공급"@ko,
        rdfs:comment "만 19세 미만 자녀 3명 이상(태아 포함) 가구 대상 특별공급"@ko
```

### 6.5 노부모부양 특별공급

```turtle
Individual: SupportingAgedParentsSupply_Type
    Types: SupportingAgedParentsSupply
    Annotations:
        rdfs:label "노부모부양 특별공급"@ko,
        rdfs:comment "만 65세 이상 직계존속을 3년 이상 부양하는 무주택 세대주 대상 특별공급"@ko
```

### 6.6 기관추천 특별공급

```turtle
Individual: InstitutionalRecommendation_Type
    Types: InstitutionalRecommendation
    Annotations:
        rdfs:label "기관추천 특별공급"@ko,
        rdfs:comment "국가유공자, 장애인, 중소기업 근로자 등 관련 기관의 추천을 받은 자 대상 특별공급"@ko
```

---

## 7. 추천 기관 개체 (Institution Individuals)

**설계 변경**: 이전에 NationalVeteransInstitution, LocalGovernment, SMEMinistry, NorthKoreanRefugeeFoundation은 Primitive Class로 정의되어 있었으나, 각 기관은 유일한 조직 개체이므로 Individual로 변경되었습니다.

### 7.1 국가보훈처

```turtle
Individual: NationalVeteransInstitution_Korea
    Types: Institution
    Annotations:
        rdfs:label "국가보훈처"@ko,
        rdfs:label "National Veterans Institution"@en,
        rdfs:comment "국가유공자 및 보훈대상자에 대한 기관추천 특별공급 추천 기관"@ko
```

### 7.2 지방자치단체

```turtle
Individual: LocalGovernment_Generic
    Types: Institution
    Annotations:
        rdfs:label "지방자치단체"@ko,
        rdfs:label "Local Government"@en,
        rdfs:comment "장애인, 철거민 등에 대한 기관추천 특별공급 추천 기관"@ko
```

### 7.3 중소벤처기업부

```turtle
Individual: SMEMinistry_Korea
    Types: Institution
    Annotations:
        rdfs:label "중소벤처기업부"@ko,
        rdfs:label "SME Ministry"@en,
        rdfs:comment "중소기업 근로자에 대한 기관추천 특별공급 추천 기관"@ko
```

### 7.4 북한이탈주민지원재단

```turtle
Individual: NorthKoreanRefugeeFoundation_Korea
    Types: Institution
    Annotations:
        rdfs:label "북한이탈주민지원재단"@ko,
        rdfs:label "North Korean Refugee Foundation"@en,
        rdfs:comment "북한이탈주민에 대한 기관추천 특별공급 추천 기관"@ko
```

---

## 8. 사용 지침

### 8.1 개체 참조 방법

SPARQL 쿼리나 추론 규칙에서 이 개체들을 참조할 때는 다음과 같이 사용합니다:

```sparql
# 예시: 서울 지역에 위치한 85㎡ 이하 주택의 예치금 요건 조회
SELECT ?requiredDeposit WHERE {
    ?housing isLocatedIn Seoul .
    ?housing area ?area .
    FILTER (?area <= 85.0)
    
    Seoul_Deposit_Under85 requiredDepositAmount ?requiredDeposit .
}
```

### 8.2 개체 업데이트

- **도시근로자 소득**: 매년 통계청 발표 시 업데이트 필요
- **예치금 요건**: 주택도시기금 정책 변경 시 업데이트
- **자산 기준**: 국토교통부 고시 변경 시 업데이트
- **지역 규제 상태**: 투기과열지구/청약과열지역 지정/해제 시 실시간 반영

### 8.3 확장 방안

- 인천 지역 예치금 요건 추가
- 광역시(부산, 대구, 대전 등) 개체 추가
- 7인 이상 가구 도시근로자 소득 개체 추가 (6인 가구 + 1인당 50만원 규칙 적용)
- 과천, 광명 등 투기과열지구로 지정된 경기도 개별 시 개체 추가

---

## 9. 개체 통계 요약

| 카테고리 | 개체 수 | 비고 |
|---------|--------|------|
| 지역 | 3개 | Seoul, Gyeonggi, Incheon (Class→Individual 변경) |
| 도시근로자 소득 기준 | 6개 | 1~6인 가구 |
| 예치금 요건 | 8개 | 서울 4개, 경기 4개 |
| 소득 기준선 | 6개 | 신혼부부 3개, 생애최초 2개, 국민주택 1개 |
| 자산 기준선 | 1개 | 국민주택 |
| 공급 유형 | 6개 | 일반공급, 특별공급 5종 |
| 추천 기관 | 4개 | 국가보훈처, 지자체, 중소벤처부, 북한이탈주민재단 (Class→Individual 변경) |
| **총합** | **34개** | |

---

## 10. 데이터 출처 및 갱신 이력

- **도시근로자 가구당 월평균 소득**: 통계청 가계동향조사 (2024년 기준)
- **예치금 요건**: 주택도시보증공사(HUG) 청약가이드 (2024년 기준)
- **자산 기준**: 국토교통부 고시 제2024-XXX호
- **최종 갱신일**: 2024년 11월

**주의사항**: 본 문서의 금액 및 기준은 예시이며, 실제 온톨로지 구현 시 최신 공식 데이터로 대체해야 합니다.

