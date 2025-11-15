# 청약 자격 테스트용 가상 주택 및 관련 정보 (Test Housing Data)

본 문서는 Competency Questions(CQ) 검증을 위한 가상의 청약 아파트 및 관련 정보에 해당하는 Individual들을 정의합니다.

**작성일**: 2024년 11월  
**목적**: CQ 1-24번에 대한 SPARQL 쿼리 및 추론 테스트

---

## 1. 테스트용 주택 Individual (Test Housing Individuals)

### 1.1 서울 소재 소형 민영주택 (85㎡ 이하)

```turtle
Individual: TestHousing_Seoul_Small_01
    Types: PrivateHousing
    Facts:
        isLocatedIn Seoul,
        area 59.8,
        price 950000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "서울 강남 래미안 59㎡"@ko,
        rdfs:comment "투기과열지구 소재 소형 주택, 100% 가점제 적용"@ko
```

```turtle
Individual: TestHousing_Seoul_Small_02
    Types: PrivateHousing
    Facts:
        isLocatedIn Seoul,
        area 84.5,
        price 1200000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "서울 송파 헬리오시티 84㎡"@ko,
        rdfs:comment "투기과열지구 소재, 가점제 100% 적용"@ko
```

### 1.2 서울 소재 중대형 민영주택 (85㎡ 초과)

```turtle
Individual: TestHousing_Seoul_Large_01
    Types: PrivateHousing
    Facts:
        isLocatedIn Seoul,
        area 101.5,
        price 1800000000,
        usesSelectionMethod TestSelection_Mixed_50_50
    Annotations:
        rdfs:label "서울 마포 래미안 101㎡"@ko,
        rdfs:comment "투기과열지구 소재, 가점제 50% + 추첨제 50%"@ko
```

```turtle
Individual: TestHousing_Seoul_Large_02
    Types: PrivateHousing
    Facts:
        isLocatedIn Seoul,
        area 140.2,
        price 2500000000,
        usesSelectionMethod TestSelection_Mixed_50_50
    Annotations:
        rdfs:label "서울 서초 자이 140㎡"@ko,
        rdfs:comment "대형 평형, 혼합 선정 방식"@ko
```

### 1.3 경기도 소재 민영주택

```turtle
Individual: TestHousing_Gyeonggi_01
    Types: PrivateHousing
    Facts:
        isLocatedIn Gyeonggi,
        area 74.9,
        price 650000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "경기 성남 판교 푸르지오 74㎡"@ko,
        rdfs:comment "경기도 소재, 청약과열지역 아님"@ko
```

```turtle
Individual: TestHousing_Gyeonggi_02
    Types: PrivateHousing
    Facts:
        isLocatedIn Gyeonggi,
        area 84.3,
        price 520000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "경기 수원 광교 호반베르디움 84㎡"@ko,
        rdfs:comment "경기도 소재 중소형 주택"@ko
```

### 1.4 서울 소재 국민주택

```turtle
Individual: TestHousing_Seoul_National_01
    Types: NationalHousing
    Facts:
        isLocatedIn Seoul,
        area 46.5,
        price 380000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "서울 강동 LH행복주택 46㎡"@ko,
        rdfs:comment "국민주택, 소득 및 자산 기준 적용"@ko
```

```turtle
Individual: TestHousing_Seoul_National_02
    Types: NationalHousing
    Facts:
        isLocatedIn Seoul,
        area 59.5,
        price 450000000,
        usesSelectionMethod TestSelection_PointBased_100pct
    Annotations:
        rdfs:label "서울 은평 SH공사 59㎡"@ko,
        rdfs:comment "서울시 공공주택"@ko
```

### 1.5 소형·저가주택 (무주택 기간 예외)

