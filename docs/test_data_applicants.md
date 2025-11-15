# 청약 자격 테스트용 가상 신청자 및 관련 정보 (Test Applicants Data)

본 문서는 Competency Questions(CQ) 검증을 위한 가상의 신청자, 세대, 세대원 및 관련 정보에 해당하는 Individual들을 정의합니다.

**작성일**: 2024년 11월  
**목적**: CQ 1-24번에 대한 SPARQL 쿼리 및 추론 테스트

---

## 1. CQ 1-3 대응: 기본 자격 신청자 A (성년, 청약통장, 무주택세대)

### 1.1 신청자 A (31세, 서울 3년 거주)

```turtle
Individual: TestApplicant_A
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "800101-1234567",
        name "김철수",
        age "31"^^xsd:integer,
        maritalStatus "기혼",
        marriageRegistrationDate "2021-03-15"^^xsd:date,
        livesIn Seoul,
        belongsToHousehold TestHousehold_A,
        hasSubscriptionAccount TestAccount_A,
        appliesFor TestApp_General_01,
        homelessStartDate "2019-01-01"^^xsd:date,
        hasResidenceHistory TestResidence_Seoul_LongTerm,
        totalSubscriptionPoints 65
    Annotations:
        rdfs:label "신청자 A (김철수)"@ko,
        rdfs:comment "CQ 1-3 대응: 성년, 청약통장 2년 이상, 무주택세대주"@ko
```

### 1.2 신청자 A의 청약통장

```turtle
Individual: TestAccount_A
    Types: SubscriptionAccount
    Facts:
        accountNumber "1234-5678-9012",
        accountType "주택청약종합저축",
        accountOpeningDate "2022-05-10"^^xsd:date,
        depositAmount 3500000,
        monthlyPaymentCount 30
    Annotations:
        rdfs:label "신청자 A의 청약통장"@ko,
        rdfs:comment "가입 기간 2.5년, 예치금 350만원, 월납입 30회"@ko
```

### 1.3 신청자 A의 세대

```turtle
Individual: TestHousehold_A
    Types: Household
    Facts:
        hasMember TestApplicant_A,
        hasMember TestSpouse_A,
        hasMember TestChild_A1,
        hasHead TestApplicant_A,
        hasIncome TestIncome_A,
        hasTotalAsset TestAsset_A
    Annotations:
        rdfs:label "신청자 A의 세대"@ko,
        rdfs:comment "세대주 + 배우자 + 미성년 자녀 1명"@ko
```

### 1.4 배우자 D

```turtle
Individual: TestSpouse_A
    Types: HouseholdMember
    Facts:
        nationalID "850615-2345678",
        name "이영희",
        age "28"^^xsd:integer,
        maritalStatus "기혼",
        belongsToHousehold TestHousehold_A,
        hasSpouse TestApplicant_A,
        personalIncome 3500000
    Annotations:
        rdfs:label "배우자 D (이영희)"@ko
```

### 1.5 미성년 자녀 E

```turtle
Individual: TestChild_A1
    Types: Child, MinorChild
    Facts:
        nationalID "201506-3456789",
        name "김민지",
        age "9"^^xsd:integer,
        belongsToHousehold TestHousehold_A,
        hasParent TestApplicant_A,
        hasParent TestSpouse_A
    Annotations:
        rdfs:label "자녀 E (김민지)"@ko,
        rdfs:comment "만 9세 미성년 자녀"@ko
```

### 1.6 세대 소득 및 자산

```turtle
Individual: TestIncome_A
    Types: Income
    Facts:
        monthlyAverageIncome 7200000
    Annotations:
        rdfs:comment "신청자 3,700만원 + 배우자 3,500만원 = 7,200만원"@ko
```

```turtle
Individual: TestAsset_A
    Types: Asset
    Facts:
        realEstateAssetValue 50000000,
        vehicleAssetValue 15000000
    Annotations:
        rdfs:comment "부동산 5천만원, 차량 1천5백만원 → 국민주택 자산 기준 충족"@ko
```

---

## 2. CQ 4 대응: 경기 거주 신청자 F (기타 지역 자격)

### 2.1 신청자 F (경기 거주, 서울 아파트 신청)

```turtle
Individual: TestApplicant_F
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "900315-1567890",
        name "박준호",
        age "34"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Gyeonggi,
        belongsToHousehold TestHousehold_F,
        hasSubscriptionAccount TestAccount_F,
        appliesFor TestApp_General_01,
        homelessStartDate "2020-01-01"^^xsd:date,
        hasResidenceHistory TestResidence_Gyeonggi_MidTerm
    Annotations:
        rdfs:label "신청자 F (박준호)"@ko,
        rdfs:comment "CQ 4 대응: 경기 거주, 서울 주택 신청 → OtherRegionApplicant"@ko
```

### 2.2 신청자 F의 청약통장

```turtle
Individual: TestAccount_F
    Types: SubscriptionAccount
    Facts:
        accountNumber "2345-6789-0123",
        accountType "주택청약종합저축",
        accountOpeningDate "2021-01-10"^^xsd:date,
        depositAmount 2800000,
        monthlyPaymentCount 45
    Annotations:
        rdfs:comment "가입 기간 3.8년, 예치금 280만원"@ko
```

