# 아파트 청약 자격 온톨로지 정의 클래스 (Defined Classes)

본 문서는 원시 클래스(Primitive Class)와 속성(Property)을 이용하여 청약 자격 요건과 같은 복잡한 개념을 논리적으로 정의하는 정의 클래스(Defined Class)를 기술합니다. 각 정의 클래스는 특정 자격 조건을 충족하는 개인들의 집합을 나타내며, Manchester-like 구문을 사용하여 필요충분조건(Equivalent To)을 명시합니다.

## 1. 기본 자격 관련 정의 클래스

### `Adult` (성년)
- **설명**: 청약 신청의 기본 요건인 만 19세 이상 성년을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Person` and (`age` some xsd:integer[>= 19])

### `HomelessHouseholdMember` (무주택세대구성원)
- **설명**: 세대주를 포함한 세대원 전원이 주택을 소유하지 않은 세대의 구성원을 정의합니다. 소형·저가주택 소유는 예외적으로 무주택으로 간주될 수 있습니다.
- **논리 정의 (Equivalent To)**:
    - `HouseholdMember` that `belongsToHousehold` some (`Household` that not (`hasMember` some (`Person` that `owns` some (`Housing` that not `SmallLowPriceHousing`))))

### `HeadOfHomelessHousehold` (무주택세대주)
- **설명**: 무주택세대구성원이면서 세대주인 사람을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `HeadOfHousehold` and `HomelessHouseholdMember`

### `RelevantRegionApplicant` (해당 지역 거주 신청자)
- **설명**: 신청하는 주택의 건설 지역과 동일한 지역에 거주하는 신청자를 정의합니다. 이는 우선공급 자격을 판단하는 데 사용됩니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` that `livesIn` some (`Region` as r1) and `appliesFor` some (`SubscriptionApplication` that `isForHousing` some (`Housing` that `isLocatedIn` some (`Region` as r2 where r1 = r2)))

### `OtherRegionApplicant` (기타 지역 거주 신청자)
- **설명**: 신청하는 주택의 건설 지역과 다른 지역에 거주하지만 수도권 내에 거주하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and not `RelevantRegionApplicant` and `livesIn` some `MetropolitanArea`

### `MetropolitanAreaResident` (수도권 거주자)
- **설명**: 서울, 경기, 인천 중 한 곳에 거주하는 사람을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Person` and `livesIn` some `MetropolitanArea`

### `LongTermResident` (장기 거주자)
- **설명**: 특정 지역에 3년 이상 거주한 사람을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Person` and `hasResidenceHistory` some (`ResidenceHistory` and (`residenceDurationInYears` some xsd:float[>= 3.0]))

### `NeverOwnedHousing` (주택 소유 이력 없음)
- **설명**: 본인이 과거에 단 한 번도 주택을 소유한 적이 없는 사람을 정의합니다. 생애최초 특공의 핵심 요건입니다.
- **논리 정의 (Equivalent To)**:
    - `Person` and not (`hasOwnershipHistory` some `HousingOwnershipHistory`)