```turtle
Individual: TestHousing_SmallLowPrice_01
    Types: Housing
    Facts:
        isLocatedIn Seoul,
        area 42.0,
        price 120000000,
        disposalDate "2021-05-15"^^xsd:date
    Annotations:
        rdfs:label "서울 노원 소형주택 42㎡"@ko,
        rdfs:comment "면적 60㎡ 이하, 가격 1.3억 이하 → SmallLowPriceHousing_Defined로 자동 분류"@ko
```

```turtle
Individual: TestHousing_SmallLowPrice_02
    Types: Housing
    Facts:
        isLocatedIn Incheon,
        area 55.0,
        price 95000000
    Annotations:
        rdfs:label "인천 부평 소형빌라 55㎡"@ko,
        rdfs:comment "현재 소유 중인 소형저가주택 예시"@ko
```

### 1.6 사후접수주택 (무순위)

```turtle
Individual: TestHousing_PostSubscription_01
    Types: PostSubscriptionHousing
    Facts:
        isLocatedIn Seoul,
        area 84.0,
        price 980000000
    Annotations:
        rdfs:label "서울 강서 미분양 무순위 84㎡"@ko,
        rdfs:comment "1, 2순위 미계약 물량"@ko
```

---

## 2. 테스트용 선정 방식 Individual (Selection Method Individuals)

### 2.1 가점제 100%

```turtle
Individual: TestSelection_PointBased_100pct
    Types: PointBasedSelection
    Facts:
        selectionRatio 1.0
    Annotations:
        rdfs:label "가점제 100%"@ko,
        rdfs:comment "85㎡ 이하 투기과열지구 주택에 적용"@ko
```

### 2.2 혼합 선정 (가점 50% + 추첨 50%)

```turtle
Individual: TestSelection_Mixed_50_50
    Types: SelectionMethod
    Facts:
        usesSelectionMethod TestSelection_PointBased_50pct,
        usesSelectionMethod TestSelection_Lottery_50pct
    Annotations:
        rdfs:label "혼합 선정 방식"@ko,
        rdfs:comment "85㎡ 초과 주택에 적용"@ko
```

```turtle
Individual: TestSelection_PointBased_50pct
    Types: PointBasedSelection
    Facts:
        selectionRatio 0.5
```

```turtle
Individual: TestSelection_Lottery_50pct
    Types: LotteryBasedSelection
    Facts:
        selectionRatio 0.5
```

---

## 3. 테스트용 청약 신청 Individual (Subscription Application Individuals)

### 3.1 일반공급 신청

```turtle
Individual: TestApp_General_01
    Types: GeneralSupply
    Facts:
        isForHousing TestHousing_Seoul_Small_01,
        recruitmentAnnouncementDate "2024-11-10"^^xsd:date
    Annotations:
        rdfs:label "서울 강남 래미안 일반공급"@ko
```

```turtle
Individual: TestApp_General_02
    Types: GeneralSupply
    Facts:
        isForHousing TestHousing_Gyeonggi_01,
        recruitmentAnnouncementDate "2024-11-12"^^xsd:date
    Annotations:
        rdfs:label "경기 판교 일반공급"@ko
```

### 3.2 신혼부부 특별공급 신청

```turtle
Individual: TestApp_Newlywed_01
    Types: NewlywedCoupleSupply
    Facts:
        isForHousing TestHousing_Seoul_Small_02,
        recruitmentAnnouncementDate "2024-11-10"^^xsd:date
    Annotations:
        rdfs:label "서울 송파 신혼부부 특공"@ko
```

```turtle
Individual: TestApp_Newlywed_02
    Types: NewlywedCoupleSupply
    Facts:
        isForHousing TestHousing_Gyeonggi_02,
        recruitmentAnnouncementDate "2024-11-15"^^xsd:date
    Annotations:
        rdfs:label "경기 수원 신혼부부 특공"@ko
```

### 3.3 생애최초 특별공급 신청