### 2.3 신청자 F의 세대

```turtle
Individual: TestHousehold_F
    Types: Household
    Facts:
        hasMember TestApplicant_F,
        hasMember TestSpouse_F,
        hasHead TestApplicant_F,
        hasIncome TestIncome_F
    Annotations:
        rdfs:label "신청자 F의 세대"@ko,
        rdfs:comment "부부 2인 가구"@ko
```

```turtle
Individual: TestSpouse_F
    Types: HouseholdMember
    Facts:
        nationalID "920808-2678901",
        name "최수진",
        age "32"^^xsd:integer,
        belongsToHousehold TestHousehold_F,
        hasSpouse TestApplicant_F,
        personalIncome 4200000
```

```turtle
Individual: TestIncome_F
    Types: Income
    Facts:
        monthlyAverageIncome 8500000
    Annotations:
        rdfs:comment "부부 합산 소득 850만원"@ko
```

---

## 3. CQ 5 대응: 소형·저가주택 처분 신청자 G (무주택 기간 산정)

### 3.1 배우자 G (소형·저가주택 처분 이력)

```turtle
Individual: TestApplicant_G
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "870420-1789012",
        name "정대현",
        age "37"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_G,
        hasSubscriptionAccount TestAccount_G,
        appliesFor TestApp_General_02,
        hasResidenceHistory TestResidence_Seoul_LongTerm
    Annotations:
        rdfs:label "신청자 G (정대현)"@ko,
        rdfs:comment "CQ 5 대응: 배우자가 소형저가주택 처분 이력 있음"@ko
```

### 3.2 배우자 (소형·저가주택 처분자)

```turtle
Individual: TestSpouse_G
    Types: HouseholdMember
    Facts:
        nationalID "880705-2890123",
        name "한지민",
        age "36"^^xsd:integer,
        belongsToHousehold TestHousehold_G,
        hasSpouse TestApplicant_G,
        hasOwnershipHistory TestOwnership_SmallLowPrice_Disposed,
        personalIncome 4000000
    Annotations:
        rdfs:label "배우자 G (한지민)"@ko,
        rdfs:comment "2021년 5월 소형저가주택 처분 → 무주택 기간 2021-05-15부터"@ko
```

### 3.3 신청자 G의 세대

```turtle
Individual: TestHousehold_G
    Types: Household
    Facts:
        hasMember TestApplicant_G,
        hasMember TestSpouse_G,
        hasHead TestApplicant_G,
        hasIncome TestIncome_G
```

```turtle
Individual: TestAccount_G
    Types: SubscriptionAccount
    Facts:
        accountNumber "3456-7890-1234",
        accountOpeningDate "2020-08-01"^^xsd:date,
        depositAmount 3200000,
        monthlyPaymentCount 52
```

```turtle
Individual: TestIncome_G
    Types: Income
    Facts:
        monthlyAverageIncome 7800000
```

---

## 4. CQ 7 대응: 투기과열지구 1주택자 신청자 L

### 4.1 신청자 L (경기 과천 거주, 1주택자)

```turtle
Individual: TestApplicant_L
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "860910-1901234",
        name "송민수",
        age "38"^^xsd:integer,
        maritalStatus "기혼",
        livesIn TestRegion_Gwacheon,
        belongsToHousehold TestHousehold_L,
        hasSubscriptionAccount TestAccount_L,
        appliesFor TestApp_General_01,
        owns TestHousing_Gyeonggi_02,
        hasOwnershipHistory TestOwnership_Current_01
    Annotations:
        rdfs:label "신청자 L (송민수)"@ko,
        rdfs:comment "CQ 7 대응: 투기과열지구 거주, 1주택 보유 → 조건부 1순위"@ko
```

### 4.2 과천 지역 Individual (투기과열지구)

```turtle
Individual: TestRegion_Gwacheon
    Types: Region, MetropolitanArea
    Facts:
        regionName "과천",
        isSpeculativeOverheatedZone true,
        isSubscriptionOverheatedArea true
    Annotations:
        rdfs:label "경기 과천시"@ko,
        rdfs:comment "경기도 내 투기과열지구"@ko
```

### 4.3 신청자 L의 세대

```turtle
Individual: TestHousehold_L
    Types: Household
    Facts:
        hasMember TestApplicant_L,
        hasMember TestSpouse_L,
        hasHead TestApplicant_L,
        hasIncome TestIncome_L
```

```turtle
Individual: TestSpouse_L
    Types: HouseholdMember
    Facts:
        nationalID "880225-2012345",
        name "윤서연",
        age "36"^^xsd:integer,
        belongsToHousehold TestHousehold_L,
        hasSpouse TestApplicant_L,
        personalIncome 5000000
```

```turtle
Individual: TestAccount_L
    Types: SubscriptionAccount
    Facts:
        accountNumber "4567-8901-2345",
        accountOpeningDate "2019-03-01"^^xsd:date,
        depositAmount 8000000,
        monthlyPaymentCount 68
```

```turtle
Individual: TestIncome_L
    Types: Income
    Facts:
        monthlyAverageIncome 12000000
    Annotations:
        rdfs:comment "고소득 가구 (1,200만원)"@ko
```

