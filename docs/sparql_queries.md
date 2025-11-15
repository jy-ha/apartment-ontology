# CQ 검증용 SPARQL 쿼리 예시 (SPARQL Queries for CQ Verification)

본 문서는 Competency Questions(CQ) 1-24번을 검증하기 위한 SPARQL 쿼리 예시를 제공합니다.

**작성일**: 2024년 11월  
**목적**: 테스트 데이터(`test_data.ttl`)를 사용한 CQ 검증  
**전제조건**: `core.ttl`, `primitive_classes.ttl`, `defined_classes.ttl`, `object_properties.ttl`, `data_properties.ttl`, `individuals.ttl`, `test_data.ttl`이 모두 로드되어 있어야 합니다.

---

## PREFIX 선언 (공통)

모든 쿼리에서 사용되는 공통 PREFIX:

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
```

---

## A. 기본 자격 및 개인 현황 (Basic & Personal Status)

### CQ 1: "신청자 A는 현재 만 31세이며 서울에 3년 거주했습니다. 청약 신청이 가능한 '성년'인가요?"

**목표**: 만 19세 이상 성년 자격 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?age ?region ?duration
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :age ?age ;
               :livesIn ?region ;
               :hasResidenceHistory ?resHistory .
    
    ?region :regionName ?regionName .
    ?resHistory :residenceDurationInYears ?duration .
    
    # 성년 조건: 만 19세 이상
    FILTER (?age >= 19)
    
    # 서울 거주 조건
    FILTER (?regionName = "서울")
    
    # 3년 이상 거주 조건
    FILTER (?duration >= 3.0)
}
```

**예상 결과**: TestApplicant_A (김철수, 31세, 서울 4.9년 거주)

**Defined Class 기반 쿼리** (추론 후):

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?age
WHERE {
    ?applicant a :Adult ;
               :name ?name ;
               :age ?age .
    
    # Adult는 Defined Class: Person and (age >= 19)
    
    FILTER (regex(STR(?applicant), "TestApplicant_A"))
}
```

---

### CQ 2: "신청자 A는 청약통장 가입 기간이 2.5년입니다. 1순위 청약에 필요한 가입 기간을 충족했나요?"

**목표**: 청약통장 2년 이상 가입 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?accountNumber ?openingDate 
       (STRDT(STR(ROUND(days(?currentDate - ?openingDate) / 365.25)), xsd:integer) AS ?yearsOwned)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasSubscriptionAccount ?account .
    
    ?account :accountNumber ?accountNumber ;
             :accountOpeningDate ?openingDate .
    
    # 현재 날짜 (2024-11-15 기준)
    BIND("2024-11-15"^^xsd:date AS ?currentDate)
    
    # 2년 전 날짜 계산 (SPARQL 1.1 표준)
    BIND(?currentDate - "P2Y"^^xsd:yearMonthDuration AS ?dateTwoYearsAgo)
    
    # 2년 이상 조건
    FILTER (?openingDate <= ?dateTwoYearsAgo)
    
    FILTER (regex(STR(?applicant), "TestApplicant_A"))
}
```

**예상 결과**: TestApplicant_A, 2022-05-10 개설, 약 2.5년

---

### CQ 3: "신청자 A의 세대는 세대주, 배우자, 미성년 자녀로 구성됩니다. 이들은 '무주택세대구성원'으로 간주되나요?"

**목표**: 세대원 전원이 주택을 소유하지 않았는지 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?household (COUNT(?member) AS ?memberCount) (COUNT(?housing) AS ?housingCount)
WHERE {
    ?applicant a :Applicant ;
               :belongsToHousehold ?household .
    
    ?household :hasMember ?member .
    
    OPTIONAL {
        ?member :owns ?housing .
    }
    
    FILTER (regex(STR(?applicant), "TestApplicant_A"))
}
GROUP BY ?applicant ?household
HAVING (?housingCount = 0)
```

**예상 결과**: TestApplicant_A의 세대는 주택 소유 0건 → 무주택세대구성원

**Defined Class 기반 쿼리** (추론 후):

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name
WHERE {
    ?applicant a :HomelessHouseholdMember ;
               :name ?name .
    
    # HomelessHouseholdMember는 Defined Class
    
    FILTER (regex(STR(?applicant), "TestApplicant_A"))
}
```