### `EverOwnedHousing` (주택 소유 이력 있음)
- **설명**: 본인이 과거에 주택을 소유한 적이 있는 사람을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Person` and (`hasOwnershipHistory` some `HousingOwnershipHistory`)

### `QualifiedDependent_Defined` (인정 부양가족 - 정의)
- **설명**: 가점제에서 부양가족으로 인정되는 세대구성원을 정의합니다. 만 65세 이상이거나 만 19세 미만이어야 합니다.
- **논리 정의 (Equivalent To)**:
    - `HouseholdMember` and ((`age` some xsd:integer[>= 65]) or (`age` some xsd:integer[< 19]) or (`hasDisability` value true))

### `MinorChild` (미성년 자녀)
- **설명**: 만 19세 미만의 자녀를 정의합니다. 다자녀가구 특별공급 자격 판단에 사용됩니다.
- **논리 정의 (Equivalent To)**:
    - `Child` and (`age` some xsd:integer[< 19])

### `InfantChild` (영유아 자녀)
- **설명**: 만 6세 이하의 자녀를 정의합니다. 신혼부부 특별공급 우선공급 자격 판단에 사용됩니다.
- **논리 정의 (Equivalent To)**:
    - `Child` and (`age` some xsd:integer[<= 6])

### `ElderlyDependent` (고령 부양가족)
- **설명**: 만 65세 이상의 부양가족을 정의합니다. 노부모부양 특별공급 및 가점제에 사용됩니다.
- **논리 정의 (Equivalent To)**:
    - `QualifiedDependent` and (`age` some xsd:integer[>= 65])

### `MinorDependent` (미성년 부양가족)
- **설명**: 만 19세 미만의 부양가족을 정의합니다. 가점제에 사용됩니다.
- **논리 정의 (Equivalent To)**:
    - `QualifiedDependent` and (`age` some xsd:integer[< 19])

### `AdoptedChild` (입양 자녀)
- **설명**: 입양한 자녀를 정의합니다. 자녀 수 산정에 포함됩니다.
- **논리 정의 (Equivalent To)**:
    - `Child` and (`isAdoptedChild` value true)

## 2. 일반공급 자격 관련 정의 클래스

### `FirstPriorityApplicant_NationalHousing` (국민주택 1순위 청약자)
- **설명**: 국민주택 일반공급 1순위 자격 요건을 모두 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HeadOfHomelessHousehold` and
    - `livesIn` some (`Region` that (`isSpeculativeOverheatedZone` value true)) and
    - `hasSubscriptionAccount` some (
        `SubscriptionAccount` and
        (`accountOpeningDate` calculation (currentDate - `accountOpeningDate`) >= 2 years) and
        (`monthlyPaymentCount` value >= 24)
    ) and
    - not (`belongsToHousehold` some (`Household` that `hasMember` some (`Person` that `hasWinningRecord` some (`WinningRecord` that (`winningDate` calculation (currentDate - `winningDate`) <= 5 years))))) and
    - `belongsToHousehold` some (`Household` that (`hasIncome` some (`Income` that meets_income_criteria_for_national_housing)) and (`hasTotalAsset` some (`Asset` that meets_asset_criteria_for_national_housing)))

### `FirstPriorityApplicant_PrivateHousing` (민영주택 1순위 청약자)
- **설명**: 민영주택 일반공급 1순위 자격 요건을 모두 충족하는 신청자를 정의합니다. (투기과열지구 기준)
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `Adult` and `HeadOfHousehold` and
    - (`HomelessHouseholdMember` or (`belongsToHousehold` some (`Household` that (`hasMember` exactly 1 (`Person` that `owns` some `Housing`))))) and
    - `livesIn` some (`Region` that (`isSpeculativeOverheatedZone` value true)) and
    - `hasSubscriptionAccount` some (
        `SubscriptionAccount` and
        (`accountOpeningDate` calculation (currentDate - `accountOpeningDate`) >= 2 years) and
        (`depositAmount` meets_deposit_criteria_for_region_and_area)
    ) and
    - not (`belongsToHousehold` some (`Household` that `hasMember` some (`Person` that `hasWinningRecord` some (`WinningRecord` that (`winningDate` calculation (currentDate - `winningDate`) <= 5 years)))))
- **주석 (rdfs:comment)**: "투기과열지구에서 1주택자가 1순위 신청 시, 계약 전까지 기존 주택을 처분해야 함 (조건부 자격). 이는 계약 시점의 절차적 요건으로, 온톨로지에서는 현재 소유 상태만을 기준으로 자격을 판단함."

### `SecondPriorityApplicant_PrivateHousing` (민영주택 2순위 청약자)
- **설명**: 민영주택 1순위 자격 요건을 충족하지 못했지만, 청약통장을 보유한 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `Adult` and
    - not `FirstPriorityApplicant_PrivateHousing` and
    - `hasSubscriptionAccount` some `SubscriptionAccount`

### `UnrankedSubscriptionApplicant` (무순위 청약 신청자)
- **설명**: 규제지역의 무순위(사후접수) 청약에 신청 가능한 자를 정의합니다. 청약통장 보유 여부와 무관합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `Adult` and `HomelessHouseholdMember` and `RelevantRegionApplicant`

## 3. 특별공급 자격 관련 정의 클래스

**특별공급 중복 신청 제한 (rdfs:comment on SpecialSupply)**: "한 신청자는 하나의 입주자 모집공고당 하나의 특별공급 유형만 선택하여 신청할 수 있음. 여러 특별공급 자격을 동시에 충족하더라도 중복 신청은 불가함. 이는 절차적 제약으로, 온톨로지에서는 각 자격 충족 여부만을 독립적으로 판단함."