---

## 5. CQ 12 대응: 예치금 부족 신청자 K

### 5.1 신청자 K (경기 거주, 서울 85㎡ 이하 주택 신청)

```turtle
Individual: TestApplicant_K
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "910512-1123456",
        name "이승현",
        age "33"^^xsd:integer,
        maritalStatus "미혼",
        livesIn Gyeonggi,
        belongsToHousehold TestHousehold_K,
        hasSubscriptionAccount TestAccount_K,
        appliesFor TestApp_General_01,
        homelessStartDate "2018-01-01"^^xsd:date
    Annotations:
        rdfs:label "신청자 K (이승현)"@ko,
        rdfs:comment "CQ 12 대응: 예치금 250만원, 50만원 부족"@ko
```

### 5.2 신청자 K의 청약통장 (예치금 부족)

```turtle
Individual: TestAccount_K
    Types: SubscriptionAccount
    Facts:
        accountNumber "5678-9012-3456",
        accountOpeningDate "2021-06-01"^^xsd:date,
        depositAmount 2500000,
        monthlyPaymentCount 41
    Annotations:
        rdfs:comment "예치금 250만원 → 서울 85㎡ 이하는 300만원 필요 → 50만원 부족"@ko
```

### 5.3 신청자 K의 세대

```turtle
Individual: TestHousehold_K
    Types: Household, SinglePersonHousehold_Defined
    Facts:
        hasMember TestApplicant_K,
        hasHead TestApplicant_K,
        hasIncome TestIncome_K
    Annotations:
        rdfs:comment "1인 가구"@ko
```

```turtle
Individual: TestIncome_K
    Types: Income
    Facts:
        monthlyAverageIncome 4200000
```

---

## 6. CQ 13 대응: 신혼부부 특별공급 신청자 R

### 6.1 신청자 R (결혼 5년차, 만 2세 자녀)

```turtle
Individual: TestApplicant_R
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "890620-1234567",
        name "최준영",
        age "35"^^xsd:integer,
        maritalStatus "기혼",
        marriageRegistrationDate "2019-09-20"^^xsd:date,
        livesIn Seoul,
        belongsToHousehold TestHousehold_R,
        hasSubscriptionAccount TestAccount_R,
        appliesFor TestApp_Newlywed_01,
        homelessStartDate "2018-01-01"^^xsd:date,
        hasChild TestChild_R1
    Annotations:
        rdfs:label "신청자 R (최준영)"@ko,
        rdfs:comment "CQ 13 대응: 신혼부부 특공, 결혼 5년, 자녀 1명"@ko
```

### 6.2 신청자 R의 세대

```turtle
Individual: TestHousehold_R
    Types: Household
    Facts:
        hasMember TestApplicant_R,
        hasMember TestSpouse_R,
        hasMember TestChild_R1,
        hasHead TestApplicant_R,
        hasIncome TestIncome_R
```

```turtle
Individual: TestSpouse_R
    Types: HouseholdMember
    Facts:
        nationalID "910815-2345678",
        name "강은지",
        age "33"^^xsd:integer,
        maritalStatus "기혼",
        belongsToHousehold TestHousehold_R,
        hasSpouse TestApplicant_R,
        personalIncome 4500000
```

```turtle
Individual: TestChild_R1
    Types: Child, MinorChild, InfantChild
    Facts:
        nationalID "220310-3456789",
        name "최서준",
        age "2"^^xsd:integer,
        belongsToHousehold TestHousehold_R,
        hasParent TestApplicant_R,
        hasParent TestSpouse_R
    Annotations:
        rdfs:comment "만 2세 자녀 → 우선공급 대상"@ko
```

```turtle
Individual: TestAccount_R
    Types: SubscriptionAccount
    Facts:
        accountNumber "6789-0123-4567",
        accountOpeningDate "2023-06-01"^^xsd:date,
        depositAmount 2000000,
        monthlyPaymentCount 17
    Annotations:
        rdfs:comment "특공은 6개월 이상이면 충족"@ko
```

```turtle
Individual: TestIncome_R
    Types: Income
    Facts:
        monthlyAverageIncome 8000000
    Annotations:
        rdfs:comment "3인 가구 기준 5,400만원의 140% = 7,560만원 이하 충족"@ko
```

---

## 7. CQ 14 대응: 생애최초 특별공급 신청자 S

### 7.1 신청자 S (만 35세 미혼 1인 가구)

```turtle
Individual: TestApplicant_S
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "890225-2123456",
        name "정수아",
        age "35"^^xsd:integer,
        maritalStatus "미혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_S,
        hasSubscriptionAccount TestAccount_S,
        appliesFor TestApp_FirstTime_01,
        homelessStartDate "1989-02-25"^^xsd:date,
        taxPaymentDuration 7,
        hasTaxPaymentHistory TestTax_2019,
        hasTaxPaymentHistory TestTax_2020,
        hasTaxPaymentHistory TestTax_2021,
        hasTaxPaymentHistory TestTax_2022,
        hasTaxPaymentHistory TestTax_2023
    Annotations:
        rdfs:label "신청자 S (정수아)"@ko,
        rdfs:comment "CQ 14 대응: 미혼 1인 가구, 소득세 5년 이상 납부"@ko
```