---

### CQ 4: "청약 신청자 F는 경기도에 거주하고 있습니다. 서울에 위치한 아파트에 청약할 수 있는 '해당 지역' 또는 '기타 지역' 자격은 무엇인가요?"

**목표**: RelevantRegionApplicant vs OtherRegionApplicant 판단

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?applicantRegion ?housingRegion 
       (IF(?applicantRegion = ?housingRegion, "해당 지역", "기타 지역") AS ?status)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :livesIn ?applicantRegionInd ;
               :appliesFor ?application .
    
    ?applicantRegionInd :regionName ?applicantRegion .
    
    ?application :isForHousing ?housing .
    ?housing :isLocatedIn ?housingRegionInd .
    ?housingRegionInd :regionName ?housingRegion .
    
    # 수도권 확인
    ?applicantRegionInd a :MetropolitanArea .
    ?housingRegionInd a :MetropolitanArea .
    
    FILTER (regex(STR(?applicant), "TestApplicant_F"))
}
```

**예상 결과**: TestApplicant_F, 경기 거주 → 서울 신청 = "기타 지역" (수도권 내이므로 청약 가능)

---

### CQ 5: "배우자 G가 3년 전 소형·저가주택을 1채 소유했다가 처분했습니다. 이 경우 '무주택 기간'은 언제부터 산정되나요?"

**목표**: 소형·저가주택 처분일 = 무주택 기간 시작일

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?spouse ?housing ?area ?price ?endDate
WHERE {
    ?applicant a :Applicant ;
               :belongsToHousehold ?household .
    
    ?household :hasMember ?spouse .
    ?spouse :hasOwnershipHistory ?ownershipHistory ;
            :hasSpouse ?applicant .
    
    ?ownershipHistory :ownedHousing ?housing ;
                      :ownershipEndDate ?endDate .
    
    ?housing :area ?area ;
             :price ?price ;
             :isLocatedIn ?region .
    
    ?region a :MetropolitanArea .
    
    # 소형·저가주택 조건: 60㎡ 이하, 1.3억 이하, 수도권
    FILTER (?area <= 60.0 && ?price <= 130000000)
    
    FILTER (regex(STR(?applicant), "TestApplicant_G"))
}
```

**예상 결과**: 배우자 한지민, 2021-05-15 처분 → 무주택 기간 시작일

**Defined Class 활용** (추론 후):

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?housing ?endDate
WHERE {
    ?housing a :SmallLowPriceHousing_Defined ;
             :disposalDate ?endDate .
    
    # SmallLowPriceHousing_Defined는 추론기가 자동 분류
}
```

---

### CQ 6: "신청자 H는 10년 전 청약에 당첨되었으나 계약을 포기했습니다. '재당첨 제한' 기간에 해당되나요?"

**목표**: 5년 재당첨 제한 기간 만료 여부 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?winningDate ?restrictionYears
       (STRDT(STR(ROUND(days(?currentDate - ?winningDate) / 365.25)), xsd:integer) AS ?yearsSince)
       (IF(?yearsSince > ?restrictionYears, "제한 만료", "제한 중") AS ?status)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasWinningRecord ?winningRecord .
    
    ?winningRecord :winningDate ?winningDate ;
                   :restrictionPeriodInYears ?restrictionYears ;
                   :isSubjectToRestriction true .
    
    BIND("2024-11-15"^^xsd:date AS ?currentDate)
    # N년 전 날짜 계산 (기간이 변수이므로 문자열 결합 후 캐스팅)
    BIND(xsd:dateTime(concat(xsd:string(year(?currentDate) - ?restrictionYears), "-", str-after(xsd:string(?currentDate), "-"))) AS ?restrictionDate)
    
    # 재당첨 제한 만료 여부 확인
    FILTER (?winningDate <= ?restrictionDate)

}
```

