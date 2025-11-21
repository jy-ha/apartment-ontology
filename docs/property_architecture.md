# 아파트 청약 자격 온톨로지 속성 아키텍처 (Property Architecture)

본 문서는 아파트 청약 자격 온톨로지의 클래스들이 갖는 속성(Property)을 정의합니다. 속성은 개체(Individual)들 간의 관계를 나타내는 **객체 속성(Object Property)**과 개체의 실제 데이터 값을 나타내는 **데이터 속성(Data Property)**으로 구분됩니다.

## 1. 객체 속성 (Object Properties)

객체 속성은 한 개체(Domain)를 다른 개체(Range)와 연결하여 관계를 정의합니다.

| 속성명 (Property)           | 정의역 (Domain)           | 치역 (Range)              | 특징 (Characteristics)                          | 역관계 (InverseOf)     | 설명                                                                 |
| --------------------------- | ------------------------- | ------------------------- | ----------------------------------------------- | -------------------- | -------------------------------------------------------------------- |
| `belongsToHousehold`        | `HouseholdMember`         | `Household`               |                                                 | `hasMember`          | 특정 세대구성원이 어느 세대에 속해 있는지를 나타냅니다.              |
| `hasMember`                 | `Household`               | `HouseholdMember`         |                                                 | `belongsToHousehold` | 특정 세대가 어떤 세대구성원들을 포함하는지를 나타냅니다.             |
| `hasHead`                   | `Household`               | `HeadOfHousehold`         | `Functional`                                    | `isHeadOf`           | 세대의 세대주가 누구인지를 나타냅니다. (한 세대는 한 명의 세대주)    |
| `isHeadOf`                  | `HeadOfHousehold`         | `Household`               |                                                 | `hasHead`            | 특정인이 어느 세대의 세대주인지를 나타냅니다.                        |
| `hasSpouse`                 | `HouseholdMember`         | `HouseholdMember`         | `Symmetric`, `Irreflexive`                      |                      | 배우자 관계를 나타냅니다. (A의 배우자가 B이면, B의 배우자도 A)       |
| `hasChild`                  | `HouseholdMember`         | `HouseholdMember`         | `Asymmetric`, `Irreflexive`                     | `hasParent`          | 자녀 관계를 나타냅니다.                                              |
| `hasParent`                 | `HouseholdMember`         | `HouseholdMember`         | `Asymmetric`, `Irreflexive`                     | `hasChild`           | 부모 관계를 나타냅니다. (`hasChild`의 역관계)                        |
| `isDependentOf`             | `HouseholdMember`         | `Applicant`               |                                                 | `hasDependent`       | 특정 세대구성원이 신청자의 부양가족임을 나타냅니다.                  |
| `hasDependent`              | `Applicant`               | `HouseholdMember`         |                                                 | `isDependentOf`      | 신청자가 부양하는 가족 구성원을 나타냅니다.                          |
| `owns`                      | `HouseholdMember`         | `Housing`                 |                                                 | `isOwnedBy`          | 세대구성원이 주택을 소유하고 있음을 나타냅니다.                      |
| `isOwnedBy`                 | `Housing`                 | `HouseholdMember`         |                                                 | `owns`               | 주택이 누구에 의해 소유되었는지를 나타냅니다.                        |
| `hasSubscriptionAccount`    | `Applicant`               | `SubscriptionAccount`     |                                                 |                      | 신청자가 보유한 청약통장을 나타냅니다.                               |
| `livesIn`                   | `Person`                  | `Region`                  | 특정인이 거주하는 지역을 나타냅니다.                                 |
| `isLocatedIn`               | `Housing`                 | `Region`                  | 주택이 위치한 지역을 나타냅니다.                                     |
| `hasWinningRecord`          | `HouseholdMember`         | `WinningRecord`           | 세대구성원의 과거 청약 당첨 이력을 나타냅니다.                       |
| `appliesFor`                | `Applicant`               | `SubscriptionApplication` | 신청자가 어떤 청약에 신청하는지를 나타냅니다.                        |
| `hasTotalAsset`             | `Household`               | `Asset`                   | 세대가 보유한 총 자산을 나타냅니다.                                  |
| `hasIncome`                 | `Household`               | `Income`                  | 세대의 소득 정보를 나타냅니다.                                       |
| `isForHousing`              | `SubscriptionApplication` | `Housing`                 |                                                 |                      | 청약 신청이 어떤 주택을 대상으로 하는지 나타냅니다.                  |
| `isRecommendedBy`           | `Applicant`               | `Institution`             |                                                 | `recommends`         | 신청자가 어떤 기관에 의해 추천되었는지를 나타냅니다.                 |
| `recommends`                | `Institution`             | `Applicant`               |                                                 | `isRecommendedBy`    | 기관이 추천한 신청자를 나타냅니다.                                   |
| `ownsAsset`                 | `HouseholdMember`         | `Asset`                   |                                                 | `isAssetOwnedBy`     | 세대구성원이 보유한 자산(부동산, 자동차 등)을 나타냅니다.            |
| `isAssetOwnedBy`            | `Asset`                   | `HouseholdMember`         |                                                 | `ownsAsset`          | 자산이 누구에 의해 소유되었는지를 나타냅니다.                        |
| `ownsLand`                  | `HouseholdMember`         | `LandAsset`               |                                                 | `isLandOwnedBy`      | 세대구성원이 보유한 토지 자산을 나타냅니다.                          |
| `isLandOwnedBy`             | `LandAsset`               | `HouseholdMember`         |                                                 | `ownsLand`           | 토지가 누구에 의해 소유되었는지를 나타냅니다.                        |
| `ownsBuilding`              | `HouseholdMember`         | `BuildingAsset`           |                                                 | `isBuildingOwnedBy`  | 세대구성원이 보유한 건물 자산을 나타냅니다.                          |
| `isBuildingOwnedBy`         | `BuildingAsset`           | `HouseholdMember`         |                                                 | `ownsBuilding`       | 건물이 누구에 의해 소유되었는지를 나타냅니다.                        |
| `ownsVehicle`               | `HouseholdMember`         | `VehicleAsset`            |                                                 | `isVehicleOwnedBy`   | 세대구성원이 보유한 차량을 나타냅니다.                               |
| `isVehicleOwnedBy`          | `VehicleAsset`            | `HouseholdMember`         |                                                 | `ownsVehicle`        | 차량이 누구에 의해 소유되었는지를 나타냅니다.                        |
| `hasPointCalculation`       | `Applicant`               | `SubscriptionPoint`       |                                                 |                      | 신청자의 청약 가점 계산 정보를 나타냅니다.                           |
| `appliesInRegion`           | `DepositRequirement`      | `Region`                  |                                                 |                      | 예치금 요건이 적용되는 지역을 나타냅니다.                            |
| `basedOnStandard`           | `IncomeThreshold`         | `StandardIncome`          |                                                 |                      | 소득 기준선이 기반하는 표준 소득을 나타냅니다.                       |
| `appliesTo`                 | `IncomeThreshold`         | `SubscriptionApplication` |                                                 |                      | 소득 기준선이 적용되는 청약 유형을 나타냅니다.                       |
| `usesSelectionMethod`       | `Housing`                 | `SelectionMethod`         |                                                 |                      | 주택의 당첨자 선정 방식을 나타냅니다.                                |
| `hasResidenceHistory`       | `Person`                  | `ResidenceHistory`        |                                                 |                      | 개인의 거주 이력을 나타냅니다.                                       |
| `residedIn`                 | `ResidenceHistory`        | `Region`                  |                                                 |                      | 거주 이력의 해당 지역을 나타냅니다.                                  |
| `hasTaxPaymentHistory`      | `Applicant`               | `TaxPaymentHistory`       |                                                 |                      | 신청자의 소득세 납부 이력을 나타냅니다.                              |
| `hasOwnershipHistory`       | `Person`                  | `HousingOwnershipHistory` |                                                 |                      | 개인의 주택 소유 이력을 나타냅니다.                                  |
| `ownedHousing`              | `HousingOwnershipHistory` | `Housing`                 |                                                 |                      | 소유 이력에 해당하는 주택을 나타냅니다.                              |
| `hasMinorChild`             | `Person`                  | `MinorChild`              | `SubPropertyOf: hasChild`                       |                      | 만 19세 미만의 자녀를 나타냅니다.                                    |
| `hasInfantChild`            | `Person`                  | `InfantChild`             | `SubPropertyOf: hasChild`                       |                      | 만 6세 이하의 자녀를 나타냅니다.                                     |
| `hasQualifiedDependent`     | `Applicant`               | `QualifiedDependent`      | `SubPropertyOf: hasDependent`                   |                      | 가점제에서 인정되는 부양가족을 나타냅니다.                           |
| `hasElderlyDependent`       | `Applicant`               | `ElderlyDependent`        | `SubPropertyOf: hasQualifiedDependent`          |                      | 만 65세 이상의 부양가족을 나타냅니다.                                |