### 7.2 신청자 S의 세대

```turtle
Individual: TestHousehold_S
    Types: Household, SinglePersonHousehold_Defined
    Facts:
        hasMember TestApplicant_S,
        hasHead TestApplicant_S,
        hasIncome TestIncome_S
    Annotations:
        rdfs:comment "1인 가구 → 2인 가구 기준 적용"@ko
```

```turtle
Individual: TestAccount_S
    Types: SubscriptionAccount
    Facts:
        accountNumber "7890-1234-5678",
        accountOpeningDate "2020-01-15"^^xsd:date,
        depositAmount 10000000,
        monthlyPaymentCount 58
```

```turtle
Individual: TestIncome_S
    Types: Income
    Facts:
        monthlyAverageIncome 5500000
    Annotations:
        rdfs:comment "2인 가구 기준 5,000만원의 130% = 6,500만원 이하 충족"@ko
```

---

## 8. CQ 15 대응: 다자녀가구 특별공급 신청자 T

### 8.1 신청자 T (3명 자녀: 18세, 10세, 5세)

```turtle
Individual: TestApplicant_T
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "850710-1345678",
        name "김태호",
        age "39"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_T,
        hasSubscriptionAccount TestAccount_T,
        appliesFor TestApp_MultiChild_01,
        homelessStartDate "2019-01-01"^^xsd:date,
        hasChild TestChild_T1,
        hasChild TestChild_T2,
        hasChild TestChild_T3
    Annotations:
        rdfs:label "신청자 T (김태호)"@ko,
        rdfs:comment "CQ 15 대응: 다자녀가구 특공, 미성년 자녀 3명"@ko
```

### 8.2 신청자 T의 세대

```turtle
Individual: TestHousehold_T
    Types: Household
    Facts:
        hasMember TestApplicant_T,
        hasMember TestSpouse_T,
        hasMember TestChild_T1,
        hasMember TestChild_T2,
        hasMember TestChild_T3,
        hasHead TestApplicant_T,
        hasIncome TestIncome_T
    Annotations:
        rdfs:comment "5인 가구 (부부 + 자녀 3명)"@ko
```

```turtle
Individual: TestSpouse_T
    Types: HouseholdMember
    Facts:
        nationalID "860920-2456789",
        name "박미경",
        age "38"^^xsd:integer,
        belongsToHousehold TestHousehold_T,
        hasSpouse TestApplicant_T,
        personalIncome 3800000
```

```turtle
Individual: TestChild_T1
    Types: Child, MinorChild
    Facts:
        nationalID "060415-3567890",
        name "김지우",
        age "18"^^xsd:integer,
        belongsToHousehold TestHousehold_T,
        hasParent TestApplicant_T,
        hasParent TestSpouse_T
    Annotations:
        rdfs:comment "만 18세 자녀"@ko
```

```turtle
Individual: TestChild_T2
    Types: Child, MinorChild
    Facts:
        nationalID "140625-4678901",
        name "김서윤",
        age "10"^^xsd:integer,
        belongsToHousehold TestHousehold_T,
        hasParent TestApplicant_T,
        hasParent TestSpouse_T
    Annotations:
        rdfs:comment "만 10세 자녀"@ko
```

```turtle
Individual: TestChild_T3
    Types: Child, MinorChild, InfantChild
    Facts:
        nationalID "190820-3789012",
        name "김예준",
        age "5"^^xsd:integer,
        belongsToHousehold TestHousehold_T,
        hasParent TestApplicant_T,
        hasParent TestSpouse_T
    Annotations:
        rdfs:comment "만 5세 자녀"@ko
```

```turtle
Individual: TestAccount_T
    Types: SubscriptionAccount
    Facts:
        accountNumber "8901-2345-6789",
        accountOpeningDate "2022-12-01"^^xsd:date,
        depositAmount 3000000,
        monthlyPaymentCount 23
```

```turtle
Individual: TestIncome_T
    Types: Income
    Facts:
        monthlyAverageIncome 8200000
```

---

## 9. CQ 16 대응: 노부모부양 특별공급 신청자 U

### 9.1 신청자 U (만 67세 아버지 5년 부양)

```turtle
Individual: TestApplicant_U
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "830512-1456789",
        name "이동진",
        age "41"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_U,
        hasSubscriptionAccount TestAccount_U,
        appliesFor TestApp_AgedParents_01,
        homelessStartDate "2018-01-01"^^xsd:date,
        hasDependent TestParent_U1,
        hasElderlyDependent TestParent_U1
    Annotations:
        rdfs:label "신청자 U (이동진)"@ko,
        rdfs:comment "CQ 16 대응: 노부모부양 특공, 만 65세 이상 부모 3년 이상 부양"@ko
```

### 9.2 신청자 U의 세대

```turtle
Individual: TestHousehold_U
    Types: Household
    Facts:
        hasMember TestApplicant_U,
        hasMember TestSpouse_U,
        hasMember TestParent_U1,
        hasHead TestApplicant_U,
        hasIncome TestIncome_U
```