**예상 결과**: TestApplicant_H, 2014년 당첨, 10년 경과 → "제한 만료"

---

## B. 일반공급 자격 (General Supply)

### CQ 7: "경기도 과천(투기과열지구) 거주자 L은 1주택자입니다. '민영주택 1순위(추첨제)'에 신청할 수 있나요?"

**목표**: 투기과열지구에서 1주택자의 1순위 자격 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?region ?isOverheated (COUNT(?housing) AS ?housingCount)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :livesIn ?regionInd ;
               :belongsToHousehold ?household .
    
    ?regionInd :regionName ?region ;
               :isSpeculativeOverheatedZone ?isOverheated .
    
    ?household :hasMember ?member .
    
    OPTIONAL {
        ?member :owns ?housing .
    }
    
    FILTER (regex(STR(?applicant), "TestApplicant_L"))
}
GROUP BY ?applicant ?name ?region ?isOverheated
```

**예상 결과**: TestApplicant_L, 과천(투기과열지구), 1주택 → 조건부 1순위 (기존 주택 처분 조건)

**규제지역 Defined Class 활용**:

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?region
WHERE {
    ?applicant a :Applicant ;
               :livesIn ?region .
    
    ?region a :SpeculativeOverheatedZone_Defined .
    
    # 추론기가 isSpeculativeOverheatedZone=true인 Region을 자동 분류
    
    FILTER (regex(STR(?applicant), "TestApplicant_L"))
}
```

---

### CQ 10: "신청자 P는 1순위 요건을 모두 갖추었으나 세대원입니다. '국민주택 1순위'에 청약할 수 있나요?"

**목표**: 국민주택 1순위는 세대주만 가능

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name 
       (IF(EXISTS { ?applicant a :HeadOfHousehold }, "세대주", "세대원") AS ?status)
WHERE {
    ?applicant a :Applicant ;
               :name ?name .
    
    FILTER (regex(STR(?applicant), "TestApplicant_P"))
}
```

**예상 결과**: TestApplicant_P, "세대원" → 국민주택 1순위 불가

---

### CQ 11: "신청자 Q의 세대는 과거 5년 이내에 다른 주택에 당첨된 사실이 있습니다. Q는 '1순위' 자격이 유지되나요?"

**목표**: 세대원 중 5년 이내 당첨 이력 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name (COUNT(?recentWinning) AS ?recentWinningCount)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :belongsToHousehold ?household .
    
    ?household :hasMember ?member .
    
    OPTIONAL {
        ?member :hasWinningRecord ?winningRecord .
        ?winningRecord :winningDate ?winningDate ;
                       :isSubjectToRestriction true .
        
        BIND("2024-11-15"^^xsd:date AS ?currentDate)

        # 5년 전 날짜 계산
        BIND(?currentDate - "P5Y"^^xsd:yearMonthDuration AS ?dateFiveYearsAgo)
        
        FILTER (?winningDate > ?dateFiveYearsAgo)
        BIND(?winningRecord AS ?recentWinning)
    }
    
    FILTER (regex(STR(?applicant), "TestApplicant_Q"))
}
GROUP BY ?applicant ?name
```

**예상 결과**: TestApplicant_Q, 배우자에 2021년 당첨 이력 → 1순위 불가

---

### CQ 12: "신청자 K는 경기도에 거주하며 서울 소재 85㎡ 이하 주택에 청약하려 합니다. 청약통장 예치금이 250만원일 때, 추가로 얼마를 더 예치해야 하나요?"

