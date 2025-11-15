# 아파트 청약 자격 온톨로지 SWRL 규칙 (SWRL Rules)

본 문서는 아파트 청약 자격 온톨로지에서 사용되는 SWRL(Semantic Web Rule Language) 규칙들을 정의합니다. 이 규칙들은 OWL만으로 표현하기 어려운 계산, 집계, 조건부 로직을 구현합니다.

---

## 1. 소득 기준 관련 규칙

### 규칙 1: 육아휴직 급여 소득 산정

**목적**: 육아휴직 중인 세대원의 육아휴직 급여를 개인 소득으로 산정

**CQ 대응**: CQ 24

```swrl
Person(?p) ∧ isOnChildcareLeave(?p, true) ∧ childcareLeaveAllowance(?p, ?allowance)
→ personalIncome(?p, ?allowance)
```

**설명**: 육아휴직 중인 사람의 육아휴직 급여는 소득으로 인정되어 세대 총소득 계산에 포함됩니다.

---

### 규칙 2: 세대 총 소득 합산 (2인 가구)

**목적**: 세대원 2명의 개인 소득을 합산하여 세대 월평균 소득 산출

```swrl
Household(?h) ∧ hasMember(?h, ?m1) ∧ hasMember(?h, ?m2) ∧
differentFrom(?m1, ?m2) ∧
personalIncome(?m1, ?inc1) ∧ personalIncome(?m2, ?inc2) ∧
swrlb:add(?total, ?inc1, ?inc2)
→ monthlyAverageIncome(?h, ?total)
```

**설명**: 부부 가구 등 2인 세대의 경우 두 사람의 소득을 합산합니다.

**확장**: 3인 이상 가구는 재귀적 합산 또는 별도 집계 규칙 필요

---

### 규칙 3: 맞벌이 가구 판정

**목적**: 부부가 모두 소득이 있는 경우 맞벌이 가구로 분류

```swrl
Household(?h) ∧
hasMember(?h, ?p1) ∧ hasMember(?h, ?p2) ∧
hasSpouse(?p1, ?p2) ∧
personalIncome(?p1, ?inc1) ∧ personalIncome(?p2, ?inc2) ∧
swrlb:greaterThan(?inc1, 0) ∧ swrlb:greaterThan(?inc2, 0)
→ DualIncomeHousehold(?h)
```

**설명**: 신혼부부 특별공급에서 소득 기준 160% 적용을 위해 사용됩니다.

---

### 규칙 4: 가구원 수 계산

**목적**: 세대의 구성원 수를 계산하여 적절한 도시근로자 소득 기준 선택

```swrl
Household(?h) ∧ hasMember(?h, ?m) ∧
count(?m) = ?size
→ householdSize(?h, ?size)
```

**설명**: SWRL의 집계 함수 `count`를 사용하여 세대원 수를 계산합니다.

**참고**: SWRL 구현에 따라 집계 함수 문법이 다를 수 있으므로 추론 엔진별 조정 필요

---

### 규칙 5: 소득 기준 충족 여부 판단

**목적**: 신청자의 세대 소득이 특정 소득 기준선 이하인지 판단

**CQ 대응**: CQ 20, 22

```swrl
Applicant(?a) ∧ belongsToHousehold(?a, ?h) ∧
monthlyAverageIncome(?h, ?income) ∧
householdSize(?h, ?size) ∧
UrbanWorkerStandardIncome(?std) ∧
yearOfStandard(?std, 2024) ∧
householdSize(?std, ?size) ∧
standardAmount(?std, ?baseAmount) ∧
IncomeThreshold(?threshold) ∧
basedOnStandard(?threshold, ?std) ∧
incomePercentage(?threshold, ?pct) ∧
swrlb:multiply(?limit, ?baseAmount, ?pct) ∧
swrlb:divide(?limit, ?limit, 100) ∧
swrlb:lessThanOrEqual(?income, ?limit)
→ meetsIncomeThreshold(?a, ?threshold)
```

**설명**:
1. 신청자의 세대 월평균 소득과 가구원 수를 확인
2. 해당 가구원 수의 2024년 도시근로자 소득 기준 조회
3. 적용할 소득 기준선(100%, 130%, 140%, 160%)의 비율 확인
4. 기준 금액 × 비율 / 100 = 소득 한도 계산
5. 세대 소득이 소득 한도 이하이면 기준 충족