```turtle
Individual: TestSpouse_U
    Types: HouseholdMember
    Facts:
        nationalID "850718-2567890",
        name "김하늘",
        age "39"^^xsd:integer,
        belongsToHousehold TestHousehold_U,
        hasSpouse TestApplicant_U,
        personalIncome 5500000
```

```turtle
Individual: TestParent_U1
    Types: HouseholdMember, QualifiedDependent, ElderlyDependent
    Facts:
        nationalID "570320-1678901",
        name "이철호",
        age "67"^^xsd:integer,
        belongsToHousehold TestHousehold_U,
        hasChild TestApplicant_U,
        supportStartDate "2019-09-01"^^xsd:date
    Annotations:
        rdfs:label "신청자 U의 아버지 (이철호)"@ko,
        rdfs:comment "만 67세, 2019년 9월부터 부양 (5년 이상)"@ko
```

```turtle
Individual: TestAccount_U
    Types: SubscriptionAccount
    Facts:
        accountNumber "9012-3456-7890",
        accountOpeningDate "2019-06-01"^^xsd:date,
        depositAmount 12000000,
        monthlyPaymentCount 65
```

```turtle
Individual: TestIncome_U
    Types: Income
    Facts:
        monthlyAverageIncome 11000000
```

---

## 10. CQ 17 대응: 기관추천 특별공급 신청자 V

### 10.1 신청자 V (장애인 등록자)

```turtle
Individual: TestApplicant_V
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "880410-2678901",
        name "한미영",
        age "36"^^xsd:integer,
        maritalStatus "미혼",
        hasDisability true,
        livesIn Gyeonggi,
        belongsToHousehold TestHousehold_V,
        hasSubscriptionAccount TestAccount_V,
        appliesFor TestApp_Institutional_01,
        homelessStartDate "1988-04-10"^^xsd:date,
        isRecommendedBy LocalGovernment_Generic,
        recommendationDate "2024-10-15"^^xsd:date,
        recommendationNumber "2024-GG-0012345"
    Annotations:
        rdfs:label "신청자 V (한미영)"@ko,
        rdfs:comment "CQ 17 대응: 장애인 기관추천 특공"@ko
```

### 10.2 신청자 V의 세대

```turtle
Individual: TestHousehold_V
    Types: Household, SinglePersonHousehold_Defined
    Facts:
        hasMember TestApplicant_V,
        hasHead TestApplicant_V,
        hasIncome TestIncome_V
```

```turtle
Individual: TestAccount_V
    Types: SubscriptionAccount
    Facts:
        accountNumber "0123-4567-8901",
        accountOpeningDate "2023-08-01"^^xsd:date,
        depositAmount 1500000,
        monthlyPaymentCount 15
```

```turtle
Individual: TestIncome_V
    Types: Income
    Facts:
        monthlyAverageIncome 2800000
```

---

## 11. CQ 20 대응: 소득 기준 신청자 Y

### 11.1 신청자 Y (부부 합산 소득 800만원)

```turtle
Individual: TestApplicant_Y
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "900530-1789012",
        name "조민준",
        age "34"^^xsd:integer,
        maritalStatus "기혼",
        marriageRegistrationDate "2020-05-10"^^xsd:date,
        livesIn Seoul,
        belongsToHousehold TestHousehold_Y,
        hasSubscriptionAccount TestAccount_Y,
        appliesFor TestApp_Newlywed_02,
        homelessStartDate "2019-01-01"^^xsd:date
    Annotations:
        rdfs:label "신청자 Y (조민준)"@ko,
        rdfs:comment "CQ 20 대응: 신혼부부 특공, 소득 800만원"@ko
```

### 11.2 신청자 Y의 세대

```turtle
Individual: TestHousehold_Y
    Types: Household, DualIncomeHousehold_Defined
    Facts:
        hasMember TestApplicant_Y,
        hasMember TestSpouse_Y,
        hasHead TestApplicant_Y,
        hasIncome TestIncome_Y
    Annotations:
        rdfs:comment "맞벌이 가구 → 160% 기준 적용"@ko
```

```turtle
Individual: TestSpouse_Y
    Types: HouseholdMember
    Facts:
        nationalID "920715-2890123",
        name "임지현",
        age "32"^^xsd:integer,
        belongsToHousehold TestHousehold_Y,
        hasSpouse TestApplicant_Y,
        personalIncome 4200000
```

```turtle
Individual: TestAccount_Y
    Types: SubscriptionAccount
    Facts:
        accountNumber "1234-5678-9012",
        accountOpeningDate "2023-03-01"^^xsd:date,
        depositAmount 2500000,
        monthlyPaymentCount 20
```

```turtle
Individual: TestIncome_Y
    Types: Income
    Facts:
        monthlyAverageIncome 8000000
    Annotations:
        rdfs:comment "2인 가구 5,000만원의 160% = 8,000만원 → 정확히 기준선"@ko
```

---

## 12. CQ 21 대응: 자산 기준 신청자 Z

### 12.1 신청자 Z (토지 1억, 건물 2억, 차량 3천만원)