**목표**: 예치금 부족액 계산

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?currentDeposit ?requiredDeposit 
       (?requiredDeposit - ?currentDeposit AS ?shortage)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasSubscriptionAccount ?account ;
               :appliesFor ?application .
    
    ?account :depositAmount ?currentDeposit .
    
    ?application :isForHousing ?housing .
    ?housing :isLocatedIn ?region ;
             :area ?area .
    
    ?depositReq a :DepositRequirement ;
                :appliesInRegion ?region ;
                :minArea ?minArea ;
                :maxArea ?maxArea ;
                :requiredDepositAmount ?requiredDeposit .
    
    FILTER (?area >= ?minArea && ?area < ?maxArea)
    FILTER (?currentDeposit < ?requiredDeposit)
    FILTER (regex(STR(?applicant), "TestApplicant_K"))
}
```

**예상 결과**: TestApplicant_K, 현재 250만원, 필요 300만원 → 부족 50만원

---

## C. 특별공급 자격 (Special Supply)

### CQ 13: "결혼 5년 차, 만 2세 자녀 1명, 소득 기준을 충족한 부부 R은 '신혼부부 특별공급' 대상인가요?"

**목표**: 신혼부부 특공 자격 확인 (혼인 7년 이내, 자녀 있음, 무주택)

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?marriageDate ?childAge ?income
       (STRDT(STR(ROUND(days(?currentDate - ?marriageDate) / 365.25)), xsd:integer) AS ?marriageYears)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :marriageRegistrationDate ?marriageDate ;
               :hasChild ?child ;
               :belongsToHousehold ?household .
    
    ?child :age ?childAge .
    ?household :hasIncome ?incomeObj .
    ?incomeObj :monthlyAverageIncome ?income .
    
    BIND("2024-11-15"^^xsd:date AS ?currentDate)

    # 7년 전 날짜 계산
    BIND(?currentDate - "P7Y"^^xsd:yearMonthDuration AS ?dateSevenYearsAgo)
    
    # 신혼부부 조건: 혼인신고일이 7년 전 날짜 이후여야 함
    FILTER (?marriageDate > ?dateSevenYearsAgo)
    
    FILTER (regex(STR(?applicant), "TestApplicant_R"))
}
```

**예상 결과**: TestApplicant_R, 2019년 결혼(5년차), 자녀 만 2세, 소득 800만원 → 자격 충족

---

### CQ 14: "신청자 S는 만 35세 미혼 1인 가구입니다. '생애최초 특별공급'에 지원할 수 있나요?"

**목표**: 생애최초 특공 자격 (무주택, 소득세 5년 이상)

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?maritalStatus (COUNT(?taxHistory) AS ?taxYears)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :maritalStatus ?maritalStatus ;
               :hasTaxPaymentHistory ?taxHistory .
    
    # 주택 소유 이력 없음 확인
    FILTER NOT EXISTS { ?applicant :hasOwnershipHistory ?ownership }
    
    FILTER (regex(STR(?applicant), "TestApplicant_S"))
}
GROUP BY ?applicant ?name ?maritalStatus
HAVING (?taxYears >= 5)
```

**예상 결과**: TestApplicant_S, 미혼 1인 가구, 소득세 5년 이상 → 자격 충족

---

### CQ 15: "신청자 T는 만 18세, 만 10세, 만 5세의 세 자녀를 두고 있습니다. '다자녀가구 특별공급'의 자녀 수 요건을 충족하나요?"

**목표**: 미성년 자녀 3명 이상 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name (COUNT(?child) AS ?childCount)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasChild ?child .
    
    ?child :age ?age .
    
    # 만 19세 미만 자녀
    FILTER (?age < 19)
    
    FILTER (regex(STR(?applicant), "TestApplicant_T"))
}
GROUP BY ?applicant ?name
HAVING (?childCount >= 3)
```

**예상 결과**: TestApplicant_T, 자녀 3명(18세, 10세, 5세) → 요건 충족