### `NewlywedSpecialSupplyApplicant` (신혼부부 특별공급 청약자)
- **설명**: 신혼부부 또는 한부모가족으로서 특별공급 자격 요건을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HomelessHouseholdMember` and
    - ((`maritalStatus` value "기혼") and (`marriageDate` calculation (currentDate - `marriageDate`) <= 7 years)) or
    - ((`isSingleParent` value true) and (`hasChild` some (`Person` that `age` some xsd:integer[<= 6]))) and
    - `hasSubscriptionAccount` some (
        `SubscriptionAccount` and
        (`accountOpeningDate` calculation (currentDate - `accountOpeningDate`) >= 6 months)
    ) and
    - `belongsToHousehold` some (`Household` that (`hasIncome` some (`Income` that meets_income_criteria_for_newlyweds)))

### `FirstTimeHomeBuyerSpecialSupplyApplicant` (생애최초 특별공급 청약자)
- **설명**: 생애최초 주택 구매 특별공급 자격 요건을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HeadOfHomelessHousehold` and
    - `FirstPriorityApplicant_PrivateHousing` and
    - (`taxPaymentDuration` value >= 5) and
    - ((`maritalStatus` value "기혼") or (`hasChild` some `Person`) or (`belongsToHousehold` some (`Household` that `hasMember` exactly 1 `Person`))) and
    - `belongsToHousehold` some (`Household` that (`hasIncome` some (`Income` that meets_income_criteria_for_first_time_homebuyer))) and
    - not (`belongsToHousehold` some (`Household` that `hasMember` some (`Person` that ever (`owns` some `Housing`))))

### `MultiChildSpecialSupplyApplicant` (다자녀가구 특별공급 청약자)
- **설명**: 만 19세 미만의 자녀를 3명 이상 둔(태아 포함) 무주택세대구성원으로서 특별공급 자격 요건을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HomelessHouseholdMember` and
    - (`hasChild` min 3 (`Person` that `age` < 19)) or (A rule to sum children count and `fetusCount`) and
    - `hasSubscriptionAccount` some (`SubscriptionAccount` and (`accountOpeningDate` calculation (currentDate - `accountOpeningDate`) >= 6 months))

### `SupportingAgedParentsSpecialSupplyApplicant` (노부모부양 특별공급 청약자)
- **설명**: 만 65세 이상 직계존속(무주택자여야 함)을 3년 이상 부양하고 있는 무주택 세대주로서 특별공급 자격 요건을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HeadOfHomelessHousehold` and `FirstPriorityApplicant_PrivateHousing` and
    - `hasDependent` some (
        `Person` that 
        (`age` >= 65) and 
        (`supportStartDate` calculation (currentDate - `supportStartDate`) >= 3 years) and
        (not (`owns` some `Housing`)) and
        (not (`hasSpouse` some (`Person` that `owns` some `Housing`)))
    )

### `InstitutionalRecommendationSpecialSupplyApplicant` (기관추천 특별공급 청약자)
- **설명**: 국가기관 등의 추천을 받은 자로서 특별공급 자격 요건을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `HomelessHouseholdMember` and
    - `isRecommendedBy` some `Institution` and
    - `hasSubscriptionAccount` some (`SubscriptionAccount` and (`accountOpeningDate` calculation (currentDate - `accountOpeningDate`) >= 6 months))

### `NewlywedPrioritySupplyApplicant` (신혼부부 우선공급 청약자)
- **설명**: 신혼부부 특공 중 만 6세 이하 자녀가 있거나 소득 기준 100% 이하인 우선공급 대상자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `NewlywedSpecialSupplyApplicant` and
    - (`hasInfantChild` some (`Person` and (`age` some xsd:integer[<= 6])) or
     `belongsToHousehold` some (`Household` and `hasIncome` some (`Income` that meets_100_percent_income_criteria)))

### `ProspectiveNewlywedApplicant` (예비신혼부부 신청자)
- **설명**: 입주 전까지 혼인신고를 약속한 예비신혼부부 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and
    - `maritalStatus` value "미혼" and
    - `hasFianceCommitment` value true and
    - `expectedMarriageDate` some xsd:date

### `SingleParentFamilyApplicant` (한부모가족 신청자)
- **설명**: 만 6세 이하 자녀를 둔 한부모가족으로 신혼부부 특공에 준하여 신청 가능한 자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and
    - `isSingleParent` value true and
    - `hasInfantChild` some (`Person` and (`age` some xsd:integer[<= 6]))