```turtle
Individual: TestApplicant_Z
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "880820-1901234",
        name "홍길동",
        age "36"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_Z,
        hasSubscriptionAccount TestAccount_Z,
        appliesFor TestApp_General_03,
        homelessStartDate "2020-01-01"^^xsd:date,
        ownsLand TestLand_Z1,
        ownsBuilding TestBuilding_Z1,
        ownsVehicle TestVehicle_Z1
    Annotations:
        rdfs:label "신청자 Z (홍길동)"@ko,
        rdfs:comment "CQ 21 대응: 자산 보유 기준 초과 여부 확인"@ko
```

### 12.2 신청자 Z의 자산

```turtle
Individual: TestLand_Z1
    Types: LandAsset
    Facts:
        landAssetValue 100000000
    Annotations:
        rdfs:comment "토지 1억원"@ko
```

```turtle
Individual: TestBuilding_Z1
    Types: BuildingAsset
    Facts:
        buildingAssetValue 200000000
    Annotations:
        rdfs:comment "건물 2억원"@ko
```

```turtle
Individual: TestVehicle_Z1
    Types: VehicleAsset
    Facts:
        vehicleAssetValue 30000000
    Annotations:
        rdfs:comment "자동차 3천만원"@ko
```

### 12.3 신청자 Z의 세대

```turtle
Individual: TestHousehold_Z
    Types: Household
    Facts:
        hasMember TestApplicant_Z,
        hasMember TestSpouse_Z,
        hasHead TestApplicant_Z,
        hasIncome TestIncome_Z,
        hasTotalAsset TestAsset_Z
```

```turtle
Individual: TestSpouse_Z
    Types: HouseholdMember
    Facts:
        nationalID "890915-2012345",
        name "김민지",
        age "35"^^xsd:integer,
        belongsToHousehold TestHousehold_Z,
        hasSpouse TestApplicant_Z,
        personalIncome 4500000
```

```turtle
Individual: TestAccount_Z
    Types: SubscriptionAccount
    Facts:
        accountNumber "2345-6789-0123",
        accountOpeningDate "2021-05-01"^^xsd:date,
        depositAmount 5000000,
        monthlyPaymentCount 42
```

```turtle
Individual: TestIncome_Z
    Types: Income
    Facts:
        monthlyAverageIncome 9200000
```

```turtle
Individual: TestAsset_Z
    Types: Asset
    Facts:
        realEstateAssetValue 300000000,
        vehicleAssetValue 30000000
    Annotations:
        rdfs:comment "부동산 3억 → 국민주택 기준 2.15억 초과, 차량 3천만원 → 기준 3,708만원 이하"@ko
```

---

## 13. CQ 24 대응: 육아휴직 중 배우자가 있는 신청자 W

### 13.1 신청자 W (배우자 육아휴직 중)

```turtle
Individual: TestApplicant_W
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "910705-1123456",
        name "신동욱",
        age "33"^^xsd:integer,
        maritalStatus "기혼",
        marriageRegistrationDate "2021-06-20"^^xsd:date,
        livesIn Seoul,
        belongsToHousehold TestHousehold_W,
        hasSubscriptionAccount TestAccount_W,
        appliesFor TestApp_Newlywed_01,
        homelessStartDate "2020-01-01"^^xsd:date,
        personalIncome 5000000,
        hasChild TestChild_W1
    Annotations:
        rdfs:label "신청자 W (신동욱)"@ko,
        rdfs:comment "CQ 24 대응: 배우자 육아휴직 중 소득 산정"@ko
```

### 13.2 배우자 (육아휴직 중)

```turtle
Individual: TestSpouse_W
    Types: HouseholdMember
    Facts:
        nationalID "920810-2234567",
        name "오수진",
        age "32"^^xsd:integer,
        belongsToHousehold TestHousehold_W,
        hasSpouse TestApplicant_W,
        isOnChildcareLeave true,
        childcareLeaveAllowance 1500000,
        personalIncome 1500000
    Annotations:
        rdfs:label "배우자 W (오수진)"@ko,
        rdfs:comment "육아휴직 급여 150만원 → 소득으로 산정"@ko
```

### 13.3 신청자 W의 세대

```turtle
Individual: TestHousehold_W
    Types: Household
    Facts:
        hasMember TestApplicant_W,
        hasMember TestSpouse_W,
        hasMember TestChild_W1,
        hasHead TestApplicant_W,
        hasIncome TestIncome_W
```

```turtle
Individual: TestChild_W1
    Types: Child, MinorChild, InfantChild
    Facts:
        nationalID "230415-3345678",
        name "신예린",
        age "1"^^xsd:integer,
        belongsToHousehold TestHousehold_W,
        hasParent TestApplicant_W,
        hasParent TestSpouse_W
```

```turtle
Individual: TestAccount_W
    Types: SubscriptionAccount
    Facts:
        accountNumber "3456-7890-1234",
        accountOpeningDate "2023-01-10"^^xsd:date,
        depositAmount 3000000,
        monthlyPaymentCount 22
```

```turtle
Individual: TestIncome_W
    Types: Income
    Facts:
        monthlyAverageIncome 6500000
    Annotations:
        rdfs:comment "신청자 500만원 + 배우자 육아휴직 급여 150만원 = 650만원"@ko
```

---

## 14. 추가 테스트 케이스: 재당첨 제한 신청자 H