```turtle
Individual: TestApp_FirstTime_01
    Types: FirstTimeHomeBuyerSupply
    Facts:
        isForHousing TestHousing_Seoul_Large_01,
        recruitmentAnnouncementDate "2024-11-10"^^xsd:date
    Annotations:
        rdfs:label "서울 마포 생애최초 특공"@ko
```

### 3.4 다자녀가구 특별공급 신청

```turtle
Individual: TestApp_MultiChild_01
    Types: MultiChildHouseholdSupply
    Facts:
        isForHousing TestHousing_Seoul_Small_01,
        recruitmentAnnouncementDate "2024-11-10"^^xsd:date
    Annotations:
        rdfs:label "서울 강남 다자녀가구 특공"@ko
```

### 3.5 노부모부양 특별공급 신청

```turtle
Individual: TestApp_AgedParents_01
    Types: SupportingAgedParentsSupply
    Facts:
        isForHousing TestHousing_Seoul_Small_02,
        recruitmentAnnouncementDate "2024-11-10"^^xsd:date
    Annotations:
        rdfs:label "서울 송파 노부모부양 특공"@ko
```

### 3.6 기관추천 특별공급 신청

```turtle
Individual: TestApp_Institutional_01
    Types: InstitutionalRecommendation
    Facts:
        isForHousing TestHousing_Gyeonggi_01,
        recruitmentAnnouncementDate "2024-11-12"^^xsd:date
    Annotations:
        rdfs:label "경기 판교 기관추천 특공"@ko
```

---

## 4. 테스트용 예치금 요건 (이미 individuals.md에 정의됨)

**참고**: `Seoul_Deposit_Under85`, `Seoul_Deposit_85to102`, `Gyeonggi_Deposit_Under85` 등은 이미 `individuals.md`에 정의되어 있으므로 재사용합니다.

---

## 5. 테스트용 소득 기준 (이미 individuals.md에 정의됨)

**참고**: `UrbanWorker_2024_2person`, `UrbanWorker_2024_4person`, `Newlywed_Income_140pct_SingleIncome`, `FirstTimeHomeBuyer_Income_130pct` 등은 이미 `individuals.md`에 정의되어 있으므로 재사용합니다.

---

## 6. 테스트용 당첨 이력 Individual (Winning Record Individuals)

### 6.1 5년 이내 당첨 (제한 기간 중)

```turtle
Individual: TestWinningRecord_Recent_01
    Types: WinningRecord
    Facts:
        winningDate "2021-06-20"^^xsd:date,
        contractCompleted true,
        isSubjectToRestriction true,
        restrictionPeriodInYears 5
    Annotations:
        rdfs:label "2021년 당첨 이력 (제한 중)"@ko,
        rdfs:comment "2021년 당첨, 5년 제한 → 2026년까지 1순위 불가"@ko
```

```turtle
Individual: TestWinningRecord_Recent_02
    Types: WinningRecord
    Facts:
        winningDate "2020-03-10"^^xsd:date,
        contractCompleted false,
        isSubjectToRestriction true,
        restrictionPeriodInYears 5
    Annotations:
        rdfs:label "2020년 당첨 후 계약 포기"@ko,
        rdfs:comment "계약 포기해도 재당첨 제한 적용"@ko
```

### 6.2 5년 이후 당첨 (제한 기간 만료)

```turtle
Individual: TestWinningRecord_Old_01
    Types: WinningRecord
    Facts:
        winningDate "2014-08-15"^^xsd:date,
        contractCompleted true,
        isSubjectToRestriction true,
        restrictionPeriodInYears 5
    Annotations:
        rdfs:label "2014년 당첨 이력 (제한 만료)"@ko,
        rdfs:comment "10년 전 당첨, 현재는 자격 회복"@ko
```

---

## 7. 테스트용 주택 소유 이력 Individual (Housing Ownership History Individuals)

### 7.1 소형·저가주택 처분 이력