## 2. 데이터 속성 (Data Properties)

데이터 속성은 개체가 갖는 구체적인 데이터 값(리터럴)을 정의합니다.

| 속성명 (Property)               | 정의역 (Domain)         | 치역 (Range) & 제약 (Restriction) | 특징 (Characteristics) | 설명                                                                 |
| ------------------------------- | ----------------------- | ----------------------------------- | ---------------------- | -------------------------------------------------------------------- |
| `age`                           | `Person`                | `xsd:integer`                       | `Functional`           | 사람의 만 나이를 나타냅니다.                                         |
| `name`                          | `Person`                | `string`                            |                        | 사람의 이름을 나타냅니다.                                            |
| `nationalID`                    | `Person`                | `string`                            |                        | 개인을 고유하게 식별하는 값 (주민등록번호 등). `Person` 클래스의 키(Key)로 사용됩니다. |
| `maritalStatus`                 | `Person`                | `string`                            |                        | 혼인 상태를 나타냅니다. (e.g., "미혼", "기혼", "이혼", "사별")        |
| `marriageDate`                  | `Person`                | `date`                              |                        | 혼인신고일. 신혼부부 특공 자격 판단에 사용됩니다.                    |
| `employmentStatus`              | `Person`                | `string`                            |                        | 고용 상태. (e.g., "재직", "휴직", "실업"). 소득 산정 시 고려될 수 있습니다. |
| `homelessStartDate`             | `Applicant`             | `date`            | 무주택 기간 산정 시작일.                                             |
| `residencePeriod`               | `Person`                | `float` (년)      | 특정 지역에서의 거주 기간을 나타냅니다.                              |
| `taxPaymentDuration`            | `Applicant`             | `integer` (년)                      |                        | 소득세 납부 총 기간(통산). 생애최초 특공 자격에 사용됩니다.           |
| `accountNumber`                 | `SubscriptionAccount`   | `string`                            |                        | 청약통장을 고유하게 식별하는 계좌번호. `SubscriptionAccount` 클래스의 키(Key)로 사용됩니다. |
| `accountOpeningDate`            | `SubscriptionAccount`   | `date`                              |                        | 청약통장 가입일.                                                     |
| `depositAmount`                 | `SubscriptionAccount`   | `xsd:integer` (원)                  |                        | 청약통장의 현재 예치금액.                                            |
| `monthlyPaymentCount`           | `SubscriptionAccount`   | `xsd:integer` (회)                  |                        | 청약통장 월 납입 횟수 (국민주택).                                    |
| `accountType`                   | `SubscriptionAccount`   | `string`                            |                        | 청약통장의 종류. (e.g., "주택청약종합저축", "청약예금")                |
| `area`                          | `Housing`               | `float` (㎡)                        |                        | 주택의 전용 면적.                                                    |
| `price`                         | `Housing`               | `integer` (원)                      |                        | 주택의 공시가격 또는 실거래가.                                       |
| `winningDate`                   | `WinningRecord`         | `date`                              |                        | 과거 청약 당첨일. 재당첨 제한 기간 산정에 사용됩니다.                |
| `monthlyAverageIncome`          | `Income`                | `integer` (원)                      |                        | 세대의 월평균 소득.                                                  |
| `realEstateAssetValue`          | `RealEstate`            | `integer` (원)                      |                        | 세대가 보유한 부동산 자산의 총액.                                    |
| `vehicleAssetValue`             | `VehicleAsset`          | `integer` (원)                      |                        | 세대가 보유한 자동차 자산의 총액.                                    |
| `isSpeculativeOverheatedZone`   | `Region`                | `boolean`         | 해당 지역이 투기과열지구인지 여부.                                   |
| `isSubscriptionOverheatedArea`  | `Region`                | `boolean`         | 해당 지역이 청약과열지역인지 여부.                                   |
| `recruitmentAnnouncementDate`   | `SubscriptionApplication` | `date`            | 입주자 모집공고일. 모든 자격 판단의 기준일이 됩니다.               |
| `restrictionPeriodInYears`      | `WinningRecord`         | `integer`         | 청약 당첨에 따른 재당첨 제한 기간 (년).                              |
| `supportStartDate`              | `HouseholdMember`       | `date`            | (직계존속 등) 부양 시작일. 노부모부양 자격 판단에 사용됩니다.        |
| `isSingleParent`                | `Applicant`             | `boolean`                           |                        | 한부모가족 여부.                                                     |
| `fetusCount`                    | `Person`                | `xsd:integer`                       |                        | 임신 중인 태아의 수. 다자녀가구 특공 자녀 수 산정에 사용됩니다.      |
| `standardAmount`                | `StandardIncome`        | `integer` (원)                      |                        | 기준 소득 금액.                                                      |
| `yearOfStandard`                | `StandardIncome`        | `integer`         | 해당 기준 소득이 적용되는 연도.                                      |
| `householdSize`                 | `StandardIncome`        | `integer`         |                        | 해당 기준 소득이 적용되는 가구원 수.                                 |
| `contractCompleted`             | `WinningRecord`         | `boolean`         | `Functional`           | 당첨 후 계약 완료 여부. false이면 계약 포기로 간주됩니다.            |
| `isSubjectToRestriction`        | `WinningRecord`         | `boolean`         | `Functional`           | 재당첨 제한 대상 여부.                                               |
| `disposalDate`                  | `Housing`               | `date`            |                        | 주택 처분일. 소형·저가주택 무주택 기간 산정에 사용됩니다.            |
| `designatedDate`                | `RegulatedArea`         | `date`            |                        | 규제지역 지정일.                                                     |
| `releasedDate`                  | `RegulatedArea`         | `date`            |                        | 규제지역 해제일.                                                     |
| `requiredDepositAmount`         | `DepositRequirement`    | `xsd:positiveInteger` (원)          |                    | 지역 및 면적에 따라 요구되는 예치금액.                               |
| `minArea`                       | `DepositRequirement`    | `float` (㎡)      |                        | 예치금 요건이 적용되는 최소 면적.                                    |
| `maxArea`                       | `DepositRequirement`    | `float` (㎡)      |                        | 예치금 요건이 적용되는 최대 면적.                                    |
| `homelessPeriodInYears`         | `Applicant`             | `xsd:integer` (년)                  |                 | 무주택 기간 (년 단위).                                               |
| `homelessPeriodPoints`          | `Applicant`             | `xsd:integer` [0-32]                |                | 무주택 기간에 따른 가점 (0~32점).                                    |
| `dependentCount`                | `Applicant`             | `xsd:integer`                       |                        | 인정 부양가족 수.                                                    |
| `dependentFamilyPoints`         | `Applicant`             | `xsd:integer` [0-35]                |                | 부양가족 수에 따른 가점 (0~35점).                                    |
| `accountPeriodInYears`          | `Applicant`             | `xsd:integer` (년)                  |                 | 청약통장 가입 기간 (년 단위).                                        |
| `accountPeriodPoints`           | `Applicant`             | `xsd:integer` [0-17]                |                | 청약통장 가입 기간에 따른 가점 (0~17점).                             |
| `totalSubscriptionPoints`       | `Applicant`             | `xsd:integer` [0-84]                | `Functional`   | 총 청약 가점 (0~84점). 무주택 기간 + 부양가족 + 통장 가입 기간 점수의 합. |
| `hasDisability`                 | `Person`                | `boolean`                           |                        | 장애 등록 여부.                                                      |
| `incomePercentage`              | `IncomeThreshold`       | `xsd:positiveInteger` (%)           |                        | 도시근로자 가구당 월평균 소득 대비 비율 (예: 100, 130, 140, 160).    |
| `calculatedThresholdAmount`     | `IncomeThreshold`       | `xsd:positiveInteger` (원)          |                        | 계산된 소득 기준선 금액.                                             |
| `personalIncome`                | `Person`                | `xsd:integer` (원)                  |                        | 개인의 월평균 소득.                                                  |
| `isOnChildcareLeave`            | `Person`                | `boolean`                           |                        | 육아휴직 중 여부.                                                    |
| `childcareLeaveAllowance`       | `Person`                | `xsd:integer` (원)                  |                        | 육아휴직 급여.                                                       |
| `landAssetValue`                | `LandAsset`             | `xsd:integer` (원)                  |                        | 토지 자산 가액.                                                      |
| `buildingAssetValue`            | `BuildingAsset`         | `xsd:integer` (원)                  |                        | 건물 자산 가액.                                                      |
| `maxRealEstateValue`            | `AssetThreshold`        | `xsd:positiveInteger` (원)          |                        | 부동산 자산 보유 한도.                                               |
| `maxVehicleValue`               | `AssetThreshold`        | `xsd:positiveInteger` (원)          |                        | 자동차 자산 보유 한도.                                               |
| `actualMarriageDate`            | `Person`                | `date`            |                        | 실제 결혼식 날짜 (혼인신고일과 다를 수 있음).                        |
| `marriageRegistrationDate`      | `Person`                | `date`            | `Functional`           | 혼인신고일. 신혼부부 특공 자격의 기준일입니다.                       |
| `hasFianceCommitment`           | `Applicant`             | `boolean`         |                        | 예비신혼부부로서 입주 전 혼인신고 약속 여부.                         |
| `expectedMarriageDate`          | `Applicant`             | `date`            |                        | 예정된 혼인신고일.                                                   |
| `singleParentCertificationDate` | `Applicant`             | `date`            |                        | 한부모가족 증명서 발급일.                                            |
| `isAdoptedChild`                | `Person`                | `boolean`         |                        | 입양 자녀 여부.                                                      |
| `adoptionDate`                  | `Person`                | `date`            |                        | 입양일.                                                              |
| `selectionRatio`                | `SelectionMethod`       | `float` [0.0-1.0] |                        | 선정 방식의 적용 비율 (예: 가점제 0.5, 추첨제 0.5).                  |
| `residenceStartDate`            | `ResidenceHistory`      | `date`            |                        | 해당 지역 거주 시작일.                                               |
| `residenceEndDate`              | `ResidenceHistory`      | `date`            |                        | 해당 지역 거주 종료일.                                               |
| `residenceDurationInYears`      | `ResidenceHistory`      | `float` (년)      |                        | 해당 지역 거주 기간 (년 단위).                                       |
| `taxYear`                       | `TaxPaymentHistory`     | `gYear`           |                        | 소득세 납부 연도.                                                    |
| `taxAmount`                     | `TaxPaymentHistory`     | `xsd:integer` (원)                  |                        | 해당 연도 소득세 납부액.                                             |
| `recommendationDate`            | `Applicant`             | `date`            |                        | 기관추천일.                                                          |
| `recommendationNumber`          | `Applicant`             | `string`          |                        | 기관추천 번호.                                                       |
| `ownershipStartDate`            | `HousingOwnershipHistory` | `date`          |                        | 주택 소유 시작일.                                                    |
| `ownershipEndDate`              | `HousingOwnershipHistory` | `date`          |                        | 주택 소유 종료일 (처분일).                                           |
| `regionName`                    | `Region`                | `string`          |                        | 지역 명칭 (예: "서울", "경기", "인천").                              |
| `pointValue`                    | `SubscriptionPoint`     | `xsd:integer` [0-84]                |                        | 가점 항목의 점수 값.                                                 |
| `hasDepositShortage`            | `Applicant`             | `xsd:integer` (원)                  |                        | 청약통장 예치금 부족액.                                              |
| `minElderlyAge`                 | `SupportingAgedParentsRequirement` | `xsd:positiveInteger`   |                        | 노부모부양 인정을 위한 최소 부모 나이 (만 나이).                      |
| `minSupportYears`               | `SupportingAgedParentsRequirement` | `xsd:positiveInteger`   |                        | 노부모부양 인정을 위한 최소 부양 기간 (년 단위).                      |