---

### 규칙 6: 1인 가구 소득 기준 특례

**목적**: 생애최초 특공에서 1인 가구는 2인 가구 소득 기준 적용

**CQ 대응**: CQ 23

```swrl
Applicant(?a) ∧ belongsToHousehold(?a, ?h) ∧
SinglePersonHousehold(?h) ∧
appliesFor(?a, ?app) ∧
FirstTimeHomeBuyerSupply(?app) ∧
UrbanWorkerStandardIncome(?std2) ∧
householdSize(?std2, 2) ∧
yearOfStandard(?std2, 2024)
→ applicableStandardIncome(?a, ?std2)
```

**설명**: 1인 가구 신청자의 생애최초 특공 신청 시 2인 가구 도시근로자 소득 기준을 적용합니다.

---

## 2. 자산 기준 관련 규칙

### 규칙 7: 세대 총 부동산 자산 합산

**목적**: 세대원 전체의 토지 및 건물 자산 가액을 합산

```swrl
Household(?h) ∧ hasMember(?h, ?m) ∧
ownsLand(?m, ?land) ∧ landAssetValue(?land, ?landValue) ∧
ownsBuilding(?m, ?building) ∧ buildingAssetValue(?building, ?buildingValue) ∧
swrlb:add(?totalRealEstate, ?landValue, ?buildingValue)
→ householdTotalRealEstateValue(?h, ?totalRealEstate)
```

**설명**: 모든 세대원의 토지 및 건물 자산을 합산하여 세대 총 부동산 가액을 산출합니다.

**참고**: 여러 세대원의 자산을 모두 합산하려면 집계 함수 또는 반복 적용 필요

---

### 규칙 8: 세대 총 자동차 자산 합산

**목적**: 세대원 전체의 자동차 자산 가액을 합산

```swrl
Household(?h) ∧ hasMember(?h, ?m) ∧
ownsVehicle(?m, ?vehicle) ∧ vehicleAssetValue(?vehicle, ?vv) ∧
sum(?vv) = ?totalVehicle  # 집계 함수
→ householdTotalVehicleValue(?h, ?totalVehicle)
```

**설명**: 모든 세대원의 자동차 자산을 합산하여 세대 총 차량 가액을 산출합니다.

---

### 규칙 9: 국민주택 자산 기준 충족 여부

**목적**: 세대의 부동산 및 자동차 자산이 국민주택 기준 이하인지 판단

**CQ 대응**: CQ 21

```swrl
Household(?h) ∧
householdTotalRealEstateValue(?h, ?re) ∧
householdTotalVehicleValue(?h, ?vv) ∧
NationalHousing_AssetThreshold_2024(assetThreshold) ∧
maxRealEstateValue(assetThreshold, 215000000) ∧
maxVehicleValue(assetThreshold, 37080000) ∧
swrlb:lessThanOrEqual(?re, 215000000) ∧
swrlb:lessThanOrEqual(?vv, 37080000)
→ meetsNationalHousingAssetLimit(?h, true)
```

**설명**:
- 부동산 가액 2억 1,500만원 이하
- 자동차 가액 3,708만원 이하
- 두 조건을 모두 충족해야 국민주택 자산 기준 통과

---

## 3. 청약통장 관련 규칙

### 규칙 10: 청약통장 가입 기간 계산 (년 단위)

**목적**: 청약통장 개설일로부터 현재까지의 기간을 년 단위로 계산

```swrl
Applicant(?a) ∧ hasSubscriptionAccount(?a, ?acc) ∧
accountOpeningDate(?acc, ?openDate) ∧
swrlb:date(?currentDate, xsd:date()) ∧
swrlb:subtractDates(?days, ?currentDate, ?openDate) ∧
swrlb:divide(?years, ?days, 365)
→ accountPeriodInYears(?a, ?years)
```

**설명**: 
- 현재 날짜 - 개설일 = 일수
- 일수 / 365 = 년 단위 기간

**참고**: 윤년 처리는 단순화를 위해 365일 고정

---

### 규칙 11: 청약통장 가입 기간 요건 충족 (2년 이상)

**목적**: 1순위 청약에 필요한 2년 가입 기간 충족 여부 판단

**CQ 대응**: CQ 2