```turtle
Individual: TestOwnership_SmallLowPrice_Disposed
    Types: HousingOwnershipHistory
    Facts:
        ownedHousing TestHousing_SmallLowPrice_01,
        ownershipStartDate "2019-03-01"^^xsd:date,
        ownershipEndDate "2021-05-15"^^xsd:date
    Annotations:
        rdfs:label "소형저가주택 처분 이력"@ko,
        rdfs:comment "2021년 5월 처분 → 무주택 기간 시작일"@ko
```

### 7.2 일반 주택 소유 이력

```turtle
Individual: TestOwnership_Regular_Past
    Types: HousingOwnershipHistory
    Facts:
        ownedHousing TestHousing_Gyeonggi_01,
        ownershipStartDate "2015-06-01"^^xsd:date,
        ownershipEndDate "2018-12-31"^^xsd:date
    Annotations:
        rdfs:label "일반 주택 과거 소유"@ko,
        rdfs:comment "생애최초 특공 자격 없음"@ko
```

### 7.3 현재 주택 소유 이력

```turtle
Individual: TestOwnership_Current_01
    Types: HousingOwnershipHistory
    Facts:
        ownedHousing TestHousing_Gyeonggi_02,
        ownershipStartDate "2022-01-15"^^xsd:date
    Annotations:
        rdfs:label "현재 1주택 보유"@ko,
        rdfs:comment "ownershipEndDate 없음 → 현재 소유 중"@ko
```

---

## 8. 테스트용 거주 이력 Individual (Residence History Individuals)

### 8.1 서울 장기 거주 (3년 이상)

```turtle
Individual: TestResidence_Seoul_LongTerm
    Types: ResidenceHistory
    Facts:
        residedIn Seoul,
        residenceStartDate "2020-01-01"^^xsd:date,
        residenceDurationInYears 4.9
    Annotations:
        rdfs:label "서울 장기 거주 이력"@ko,
        rdfs:comment "2020년부터 현재까지 약 5년"@ko
```

### 8.2 경기도 중기 거주 (1-3년)

```turtle
Individual: TestResidence_Gyeonggi_MidTerm
    Types: ResidenceHistory
    Facts:
        residedIn Gyeonggi,
        residenceStartDate "2022-06-01"^^xsd:date,
        residenceDurationInYears 2.4
    Annotations:
        rdfs:label "경기도 중기 거주 이력"@ko
```

### 8.3 인천 단기 거주 (1년 미만)

```turtle
Individual: TestResidence_Incheon_ShortTerm
    Types: ResidenceHistory
    Facts:
        residedIn Incheon,
        residenceStartDate "2024-05-01"^^xsd:date,
        residenceDurationInYears 0.5
    Annotations:
        rdfs:label "인천 단기 거주 이력"@ko
```

---

## 9. 테스트용 소득세 납부 이력 Individual (Tax Payment History Individuals)

### 9.1 5년 이상 납부 (생애최초 자격 충족)

```turtle
Individual: TestTax_2019
    Types: TaxPaymentHistory
    Facts:
        taxYear "2019"^^xsd:gYear,
        taxAmount 2500000
```

```turtle
Individual: TestTax_2020
    Types: TaxPaymentHistory
    Facts:
        taxYear "2020"^^xsd:gYear,
        taxAmount 3000000
```

```turtle
Individual: TestTax_2021
    Types: TaxPaymentHistory
    Facts:
        taxYear "2021"^^xsd:gYear,
        taxAmount 3200000
```

```turtle
Individual: TestTax_2022
    Types: TaxPaymentHistory
    Facts:
        taxYear "2022"^^xsd:gYear,
        taxAmount 3500000
```

```turtle
Individual: TestTax_2023
    Types: TaxPaymentHistory
    Facts:
        taxYear "2023"^^xsd:gYear,
        taxAmount 3800000
```

### 9.2 3년 납부 (자격 미달)

```turtle
Individual: TestTax_Short_2022
    Types: TaxPaymentHistory
    Facts:
        taxYear "2022"^^xsd:gYear,
        taxAmount 1500000
```