### `FirstTimeHomeBuyer_Qualified` (생애최초 자격자)
- **설명**: 생애최초 특공의 핵심 요건인 '본인 및 세대원 전원이 주택 소유 이력 없음'을 충족하는 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and `NeverOwnedHousing` and
    - `belongsToHousehold` some (`Household` that (`hasMember` only `NeverOwnedHousing`))

### `ElderlyParentSupporter` (노부모 부양자)
- **설명**: 만 65세 이상 부모를 부양하는 청약 신청자를 정의합니다. 부양 기간과 무관하게 추론됩니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and
    - `hasElderlyDependent` some `ElderlyDependent`

### `SupportingAgedParentsApplicant` (노부모부양 특별공급 신청자)
- **설명**: 노부모부양 특별공급 자격 요건을 충족하는 신청자를 정의합니다. 만 65세 이상 부모를 부양하는 무주택 세대주입니다.
- **논리 정의 (Equivalent To)**:
    - `ElderlyParentSupporter` and `HeadOfHomelessHousehold`
- **주의사항**: 부양 기간(3년 이상)은 시간 계산이 필요하므로 OWL Defined Class로 표현할 수 없습니다. SPARQL 쿼리 또는 애플리케이션 로직에서 별도로 확인해야 합니다.
- **관련 Individual**: `AgedParentsSupport_Requirement_2024` (최소 부양 기간 3년, 최소 부모 나이 65세 정의)

## 5. 소득 및 자산 기준 관련 정의 클래스

### `WithinNationalHousingIncomeLimit` (국민주택 소득 기준 충족)
- **설명**: 국민주택 청약에 필요한 소득 기준(도시근로자 가구당 월평균 소득 100% 이하)을 충족하는 세대를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Household` and `hasIncome` some (`Income` that satisfies_national_housing_income_criteria)
- **SWRL 규칙 예시**:
```swrl
Household(?h), hasIncome(?h, ?inc), monthlyAverageIncome(?inc, ?amt),
Household(?h), hasMember(?h, ?m1), ... (가구원 수 계산),
UrbanWorkerStandardIncome(?std), yearOfStandard(?std, 2024), 
householdSize(?std, ?size), standardAmount(?std, ?base),
swrlb:lessThanOrEqual(?amt, ?base)
-> satisfies_national_housing_income_criteria(?inc, true)
```

### `WithinNationalHousingAssetLimit` (국민주택 자산 기준 충족)
- **설명**: 국민주택 청약에 필요한 자산 기준(부동산 2.15억 이하, 자동차 3,708만원 이하)을 충족하는 세대를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Household` and `hasTotalAsset` some (
        `Asset` that (total_real_estate_value <= 215000000) and
        (total_vehicle_value <= 37080000))
- **SWRL 규칙 예시**:
```swrl
Household(?h), hasMember(?m), ownsLand(?m, ?land), landAssetValue(?land, ?lv),
ownsBuilding(?m, ?building), buildingAssetValue(?building, ?bv),
swrlb:add(?re, ?lv, ?bv), swrlb:lessThanOrEqual(?re, 215000000),
ownsVehicle(?m, ?vehicle), vehicleAssetValue(?vehicle, ?vv),
swrlb:lessThanOrEqual(?vv, 37080000)
-> satisfies_national_housing_asset_criteria(?h, true)
```

### `DualIncomeHousehold_Defined` (맞벌이 가구 - 정의)
- **설명**: 부부가 모두 소득이 있는 가구를 정의합니다. 신혼부부 특공에서 소득 기준이 160%로 완화됩니다.
- **논리 정의 (Equivalent To)**:
    - `Household` and
    - `hasMember` some (`Person` and `hasSpouse` some `Person` and `personalIncome` some xsd:integer[> 0]) and
    - `hasMember` some (`Person` and `personalIncome` some xsd:integer[> 0] and `hasSpouse` some (`Person` and `personalIncome` some xsd:integer[> 0]))

### `SinglePersonHousehold_Defined` (1인 가구 - 정의)
- **설명**: 구성원이 1명인 가구를 정의합니다. 생애최초 특공에서 특별한 소득 기준이 적용됩니다.
- **논리 정의 (Equivalent To)**:
    - `Household` and (`hasMember` exactly 1 `HouseholdMember`)

## 6. 가점 및 점수 관련 정의 클래스

### `HighPointApplicant` (고득점 신청자)
- **설명**: 청약 가점이 60점 이상인 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and (`totalSubscriptionPoints` some xsd:integer[>= 60])