```swrl
Applicant(?a) ∧ accountPeriodInYears(?a, ?years) ∧
swrlb:greaterThanOrEqual(?years, 2)
→ meetsAccountPeriodRequirement(?a, true)
```

**설명**: 청약통장 가입 기간이 2년(24개월) 이상이면 요건 충족

---

### 규칙 12: 예치금 부족분 계산

**목적**: 신청자의 현재 예치금과 필요 예치금의 차액 산출

**CQ 대응**: CQ 28

```swrl
Applicant(?a) ∧ appliesFor(?a, ?app) ∧ isForHousing(?app, ?housing) ∧
isLocatedIn(?housing, ?region) ∧ area(?housing, ?area) ∧
hasSubscriptionAccount(?a, ?acc) ∧ depositAmount(?acc, ?currentDeposit) ∧
DepositRequirement(?req) ∧ appliesInRegion(?req, ?region) ∧
minArea(?req, ?minA) ∧ maxArea(?req, ?maxA) ∧
swrlb:greaterThanOrEqual(?area, ?minA) ∧ swrlb:lessThan(?area, ?maxA) ∧
requiredDepositAmount(?req, ?required) ∧
swrlb:lessThan(?currentDeposit, ?required) ∧
swrlb:subtract(?shortage, ?required, ?currentDeposit)
→ hasDepositShortage(?a, ?shortage)
```

**설명**:
1. 신청 주택의 지역 및 면적 확인
2. 해당 지역 및 면적 구간의 필요 예치금 조회
3. 현재 예치금 < 필요 예치금이면 부족분 계산
4. 부족분 = 필요 예치금 - 현재 예치금

---

## 4. 무주택 및 주택 소유 관련 규칙

### 규칙 13: 소형·저가주택 처분 후 무주택 기간 산정

**목적**: 소형·저가주택을 처분한 날짜를 무주택 기간 시작일로 설정

**CQ 대응**: CQ 5

**설계 변경**: `SmallLowPriceHousing`과 `DisposedSmallLowPriceHousing`은 Defined Class로 변경되었으므로, 규칙에서 조건을 직접 확인합니다.

```swrl
Person(?p) ∧ hasOwnershipHistory(?p, ?hist) ∧
ownedHousing(?hist, ?housing) ∧ 
area(?housing, ?a) ∧ swrlb:lessThanOrEqual(?a, 60.0) ∧
price(?housing, ?pr) ∧ swrlb:lessThanOrEqual(?pr, 130000000) ∧
isLocatedIn(?housing, ?region) ∧ MetropolitanArea(?region) ∧
ownershipEndDate(?hist, ?endDate)
→ homelessStartDate(?p, ?endDate)
```

**대안 (Defined Class 사용)**:
```swrl
Person(?p) ∧ hasOwnershipHistory(?p, ?hist) ∧
ownedHousing(?hist, ?housing) ∧ SmallLowPriceHousing_Defined(?housing) ∧
ownershipEndDate(?hist, ?endDate)
→ homelessStartDate(?p, ?endDate)
```

**설명**: 
- 소형·저가주택(면적 60㎡ 이하, 가격 1억3천만원 이하, 수도권 소재)은 무주택 기간 산정 시 예외 처리
- 처분일부터 무주택으로 간주
- `SmallLowPriceHousing_Defined`는 이제 Defined Class이므로 추론기가 자동으로 분류함

---

### 규칙 14: 무주택 기간 계산 (년 단위)

**목적**: 무주택 시작일로부터 현재까지의 기간을 년 단위로 계산

```swrl
Applicant(?a) ∧ homelessStartDate(?a, ?startDate) ∧
swrlb:date(?currentDate, xsd:date()) ∧
swrlb:subtractDates(?days, ?currentDate, ?startDate) ∧
swrlb:divide(?years, ?days, 365)
→ homelessPeriodInYears(?a, ?years)
```

**설명**: (현재 날짜 - 무주택 시작일) / 365 = 무주택 기간(년)

---

## 5. 재당첨 제한 관련 규칙

### 규칙 15: 5년 이내 당첨 이력 확인

**목적**: 세대원 중 5년 이내 청약 당첨 이력이 있는지 확인

**CQ 대응**: CQ 6, 11