---

### CQ 16: "신청자 U는 만 67세의 아버지를 5년째 부양하고 있습니다. '노부모부양 특별공급' 자격이 되나요?"

**목표**: 만 65세 이상 부양 3년 이상 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?parentAge ?supportStartDate
       (STRDT(STR(ROUND(days(?currentDate - ?supportStartDate) / 365.25)), xsd:integer) AS ?supportYears)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasElderlyDependent ?parent .
    
    ?parent :age ?parentAge ;
            :supportStartDate ?supportStartDate .
    
    BIND("2024-11-15"^^xsd:date AS ?currentDate)

    # 3년 전 날짜 계산
    BIND(?currentDate - "P3Y"^^xsd:yearMonthDuration AS ?dateThreeYearsAgo)

    # 만 65세 이상, 3년 이상 부양 조건
    FILTER (?parentAge >= 65)
    FILTER (?supportStartDate <= ?dateThreeYearsAgo)
    
    FILTER (regex(STR(?applicant), "TestApplicant_U"))
}
```

**예상 결과**: TestApplicant_U, 아버지 만 67세, 2019년부터 부양(5년) → 자격 충족

---

### CQ 17: "장애인으로 등록된 V는 '기관추천 특별공급' 대상이 되기 위해 어떤 절차를 거쳐야 하나요?"

**목표**: 기관 추천 여부 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?hasDisability ?institution ?recommendationDate
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :hasDisability ?hasDisability ;
               :isRecommendedBy ?institution ;
               :recommendationDate ?recommendationDate .
    
    ?institution rdfs:label ?institutionLabel .
    
    FILTER (regex(STR(?applicant), "TestApplicant_V"))
}
```

**예상 결과**: TestApplicant_V, 장애인, 지방자치단체 추천, 2024-10-15 → 절차 완료

---

## D. 소득 및 자산 기준 (Income & Asset)

### CQ 20: "신청자 Y의 부부 합산 월평균 소득이 800만원입니다. '신혼부부 특별공급(민영주택)'의 소득 기준을 충족하나요?"

**목표**: 맞벌이 가구 160% 기준 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?householdSize ?income ?standardIncome 
       (ROUND(?standardIncome * 1.6) AS ?threshold160)
       (IF(?income <= ?standardIncome * 1.6, "충족", "초과") AS ?status)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :belongsToHousehold ?household .
    
    ?household :hasIncome ?incomeObj ;
               :hasMember ?member .
    ?incomeObj :monthlyAverageIncome ?income .
    
    # 가구원 수 계산
    {
        SELECT ?household (COUNT(?m) AS ?householdSize)
        WHERE {
            ?household :hasMember ?m .
        }
        GROUP BY ?household
    }
    
    # 도시근로자 소득 기준 조회
    ?standard a :UrbanWorkerStandardIncome ;
              :yearOfStandard 2024 ;
              :householdSize ?householdSize ;
              :standardAmount ?standardIncome .
    
    # 맞벌이 확인 (두 세대원 모두 소득 있음)
    ?household :hasMember ?m1 , ?m2 .
    ?m1 :personalIncome ?income1 .
    ?m2 :personalIncome ?income2 .
    ?m1 :hasSpouse ?m2 .
    FILTER (?income1 > 0 && ?income2 > 0)
    
    FILTER (regex(STR(?applicant), "TestApplicant_Y"))
}
```

**예상 결과**: TestApplicant_Y, 2인 가구, 소득 800만원, 기준 500만원 × 160% = 800만원 → "충족" (정확히 기준선)

---

### CQ 21: "신청자 Z의 세대는 토지 1억원, 건물 2억원, 자동차 3천만원을 보유 중입니다. '국민주택 1순위'의 자산 기준을 초과하나요?"

**목표**: 자산 기준 확인 (부동산 2.15억 이하, 차량 3,708만원 이하)

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name 
       (SUM(?landValue) AS ?totalLand)
       (SUM(?buildingValue) AS ?totalBuilding)
       ((?totalLand + ?totalBuilding) AS ?totalRealEstate)
       (SUM(?vehicleValue) AS ?totalVehicle)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :belongsToHousehold ?household .
    
    ?household :hasMember ?member .
    
    OPTIONAL {
        ?member :ownsLand ?land .
        ?land :landAssetValue ?landValue .
    }
    
    OPTIONAL {
        ?member :ownsBuilding ?building .
        ?building :buildingAssetValue ?buildingValue .
    }
    
    OPTIONAL {
        ?member :ownsVehicle ?vehicle .
        ?vehicle :vehicleAssetValue ?vehicleValue .
    }
    
    FILTER (regex(STR(?applicant), "TestApplicant_Z"))
}
GROUP BY ?applicant ?name
HAVING (?totalRealEstate > 215000000 || ?totalVehicle > 37080000)
```