### 14.1 신청자 H (10년 전 당첨 후 계약 포기)

```turtle
Individual: TestApplicant_H
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "820315-1234567",
        name "박지훈",
        age "42"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_H,
        hasSubscriptionAccount TestAccount_H,
        appliesFor TestApp_General_01,
        homelessStartDate "2010-01-01"^^xsd:date,
        hasWinningRecord TestWinningRecord_Old_01
    Annotations:
        rdfs:label "신청자 H (박지훈)"@ko,
        rdfs:comment "CQ 6 대응: 10년 전 당첨 포기, 재당첨 제한 만료"@ko
```

### 14.2 신청자 H의 세대

```turtle
Individual: TestHousehold_H
    Types: Household
    Facts:
        hasMember TestApplicant_H,
        hasMember TestSpouse_H,
        hasHead TestApplicant_H,
        hasIncome TestIncome_H
```

```turtle
Individual: TestSpouse_H
    Types: HouseholdMember
    Facts:
        nationalID "840525-2345678",
        name "정유진",
        age "40"^^xsd:integer,
        belongsToHousehold TestHousehold_H,
        hasSpouse TestApplicant_H,
        personalIncome 4800000
```

```turtle
Individual: TestAccount_H
    Types: SubscriptionAccount
    Facts:
        accountNumber "4567-8901-2345",
        accountOpeningDate "2018-03-01"^^xsd:date,
        depositAmount 8000000,
        monthlyPaymentCount 80
```

```turtle
Individual: TestIncome_H
    Types: Income
    Facts:
        monthlyAverageIncome 10500000
```

---

## 15. 추가 테스트 케이스: 세대원 신청자 P

### 15.1 신청자 P (1순위 요건 충족, 세대원)

```turtle
Individual: TestApplicant_P
    Types: Applicant, NonHeadOfHouseholdMember
    Facts:
        nationalID "920820-2456789",
        name "서지영",
        age "32"^^xsd:integer,
        maritalStatus "미혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_P,
        hasSubscriptionAccount TestAccount_P,
        appliesFor TestApp_General_03,
        homelessStartDate "1992-08-20"^^xsd:date
    Annotations:
        rdfs:label "신청자 P (서지영)"@ko,
        rdfs:comment "CQ 10 대응: 세대원 신분으로 국민주택 1순위 신청 불가"@ko
```

### 15.2 신청자 P의 세대 (부모와 함께 거주)

```turtle
Individual: TestHousehold_P
    Types: Household
    Facts:
        hasMember TestApplicant_P,
        hasMember TestParent_P1,
        hasHead TestParent_P1,
        hasIncome TestIncome_P
```

```turtle
Individual: TestParent_P1
    Types: HouseholdMember, HeadOfHousehold
    Facts:
        nationalID "650420-1567890",
        name "서대용",
        age "59"^^xsd:integer,
        belongsToHousehold TestHousehold_P,
        hasChild TestApplicant_P,
        personalIncome 6000000
```

```turtle
Individual: TestAccount_P
    Types: SubscriptionAccount
    Facts:
        accountNumber "5678-9012-3456",
        accountOpeningDate "2020-02-01"^^xsd:date,
        depositAmount 4000000,
        monthlyPaymentCount 56
```

```turtle
Individual: TestIncome_P
    Types: Income
    Facts:
        monthlyAverageIncome 9500000
```

---

## 16. 추가 테스트 케이스: 5년 이내 당첨 이력 있는 세대 신청자 Q

### 16.1 신청자 Q (본인은 무당첨, 배우자 3년 전 당첨)

```turtle
Individual: TestApplicant_Q
    Types: Applicant, HeadOfHousehold
    Facts:
        nationalID "870925-1678901",
        name "강민수",
        age "37"^^xsd:integer,
        maritalStatus "기혼",
        livesIn Seoul,
        belongsToHousehold TestHousehold_Q,
        hasSubscriptionAccount TestAccount_Q,
        appliesFor TestApp_General_01,
        homelessStartDate "2018-01-01"^^xsd:date
    Annotations:
        rdfs:label "신청자 Q (강민수)"@ko,
        rdfs:comment "CQ 11 대응: 배우자에 당첨 이력 있어 1순위 불가"@ko
```

### 16.2 신청자 Q의 배우자 (5년 이내 당첨)

```turtle
Individual: TestSpouse_Q
    Types: HouseholdMember
    Facts:
        nationalID "890610-2789012",
        name "이서윤",
        age "35"^^xsd:integer,
        belongsToHousehold TestHousehold_Q,
        hasSpouse TestApplicant_Q,
        hasWinningRecord TestWinningRecord_Recent_01,
        personalIncome 4500000
    Annotations:
        rdfs:comment "2021년 당첨 이력 보유 → 세대 전체 1순위 불가"@ko
```

### 16.3 신청자 Q의 세대

```turtle
Individual: TestHousehold_Q
    Types: Household, HouseholdWithRecentWinning
    Facts:
        hasMember TestApplicant_Q,
        hasMember TestSpouse_Q,
        hasHead TestApplicant_Q,
        hasIncome TestIncome_Q
    Annotations:
        rdfs:comment "최근 당첨 이력 있는 세대"@ko
```