### `MaxHomelessPeriodPoints` (무주택 기간 만점)
- **설명**: 무주택 기간이 15년 이상으로 만점(32점)을 받은 신청자를 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Applicant` and (`homelessPeriodInYears` some xsd:integer[>= 15]) and (`homelessPeriodPoints` value 32)

## 7. 주택 특성 관련 정의 클래스

### `SmallSizeHousing_Defined` (소형주택 - 정의)
- **설명**: 전용면적 85㎡ 이하 주택을 정의합니다. 투기과열지구에서 100% 가점제가 적용됩니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and (`area` some xsd:float[<= 85.0])

### `MediumSizeHousing_Defined` (중형주택 - 정의)
- **설명**: 전용면적 85㎡ 초과 102㎡ 이하 주택을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and (`area` some xsd:float[> 85.0 and <= 102.0])

### `LargeSizeHousing_Defined` (대형주택 - 정의)
- **설명**: 전용면적 102㎡ 초과 주택을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and (`area` some xsd:float[> 102.0])

### `SmallLowPriceHousing_Defined` (소형·저가주택 - 정의)
- **설명**: 면적 60㎡ 이하, 가격 1억3천만원 이하, 수도권 소재 주택을 정의합니다. 무주택 기간 산정 시 예외로 처리됩니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and 
    - (`area` some xsd:float[<= 60.0]) and
    - (`price` some xsd:integer[<= 130000000]) and
    - (`isLocatedIn` some `MetropolitanArea`)

### `FullPointSelectionHousing` (전액 가점제 주택)
- **설명**: 100% 가점제로 당첨자를 선정하는 주택을 정의합니다. 투기과열지구의 85㎡ 이하 주택이 해당됩니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and
    - `SmallSizeHousing_Defined` and
    - `isLocatedIn` some (`Region` and (`isSpeculativeOverheatedZone` value true)) and
    - `usesSelectionMethod` some (`PointBasedSelection` and (`selectionRatio` value 1.0))

### `MixedSelectionHousing` (혼합 선정 주택)
- **설명**: 가점제와 추첨제를 혼합하여 당첨자를 선정하는 주택을 정의합니다. 투기과열지구의 85㎡ 초과 주택이 해당됩니다.
- **논리 정의 (Equivalent To)**:
    - `Housing` and
    - not `SmallSizeHousing_Defined` and
    - `isLocatedIn` some (`Region` and (`isSpeculativeOverheatedZone` value true)) and
    - `usesSelectionMethod` some (`PointBasedSelection` and (`selectionRatio` value 0.5)) and
    - `usesSelectionMethod` some (`LotteryBasedSelection` and (`selectionRatio` value 0.5))

## 7.1 규제지역 관련 정의 클래스

### `SpeculativeOverheatedZone_Defined` (투기과열지구 - 정의)
- **설명**: 투기 우려가 큰 지역으로 지정되어 가장 엄격한 청약 자격이 적용되는 지역을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Region` and (`isSpeculativeOverheatedZone` value true)
- **참고**: 이전에 Primitive Class로 정의되었으나, `isSpeculativeOverheatedZone` boolean 속성으로 명확히 정의 가능하므로 Defined Class로 변경되었습니다.
- **관련 CQ**: CQ 7
- **법적 근거**: 주택법 제63조의2