**예상 결과**: TestApplicant_Z, 부동산 3억원(초과), 차량 3천만원(기준 내) → 자산 기준 초과

---

### CQ 22: "'생애최초 특별공급'에서 '도시근로자 가구당 월평균 소득'의 130%는 구체적으로 얼마인가요?"

**목표**: 소득 기준 계산

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?householdSize ?standardAmount 
       (ROUND(?standardAmount * 1.3) AS ?threshold130pct)
WHERE {
    ?standard a :UrbanWorkerStandardIncome ;
              :yearOfStandard 2024 ;
              :householdSize ?householdSize ;
              :standardAmount ?standardAmount .
}
ORDER BY ?householdSize
```

**예상 결과**:
- 1인: 300만원 × 130% = 390만원
- 2인: 500만원 × 130% = 650만원
- 3인: 540만원 × 130% = 702만원
- 4인: 620만원 × 130% = 806만원
- 5인: 670만원 × 130% = 871만원
- 6인: 720만원 × 130% = 936만원

---

### CQ 23: "1인 가구 A는 '생애최초 특별공급' 신청 시 소득 기준이 2인 가구와 동일하게 적용되나요?"

**목표**: 1인 가구 특례 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name 
       (COUNT(?member) AS ?actualSize)
       ?applicableSize ?standardAmount
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :belongsToHousehold ?household ;
               :appliesFor ?application .
    
    ?application a :FirstTimeHomeBuyerSupply .
    
    ?household :hasMember ?member .
    
    # 1인 가구 → 2인 가구 기준 적용
    BIND(IF((COUNT(?member) = 1), 2, COUNT(?member)) AS ?applicableSize)
    
    ?standard a :UrbanWorkerStandardIncome ;
              :yearOfStandard 2024 ;
              :householdSize ?applicableSize ;
              :standardAmount ?standardAmount .
    
    FILTER (regex(STR(?applicant), "TestApplicant_S"))
}
GROUP BY ?applicant ?name ?applicableSize ?standardAmount
```

**예상 결과**: TestApplicant_S, 실제 1인 가구 → 2인 가구 기준(500만원) 적용

---

### CQ 24: "소득 산정 시, 배우자가 육아휴직 중인 경우 소득은 어떻게 계산되나요?"