```turtle
Individual: TestAccount_Q
    Types: SubscriptionAccount
    Facts:
        accountNumber "6789-0123-4567",
        accountOpeningDate "2019-07-01"^^xsd:date,
        depositAmount 7000000,
        monthlyPaymentCount 64
```

```turtle
Individual: TestIncome_Q
    Types: Income
    Facts:
        monthlyAverageIncome 9800000
```

---

## 17. 추가 청약 신청 Individual

```turtle
Individual: TestApp_General_03
    Types: GeneralSupply
    Facts:
        isForHousing TestHousing_Seoul_National_01,
        recruitmentAnnouncementDate "2024-11-15"^^xsd:date
    Annotations:
        rdfs:label "서울 강동 LH행복주택 일반공급"@ko
```

---

## 18. 신청자 및 관련 정보 통계

| 카테고리 | 개체 수 | 비고 |
|---------|--------|------|
| 신청자 (Applicant) | 15명 | A, F, G, H, K, L, P, Q, R, S, T, U, V, Y, Z, W |
| 세대 (Household) | 15개 | 각 신청자별 세대 |
| 배우자 (Spouse) | 12명 | 기혼 신청자의 배우자 |
| 자녀 (Child) | 6명 | 미성년 자녀 |
| 부모/부양가족 | 2명 | 노부모, 세대원의 부모 |
| 청약통장 | 15개 | 각 신청자별 청약통장 |
| 세대 소득 | 15개 | 각 세대별 소득 정보 |
| 자산 | 2개 | TestAsset_A, TestAsset_Z |
| 토지/건물/차량 | 3개 | 신청자 Z의 자산 상세 |
| **총합** | **85개** | |

---

## 19. CQ별 테스트 신청자 매핑

| CQ 번호 | 주제 | 테스트 신청자 | 비고 |
|---------|------|-------------|------|
| CQ 1 | 성년 자격 | TestApplicant_A | 만 31세 |
| CQ 2 | 청약통장 가입 기간 | TestApplicant_A | 2.5년 |
| CQ 3 | 무주택세대구성원 | TestApplicant_A | 세대주 + 배우자 + 자녀 |
| CQ 4 | 해당/기타 지역 | TestApplicant_F | 경기 거주, 서울 신청 |
| CQ 5 | 소형저가주택 처분 | TestApplicant_G | 배우자 처분 이력 |
| CQ 6 | 재당첨 제한 | TestApplicant_H | 10년 전 당첨 포기 |
| CQ 7 | 투기과열지구 1주택자 | TestApplicant_L | 과천 거주, 1주택 |
| CQ 10 | 세대원의 국민주택 1순위 | TestApplicant_P | 세대원 신분 |
| CQ 11 | 5년 이내 당첨 이력 | TestApplicant_Q | 배우자 당첨 이력 |
| CQ 12 | 예치금 부족 | TestApplicant_K | 50만원 부족 |
| CQ 13 | 신혼부부 특공 | TestApplicant_R | 결혼 5년, 자녀 1명 |
| CQ 14 | 생애최초 특공 | TestApplicant_S | 미혼 1인 가구 |
| CQ 15 | 다자녀가구 특공 | TestApplicant_T | 자녀 3명 |
| CQ 16 | 노부모부양 특공 | TestApplicant_U | 만 67세 아버지 부양 |
| CQ 17 | 기관추천 특공 | TestApplicant_V | 장애인 |
| CQ 20 | 소득 기준 | TestApplicant_Y | 소득 800만원 |
| CQ 21 | 자산 기준 | TestApplicant_Z | 부동산 3억 |
| CQ 24 | 육아휴직 소득 | TestApplicant_W | 배우자 육아휴직 |

---

## 20. 데이터 확장 방안

### 20.1 추가 가능한 신청자 유형
- 예비신혼부부 신청자
- 한부모가족 신청자 (실제 케이스)
- 국가유공자 기관추천 신청자
- 중소기업 근로자 기관추천 신청자
- 북한이탈주민 신청자
- 4인 이상 자녀가구 (다자녀가구)
- 태아 포함 다자녀가구

### 20.2 추가 가능한 시나리오
- 계약취소주택 신청 케이스
- 무순위 청약 신청 케이스
- 생애최초 특공 과거 소유 이력 있는 케이스 (자격 없음)
- 투기과열지구 2주택 이상 보유 케이스
- 예치금 초과 보유 케이스
- 소득 기준 초과 케이스

### 20.3 엣지 케이스
- 만 19세 정확히 일치하는 성년 (경계 케이스)
- 청약통장 가입 정확히 2년 (경계 케이스)
- 소득이 기준선에 정확히 일치하는 케이스
- 무주택 기간 정확히 15년 (가점 만점 경계)

---

**주의사항**: 
1. 본 문서의 모든 Individual은 테스트 및 검증 목적으로 작성된 가상 데이터입니다.
2. 주민등록번호는 모두 가상의 번호이며, 실제 개인정보가 아닙니다.
3. 금액 및 날짜는 2024년 11월 기준으로 작성되었습니다.
4. 실제 온톨로지 구현 시에는 개인정보 보호법을 준수하여 익명화된 데이터를 사용해야 합니다.