```swrl
WinningRecord(?wr) ∧ winningDate(?wr, ?date) ∧
swrlb:date(?currentDate, xsd:date()) ∧
swrlb:subtractDates(?days, ?currentDate, ?date) ∧
swrlb:divide(?years, ?days, 365) ∧
swrlb:lessThanOrEqual(?years, 5) ∧
isSubjectToRestriction(?wr, true)
→ ActiveRestrictionPeriod(?wr)
```

**설명**:
- 당첨일로부터 5년 이내이고
- 재당첨 제한 대상인 경우
- 현재 제한 기간 중으로 판정

---

### 규칙 16: 세대 내 제한 기간 중 당첨자 확인

**목적**: 세대원 중 한 명이라도 제한 기간 중이면 세대 전체 1순위 자격 상실

```swrl
Household(?h) ∧ hasMember(?h, ?m) ∧
hasWinningRecord(?m, ?wr) ∧ ActiveRestrictionPeriod(?wr)
→ HouseholdWithRecentWinning(?h)
```

**설명**: 5년 이내 당첨 이력이 있는 세대원이 있으면 세대 전체가 1순위 신청 불가

---

## 6. 자녀 및 부양가족 관련 규칙

### 규칙 17: 태아 포함 미성년 자녀 수 계산

**목적**: 만 19세 미만 자녀 수 + 태아 수 = 총 자녀 수 산정

**CQ 대응**: CQ 15

```swrl
Person(?p) ∧ hasChild(?p, ?child) ∧ age(?child, ?age) ∧
swrlb:lessThan(?age, 19) ∧
count(?child) = ?childCount ∧
fetusCount(?p, ?fetusCount) ∧
swrlb:add(?total, ?childCount, ?fetusCount)
→ totalMinorChildCount(?p, ?total)
```

**설명**: 다자녀가구 특별공급 자격 판단 시 임신 중인 태아도 자녀 수에 포함

---

### 규칙 18: 인정 부양가족 수 계산

**목적**: 만 65세 이상 또는 만 19세 미만 세대원 수 계산

```swrl
Applicant(?a) ∧ hasDependent(?a, ?dep) ∧
QualifiedDependent(?dep) ∧
count(?dep) = ?depCount
→ dependentCount(?a, ?depCount)
```

**설명**: 가점제에서 부양가족 수에 따른 가점 산정에 사용 (본 온톨로지는 가점 제외)

---

## 7. 생애최초 특공 관련 규칙

### 규칙 19: 소득세 납부 통산 기간 계산

**목적**: 신청자의 과거 소득세 납부 연도 수를 합산

```swrl
Applicant(?a) ∧ hasTaxPaymentHistory(?a, ?hist) ∧
taxYear(?hist, ?year) ∧
count(distinct ?year) = ?years
→ taxPaymentDuration(?a, ?years)
```

**설명**: 생애최초 특별공급은 5년 이상 소득세 납부 이력 필요

---

### 규칙 20: 생애최초 자격 판정 (세대원 전원 무소유)

**목적**: 신청자 본인 및 세대원 전원이 단 한 번도 주택을 소유한 적이 없는지 확인

**CQ 대응**: CQ 19

```swrl
Applicant(?a) ∧ NeverOwnedHousing(?a) ∧
belongsToHousehold(?a, ?h) ∧
forall ?m (hasMember(?h, ?m) → NeverOwnedHousing(?m))
→ FirstTimeHomeBuyer_Qualified(?a)
```

**설명**:
- 본인이 주택 소유 이력이 없고
- 모든 세대원도 주택 소유 이력이 없어야 함
- 과거 소유 후 처분한 경우도 자격 없음

**참고**: SWRL의 `forall` 표현은 일부 엔진에서 지원 안 될 수 있으므로, 부정 로직으로 전환 필요:

```swrl
# 대안: 소유 이력 있는 세대원이 없으면 자격 있음
Applicant(?a) ∧ NeverOwnedHousing(?a) ∧
belongsToHousehold(?a, ?h) ∧
not exists ?m (hasMember(?h, ?m) ∧ EverOwnedHousing(?m))
→ FirstTimeHomeBuyer_Qualified(?a)
```

---

## 8. 규칙 적용 순서 및 의존성

### 8.1 계산 규칙 (먼저 실행)