**목표**: 육아휴직 급여 소득 포함 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?applicant ?name ?applicantIncome ?spouseIncome 
       ?isOnLeave ?leaveAllowance ?totalIncome
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :personalIncome ?applicantIncome ;
               :belongsToHousehold ?household .
    
    ?household :hasMember ?spouse ;
               :hasIncome ?incomeObj .
    ?incomeObj :monthlyAverageIncome ?totalIncome .
    
    ?spouse :hasSpouse ?applicant ;
            :isOnChildcareLeave ?isOnLeave ;
            :childcareLeaveAllowance ?leaveAllowance ;
            :personalIncome ?spouseIncome .
    
    FILTER (regex(STR(?applicant), "TestApplicant_W"))
}
```

**예상 결과**: TestApplicant_W, 신청자 500만원, 배우자 육아휴직 급여 150만원 → 총 650만원

---

## E. 복합 쿼리 (Complex Queries)

### 복합 CQ 1: "신청자 A의 완전한 청약 자격 프로필 조회"

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?name ?age ?region ?accountYears ?deposit ?income 
       (IF(?age >= 19, "성년", "미성년") AS ?ageStatus)
       (IF(?accountYears >= 2, "충족", "미달") AS ?accountStatus)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :age ?age ;
               :livesIn ?regionInd ;
               :hasSubscriptionAccount ?account ;
               :belongsToHousehold ?household .
    
    ?regionInd :regionName ?region .
    
    ?account :accountOpeningDate ?openingDate ;
             :depositAmount ?deposit .
    
    ?household :hasIncome ?incomeObj .
    ?incomeObj :monthlyAverageIncome ?income .
    
    BIND("2024-11-15"^^xsd:date AS ?currentDate)
    BIND((?currentDate - ?openingDate) / 365 AS ?accountYears)
    
    FILTER (regex(STR(?applicant), "TestApplicant_A"))
}
```

---

### 복합 CQ 2: "모든 신청자의 자격 등급 분류"

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?name 
       (IF(?age >= 19, "성년", "미성년") AS ?ageCheck)
       (IF(?accountYears >= 2, "청약통장 충족", "청약통장 미달") AS ?accountCheck)
       (IF(?housingCount = 0, "무주택", "유주택") AS ?housingCheck)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :age ?age ;
               :hasSubscriptionAccount ?account ;
               :belongsToHousehold ?household .
    
    ?account :accountOpeningDate ?openingDate .
    
    ?household :hasMember ?member .
    
    OPTIONAL {
        ?member :owns ?housing .
    }
    
    BIND("2024-11-15"^^xsd:date AS ?currentDate)
    BIND((?currentDate - ?openingDate) / 365 AS ?accountYears)
    
    {
        SELECT ?household (COUNT(?h) AS ?housingCount)
        WHERE {
            ?household :hasMember ?m .
            OPTIONAL { ?m :owns ?h . }
        }
        GROUP BY ?household
    }
}
ORDER BY ?name
```

---

### 복합 CQ 3: "특별공급 대상자 자동 매칭"

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?name 
       (IF(?hasChild && ?marriageYears <= 7, "신혼부부", "") AS ?newlywed)
       (IF(?taxYears >= 5 && ?housingCount = 0, "생애최초", "") AS ?firstTime)
       (IF(?childCount >= 3, "다자녀", "") AS ?multiChild)
       (IF(?elderlyCount >= 1, "노부모부양", "") AS ?agedParents)
WHERE {
    ?applicant a :Applicant ;
               :name ?name ;
               :belongsToHousehold ?household .
    
    OPTIONAL {
        ?applicant :marriageRegistrationDate ?marriageDate .
        BIND("2024-11-15"^^xsd:date AS ?currentDate)
        BIND((?currentDate - ?marriageDate) / 365 AS ?marriageYears)
    }
    
    OPTIONAL {
        ?applicant :hasChild ?child .
        BIND(true AS ?hasChild)
    }
    
    OPTIONAL {
        SELECT ?applicant (COUNT(?tax) AS ?taxYears)
        WHERE {
            ?applicant :hasTaxPaymentHistory ?tax .
        }
        GROUP BY ?applicant
    }
    
    OPTIONAL {
        SELECT ?applicant (COUNT(?c) AS ?childCount)
        WHERE {
            ?applicant :hasChild ?c .
            ?c :age ?age .
            FILTER (?age < 19)
        }
        GROUP BY ?applicant
    }
    
    OPTIONAL {
        SELECT ?applicant (COUNT(?e) AS ?elderlyCount)
        WHERE {
            ?applicant :hasElderlyDependent ?e .
        }
        GROUP BY ?applicant
    }
    
    OPTIONAL {
        SELECT ?household (COUNT(?h) AS ?housingCount)
        WHERE {
            ?household :hasMember ?m .
            OPTIONAL { ?m :owns ?h . }
        }
        GROUP BY ?household
    }
}
ORDER BY ?name
```