```turtle
Individual: TestTax_Short_2023
    Types: TaxPaymentHistory
    Facts:
        taxYear "2023"^^xsd:gYear,
        taxAmount 1800000
```

```turtle
Individual: TestTax_Short_2024
    Types: TaxPaymentHistory
    Facts:
        taxYear "2024"^^xsd:gYear,
        taxAmount 2000000
```

---

## 10. 주택 및 관련 정보 통계

| 카테고리 | 개체 수 | 비고 |
|---------|--------|------|
| 테스트 주택 | 11개 | 서울 6개, 경기 3개, 인천 1개, 소형저가 2개 |
| 선정 방식 | 3개 | 가점제 100%, 혼합, 구성 요소 |
| 청약 신청 | 8개 | 일반공급 2개, 특별공급 6개 |
| 당첨 이력 | 3개 | 제한 중 2개, 만료 1개 |
| 소유 이력 | 3개 | 소형저가 처분, 과거 소유, 현재 소유 |
| 거주 이력 | 3개 | 장기, 중기, 단기 |
| 소득세 납부 이력 | 8개 | 5년 납부 5개, 3년 납부 3개 |
| **총합** | **39개** | |

---

## 11. CQ 매핑 및 활용 가이드

### CQ 1, 2, 3 (기본 자격)
- **사용 주택**: TestHousing_Seoul_Small_01
- **사용 신청**: TestApp_General_01
- **키워드**: 성년(age >= 19), 청약통장 가입 기간, 무주택세대구성원

### CQ 4 (해당/기타 지역)
- **사용 주택**: TestHousing_Seoul_Small_01 (서울)
- **경기 거주자**: TestResidence_Gyeonggi_MidTerm 활용
- **키워드**: OtherRegionApplicant, MetropolitanArea

### CQ 5 (소형저가주택 처분)
- **사용 이력**: TestOwnership_SmallLowPrice_Disposed
- **사용 주택**: TestHousing_SmallLowPrice_01
- **키워드**: homelessStartDate, ownershipEndDate

### CQ 7 (투기과열지구 1주택자)
- **사용 주택**: TestHousing_Seoul_Small_01
- **사용 소유**: TestOwnership_Current_01
- **키워드**: isSpeculativeOverheatedZone, FirstPriorityApplicant_PrivateHousing

### CQ 12 (예치금 부족)
- **사용 주택**: TestHousing_Seoul_Small_01 (85㎡ 이하)
- **필요 예치금**: 3,000,000원
- **키워드**: hasDepositShortage, requiredDepositAmount

### CQ 17 (기관추천)
- **사용 신청**: TestApp_Institutional_01
- **추천 기관**: LocalGovernment_Generic
- **키워드**: isRecommendedBy, hasDisability

### CQ 20-24 (소득/자산 기준)
- **사용 소득 기준**: UrbanWorker_2024_*person
- **사용 기준선**: Newlywed_Income_140pct_SingleIncome 등
- **키워드**: monthlyAverageIncome, meetsIncomeThreshold

---

## 12. 데이터 확장 방안

### 12.1 추가 가능한 주택 유형
- 재개발/재건축 주택
- 오피스텔 (주거용)
- 도시형 생활주택
- 행복주택

### 12.2 추가 가능한 지역
- 과천, 광명 (투기과열지구 경기도 지역)
- 부산, 대구, 대전 (광역시)
- 세종시 (특별자치시)

### 12.3 추가 가능한 시나리오
- 예비신혼부부 케이스
- 한부모가족 케이스
- 장애인 기관추천 케이스
- 국가유공자 기관추천 케이스
- 중소기업 근로자 케이스

---

**주의사항**: 본 문서의 모든 Individual은 테스트 및 검증 목적으로 작성된 가상 데이터입니다. 실제 온톨로지 적용 시에는 실제 데이터로 대체해야 합니다.