1. **기간 계산**: 규칙 10, 14 (청약통장 가입 기간, 무주택 기간)
2. **집계 계산**: 규칙 2, 4, 7, 8, 17, 18 (소득 합산, 가구원 수, 자산 합산, 자녀 수)
3. **개인 소득**: 규칙 1 (육아휴직 급여)

### 8.2 판정 규칙 (계산 후 실행)

4. **자격 판정**: 규칙 3, 5, 6, 9, 11, 15, 16, 19, 20
5. **부족분 계산**: 규칙 12, 13

---

## 9. SWRL 구현 시 주의사항

### 9.1 날짜 연산

- SWRL built-in 함수 `swrlb:subtractDates`는 표준이 아니며, Pellet, HermiT 등 추론기에 따라 지원 여부가 다름
- 대안: 외부 Java/Python 함수를 SWRL에 연결하거나, SPARQL 쿼리로 대체

### 9.2 집계 함수

- `count`, `sum` 등 집계 함수는 SWRL 1.0 표준에 없음
- SQWRL(Semantic Query-enhanced Web Rule Language) 확장 사용 필요
- 또는 SPARQL 1.1 집계 기능 활용

### 9.3 추론 성능

- SWRL 규칙이 많아질수록 추론 시간 증가
- 규칙 간 의존성이 복잡하면 무한 루프 위험
- 규칙 최적화: 불필요한 변수 최소화, 조건 순서 조정

### 9.4 대안: SPARQL + 애플리케이션 로직

복잡한 계산 및 집계는 SWRL보다 다음 방식이 더 효율적일 수 있음:
1. SPARQL로 기본 데이터 조회
2. Python/Java 애플리케이션에서 계산 수행
3. 결과를 온톨로지에 다시 저장

---

## 10. 규칙 테스트 케이스

### 테스트 1: 육아휴직 급여 소득 산정 (규칙 1)

**입력**:
```
Person: TestPerson_A
    isOnChildcareLeave: true
    childcareLeaveAllowance: 1500000
```

**기대 출력**:
```
TestPerson_A personalIncome 1500000
```

---

### 테스트 2: 예치금 부족분 계산 (규칙 12)

**입력**:
```
Applicant: TestApplicant_B
    appliesFor: TestApp_1
    hasSubscriptionAccount: TestAccount_1

TestApp_1:
    isForHousing: TestHousing_1

TestHousing_1:
    isLocatedIn: Seoul
    area: 80.0

TestAccount_1:
    depositAmount: 2500000

Seoul_Deposit_Under85:
    requiredDepositAmount: 3000000
```

**기대 출력**:
```
TestApplicant_B hasDepositShortage 500000
```

---

### 테스트 3: 소득 기준 충족 (규칙 5)

**입력**:
```
Applicant: TestApplicant_C
    belongsToHousehold: TestHousehold_1

TestHousehold_1:
    monthlyAverageIncome: 7000000
    householdSize: 4

UrbanWorker_2024_4person:
    standardAmount: 6200000

FirstTimeHomeBuyer_Income_130pct:
    incomePercentage: 130
    basedOnStandard: UrbanWorker_2024_4person
```

**계산**:
- 소득 한도 = 6,200,000 × 130 / 100 = 8,060,000
- 세대 소득 7,000,000 < 8,060,000 → 충족

**기대 출력**:
```
TestApplicant_C meetsIncomeThreshold FirstTimeHomeBuyer_Income_130pct
```

---

## 11. 규칙 통계 요약

| 카테고리 | 규칙 수 | 주요 기능 |
|---------|--------|----------|
| 소득 관련 | 6개 | 소득 합산, 기준 충족 판단, 맞벌이 판정 |
| 자산 관련 | 3개 | 자산 합산, 기준 충족 판단 |
| 청약통장 관련 | 3개 | 가입 기간 계산, 예치금 부족분 산정 |
| 무주택 관련 | 2개 | 무주택 기간 계산, 소형저가주택 예외 |
| 재당첨 제한 | 2개 | 당첨 이력 확인, 제한 기간 판정 |
| 자녀/부양가족 | 2개 | 자녀 수 계산, 부양가족 수 계산 |
| 생애최초 | 2개 | 소득세 납부 기간, 무소유 자격 판정 |
| **총합** | **20개** | **자격 판단 핵심 로직** |