### `SubscriptionOverheatedArea_Defined` (청약과열지역 - 정의)
- **설명**: 청약 경쟁이 과열된 지역으로 강화된 청약 자격이 적용되는 지역을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Region` and (`isSubscriptionOverheatedArea` value true)
- **참고**: 이전에 Primitive Class로 정의되었으나, `isSubscriptionOverheatedArea` boolean 속성으로 명확히 정의 가능하므로 Defined Class로 변경되었습니다.
- **법적 근거**: 주택법 제63조

### `RegulatedRegion_Defined` (규제지역 - 정의)
- **설명**: 투기과열지구 또는 청약과열지역으로 지정된 모든 지역을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `Region` and ((`isSpeculativeOverheatedZone` value true) or (`isSubscriptionOverheatedArea` value true))
- **참고**: `RegulatedArea` Primitive Class는 추상적 개념으로 유지되며, 이 Defined Class는 실제 규제 대상 지역을 자동으로 분류합니다.

## 8. 재당첨 제한 관련 정의 클래스

### `ActiveRestrictionPeriod` (재당첨 제한 기간 중)
- **설명**: 과거 당첨 이력으로 인해 현재 재당첨 제한 기간에 해당하는 당첨 기록을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `WinningRecord` and
    - `isSubjectToRestriction` value true and
    - `winningDate` some xsd:date[(currentDate - winningDate) / 365 <= restrictionPeriodInYears]

### `HouseholdWithRecentWinning` (최근 당첨 이력 있는 세대)
- **설명**: 세대원 중 5년 이내 당첨 이력이 있는 세대를 정의합니다. 1순위 자격을 제한합니다.
- **논리 정의 (Equivalent To)**:
    - `Household` and
    - `hasMember` some (`HouseholdMember` and
      `hasWinningRecord` some (`WinningRecord` and
        `winningDate` some xsd:date[(currentDate - winningDate) / 365 <= 5]))

### `CompletedContractWinning_Defined` (계약 완료 당첨 - 정의)
- **설명**: 당첨 후 계약을 완료한 이력을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `WinningRecord` and (`contractCompleted` value true)

### `AbandonedContractWinning_Defined` (계약 포기 당첨 - 정의)
- **설명**: 당첨 후 계약을 포기한 이력을 정의합니다.
- **논리 정의 (Equivalent To)**:
    - `WinningRecord` and (`contractCompleted` value false)

## 4. 특별공급 클래스 간 관계

-   **상호 배타 클래스 (Disjoint Classes)**: 아래의 특별공급 자격 클래스들은 서로 상호 배타적으로 정의됩니다. 이는 온톨로지 추론 시 각 클래스를 명확하게 구분하기 위함입니다. (한 신청자가 여러 자격 조건을 동시에 만족하여 여러 클래스의 개체가 될 수는 있지만, 클래스 정의 자체는 서로를 포함하지 않도록 설계합니다.)
    -   `NewlywedSpecialSupplyApplicant`
    -   `FirstTimeHomeBuyerSpecialSupplyApplicant`
    -   `MultiChildSpecialSupplyApplicant`
    -   `SupportingAgedParentsSpecialSupplyApplicant`
    -   `InstitutionalRecommendationSpecialSupplyApplicant`

---
*주: 위의 논리 정의에서 `meets_*_criteria`와 같은 표현은 실제 온톨로지에서는 구체적인 소득/자산 금액 비교 규칙(Rule)이나 SWRL(Semantic Web Rule Language) 등으로 구현되어야 할 복잡한 조건을 간략하게 표현한 것입니다. 예를 들어, `meets_deposit_criteria_for_region_and_area`는 아래와 같은 SWRL 규칙으로 구체화될 수 있습니다.*
```swrl
// 서울 거주, 85㎡ 이하 주택 신청 시 예치금 300만원 이상
Applicant(a), livesIn(a, ?seoul), regionName(?seoul, "서울"), appliesFor(a, ?app), isForHousing(?app, ?h), area(?h, ?ar), swrlb:lessThanOrEqual(?ar, 85), hasSubscriptionAccount(a, ?acc), depositAmount(?acc, ?dep), swrlb:greaterThanOrEqual(?dep, 3000000) -> meets_deposit_criteria(a, true)
```

**온톨로지 표현의 한계 (Limitations of OWL)**

본 온톨로지 모델은 청약 '자격 조건'을 논리적으로 '분류(Classify)'하는 데 중점을 둡니다. 따라서 아래와 같은 일부 청약 제도의 절차적, 계산적 측면은 OWL만으로 완전하게 표현하기 어렵고 별도의 어플리케이션 로직(예: SPARQL 쿼리, Rule Engine)이 필요합니다.

-   **가점제 (Point System)**: 무주택 기간, 부양가족 수 등에 따라 점수를 '계산'하고 합산하여 순위를 매기는 방식은 OWL의 추론 범위 밖입니다. 온톨로지는 가점 계산에 필요한 기본 데이터(예: `homelessStartDate`)를 제공하는 역할을 합니다.
-   **추첨제 및 공급 비율 (Lottery System)**: 특정 조건 하에서 추첨을 하거나 가점제와 추첨제 비율(예: 50:50)을 적용하는 것은 절차적 규칙으로, 온톨로지 모델링 대상이 아닙니다.
-   **조건부 자격 (Conditional Eligibility)**: '기존 주택 처분 조건부'와 같이 특정 행위를 서약하는 조건은 온톨로지 상에서는 현재 상태(1주택 소유)로만 판단 가능하며, 조건 이행 여부의 관리는 별도의 시스템 로직이 필요합니다.