---

## F. 추론 검증 쿼리 (Reasoning Verification Queries)

### 추론 1: Defined Class 자동 분류 확인

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?individual ?class
WHERE {
    {
        ?individual a :Adult .
        BIND("Adult" AS ?class)
    } UNION {
        ?individual a :SmallLowPriceHousing_Defined .
        BIND("SmallLowPriceHousing_Defined" AS ?class)
    } UNION {
        ?individual a :SpeculativeOverheatedZone_Defined .
        BIND("SpeculativeOverheatedZone_Defined" AS ?class)
    } UNION {
        ?individual a :HomelessHouseholdMember .
        BIND("HomelessHouseholdMember" AS ?class)
    }
    
    FILTER (regex(STR(?individual), "Test"))
}
ORDER BY ?class ?individual
```

**기대 결과**: 추론 후 자동 분류된 개체들 표시

---

### 추론 2: 대칭 속성 검증 (hasSpouse)

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT ?person1 ?person2
WHERE {
    ?person1 :hasSpouse ?person2 .
    ?person2 :hasSpouse ?person1 .
    
    FILTER (regex(STR(?person1), "Test"))
}
```

**기대 결과**: 모든 배우자 관계가 양방향으로 추론됨

---

## G. 성능 테스트 쿼리 (Performance Test Queries)

### 성능 1: 전체 신청자 통계

```sparql
PREFIX : <http://www.example.org/apartment-subscription-ontology#>

SELECT (COUNT(DISTINCT ?applicant) AS ?totalApplicants)
       (COUNT(DISTINCT ?household) AS ?totalHouseholds)
       (COUNT(DISTINCT ?housing) AS ?totalHousings)
       (COUNT(DISTINCT ?application) AS ?totalApplications)
WHERE {
    ?applicant a :Applicant .
    OPTIONAL { ?applicant :belongsToHousehold ?household . }
    OPTIONAL { ?application :isForHousing ?housing . }
    OPTIONAL { ?applicant :appliesFor ?application . }
}
```

---

## H. 사용 가이드

### 쿼리 실행 환경

1. **Apache Jena Fuseki** (추천)
   ```bash
   fuseki-server --file=merged_ontology.ttl /apartment-subscription
   ```

2. **Protégé SPARQL Query Plugin**
   - File → Open → merged_ontology.ttl 로드
   - Window → Tabs → SPARQL Query

3. **RDFLib (Python)**
   ```python
   from rdflib import Graph
   
   g = Graph()
   g.parse("merged_ontology.ttl", format="turtle")
   g.parse("test_data.ttl", format="turtle")
   
   results = g.query("""
       PREFIX : <http://www.example.org/apartment-subscription-ontology#>
       SELECT ?applicant ?name
       WHERE {
           ?applicant a :Applicant ;
                      :name ?name .
       }
   """)
   
   for row in results:
       print(f"{row.applicant}: {row.name}")
   ```

### 추론 활성화

추론기를 활성화하여 Defined Class 자동 분류:

```bash
# Jena 추론
riot --validate merged_ontology.ttl test_data.ttl > combined.ttl
```

---

## 참고 자료

- **온톨로지 파일**: `ttl/` 디렉토리
- **테스트 데이터**: `ttl/test_data.ttl`
- **CQ 문서**: `docs/cq.md`
- **CQ 검증 문서**: `docs/cq_verification.md`
- **DL Query 문서**: `docs/cq_dl_queries.md`

---

**작성자**: Ontology Development Team  
**최종 수정**: 2024년 11월 15일

