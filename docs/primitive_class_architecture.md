# 아파트 청약 자격 온톨로지 원시 클래스 아키텍처 (Primitive Class Architecture)

본 문서는 아파트 청약 자격 온톨로지의 기초를 형성하는 원시 클래스(Primitive Class)와 그 계층 구조를 정의합니다. 원시 클래스는 온톨로지에서 가장 기본적인 개념 단위로, 더 복잡한 개념(Defined Class)을 정의하는 데 사용됩니다.

## 최상위 클래스 (Top-Level Class)

-   **`Thing`**: 모든 클래스의 최상위 슈퍼 클래스입니다. (owl:Thing)

## 클래스 계층 구조 (Class Hierarchy)

### 1. `Person` (사람)

-   **설명**: 온톨로지에서 개인을 나타내는 최상위 클래스입니다. 신청자, 세대구성원 등의 하위 클래스를 가집니다.
-   **하위 클래스**:
    -   **`Applicant` (신청자)**: 주택 청약을 신청하는 주체입니다. 온톨로지의 중심이 되는 클래스 중 하나입니다.
    -   **`HouseholdMember` (세대구성원)**: 세대를 구성하는 모든 개인을 나타냅니다. 신청자는 항상 세대구성원에 속합니다.
        -   **`HeadOfHousehold` (세대주)**: 세대의 대표자인 세대주입니다. 청약 자격에서 중요한 역할을 합니다.
        -   **`NonHeadOfHouseholdMember` (세대원)**: 세대주가 아닌 세대구성원입니다.
        -   **`QualifiedDependent` (인정 부양가족)**: 가점제에서 부양가족으로 인정받을 수 있는 세대구성원의 기본 클래스입니다.
        -   **`Child` (자녀)**: 직계비속인 자녀를 나타냅니다.
        -   **`HousingOwner` (주택 소유자)**: 현재 주택을 소유하고 있는 세대구성원입니다. (Closed World 구현용)
        -   **`NonHousingOwner` (무주택자)**: 현재 주택을 소유하지 않은 세대구성원입니다. (Closed World 구현용)
    -   **`HousingOwnershipHistoryHolder` (주택 소유 이력 보유자)**: 과거에 주택을 소유한 적이 있는 사람입니다.
    -   **`NeverOwnedHousingPerson` (주택 소유 이력 없는 자)**: 과거에 주택을 소유한 적이 없는 사람입니다.

### 2. `Household` (세대)

-   **설명**: 주거 및 생계를 같이하는 단위인 세대를 나타냅니다. `HouseholdMember`들의 집합으로 구성됩니다.

### 3. `Housing` (주택)

-   **설명**: 주거 목적의 건물, 즉 주택을 나타내는 클래스입니다.
-   **하위 클래스**:
    -   **`NationalHousing` (국민주택)**: 국가, 지자체, LH 등이 건설하는 주택으로, 특정 소득/자산 기준을 충족해야 합니다.
    -   **`PrivateHousing` (민영주택)**: 민간 건설사가 건설하는 주택입니다.
    -   **`CancelledContractHousing` (계약취소주택)**: 불법 전매나 공급 질서 교란으로 계약이 취소된 주택으로, 재공급 시 엄격한 자격 요건이 적용됩니다.
    -   **`PostSubscriptionHousing` (사후접수주택)**: 1, 2순위 청약 마감 후 미계약 물량으로 무순위로 공급되는 주택입니다.

**참고**: 
- 면적에 따른 주택 분류(`SmallSizeHousing`, `MediumSizeHousing`, `LargeSizeHousing`)는 Defined Class입니다 (`defined_classes.md` 참조).
- 소형·저가주택(`SmallLowPriceHousing`)은 명확한 논리적 기준(면적 ≤60㎡, 가격 ≤1.3억원, 수도권 소재)으로 정의 가능하므로 Defined Class로 변경되었습니다 (`defined_classes.md` 참조).

### 4. `SubscriptionAccount` (청약통장)

-   **설명**: 주택 청약을 위해 가입하는 금융 상품입니다. 가입 기간, 예치금 등이 자격 판단의 주요 요소입니다.

### 5. `Place` (장소)

-   **설명**: 지리적 위치나 구역을 나타내는 클래스입니다.
-   **하위 클래스**:
    -   **`Region` (지역)**: 서울, 경기도 등 행정 구역을 나타냅니다. 거주지 및 주택 건설 지역을 특정하는 데 사용됩니다. 구체적인 지역(서울, 경기, 인천 등)은 Individual로 정의됩니다.
        -   **`MetropolitanArea` (수도권)**: 서울, 경기, 인천을 포함하는 광역 권역입니다. 이는 추상적 범주 클래스이며, 구체적인 수도권 지역들(Seoul, Gyeonggi, Incheon)은 Individual로 정의됩니다 (`individuals.md` 또는 `core.ttl` 참조).
    -   **`RegulatedArea` (규제지역)**: 부동산 시장 안정을 위해 지정된 특별 구역을 나타내는 추상적 클래스입니다. 실제 규제 여부는 Region Individual의 `isSpeculativeOverheatedZone` 또는 `isSubscriptionOverheatedArea` 속성으로 판단합니다.

**참고**: 
- **투기과열지구와 청약과열지역**: 이전에 Primitive Class로 정의되었으나, `isSpeculativeOverheatedZone`, `isSubscriptionOverheatedArea` boolean 속성으로 명확히 정의 가능하므로 Defined Class로 변경되었습니다 (`defined_classes.md`의 `SpeculativeOverheatedZone_Defined`, `SubscriptionOverheatedArea_Defined` 참조).
- **구체적 지역 개체**: Seoul, Gyeonggi, Incheon은 Individual입니다 (`individuals.md` 섹션 1 참조).

### 6. `Concept` (추상적 개념)

-   **설명**: 물리적 실체는 없지만, 청약 제도에서 중요한 역할을 하는 추상적인 개념들을 나타내는 클래스입니다.
-   **하위 클래스**:
    -   **`SubscriptionApplication` (청약 신청)**: 주택을 공급받기 위해 의사를 표시하는 행위 또는 그 자체를 나타냅니다. 공급 유형에 따라 세분화됩니다.
        -   **`GeneralSupply` (일반공급)**
        -   **`SpecialSupply` (특별공급)**
            -   **`InstitutionalRecommendation` (기관추천)**: 국가유공자, 장애인, 중소기업 근로자 등 기관 추천을 받은 자를 위한 특별공급
            -   **`MultiChildHouseholdSupply` (다자녀가구)**: 만 19세 미만 자녀 3명 이상을 둔 가구를 위한 특별공급
            -   **`NewlywedCoupleSupply` (신혼부부)**: 혼인 기간 7년 이내의 신혼부부를 위한 특별공급
                -   **`NewlywedPrioritySupply` (신혼부부 우선공급)**: 만 6세 이하 자녀가 있거나 소득 기준 100% 이하인 경우
                -   **`NewlywedGeneralSupply` (신혼부부 일반공급)**: 우선공급에 해당하지 않는 신혼부부
            -   **`SupportingAgedParentsSupply` (노부모부양)**: 만 65세 이상 부모를 3년 이상 부양하는 자를 위한 특별공급
            -   **`FirstTimeHomeBuyerSupply` (생애최초)**: 생애 최초로 주택을 구매하는 자를 위한 특별공급
        -   **`UnrankedSubscription` (무순위 청약)**
    -   **`Asset` (자산)**: 세대가 보유한 경제적 가치를 지닌 재산을 나타냅니다. 소득과 함께 특정 청약 자격의 기준이 됩니다.
        -   **`RealEstate` (부동산 자산)**: 토지 및 건물 등 부동산 자산
            -   **`LandAsset` (토지 자산)**: 세대가 보유한 토지
            -   **`BuildingAsset` (건물 자산)**: 세대가 보유한 건물
        -   **`VehicleAsset` (자동차 자산)**: 세대가 보유한 자동차
    -   **`Income` (소득)**: 세대의 월평균 소득을 나타냅니다.
    -   **`WinningRecord` (당첨 이력)**: 과거 청약 당첨 사실을 나타냅니다. 재당첨 제한 여부를 판단하는 데 사용됩니다.
    -   **`StandardIncome` (기준 소득)**: 도시근로자 가구당 월평균 소득과 같이, 소득 기준을 판단하기 위한 기준값을 나타냅니다.
        -   **`UrbanWorkerStandardIncome` (도시근로자 가구당 월평균 소득)**: 가구원 수별, 연도별로 정부가 고시하는 기준 소득
    -   **`IncomeThreshold` (소득 기준선)**: 특정 청약 유형에 적용되는 소득 기준(예: 130%, 140%, 160% 등)을 나타냅니다.
    -   **`AssetThreshold` (자산 기준선)**: 특정 청약 유형에 적용되는 자산 보유 한도(부동산, 자동차 등)를 나타냅니다.
    -   **`DepositRequirement` (예치금 요건)**: 지역별, 면적별로 요구되는 청약통장 예치금 기준을 나타냅니다.
    -   **`SelectionMethod` (당첨자 선정 방식)**: 청약 당첨자를 선정하는 방법을 나타냅니다.
        -   **`PointBasedSelection` (가점제)**: 가점 점수가 높은 순으로 선정
        -   **`LotteryBasedSelection` (추첨제)**: 무작위 추첨으로 선정
    -   **`HousingOwnershipHistory` (주택 소유 이력)**: 개인의 과거 주택 소유 이력을 나타냅니다. 생애최초 특공 자격 판단에 사용됩니다.
    -   **`ResidenceHistory` (거주 이력)**: 개인의 지역별 거주 이력을 나타냅니다. 해당 지역 거주 기간 판단에 사용됩니다.
    -   **`TaxPaymentHistory` (소득세 납부 이력)**: 신청자의 연도별 소득세 납부 이력을 나타냅니다. 생애최초 특공 자격 판단에 사용됩니다.

### 7. `Institution` (추천 기관)
-   **설명**: 기관추천 특별공급 대상자를 추천하는 공공기관을 나타내는 클래스입니다. 구체적인 기관들(국가보훈처, 지방자치단체 등)은 Individual로 정의됩니다.

**참고**: 
- **구체적 기관 개체**: `NationalVeteransInstitution_Korea`, `LocalGovernment_Generic`, `SMEMinistry_Korea`, `NorthKoreanRefugeeFoundation_Korea`는 Individual입니다 (`individuals.md` 섹션 7 또는 `core.ttl` 참조).
- 이전에 하위 클래스로 정의되었으나, 각 기관은 유일하고 구체적인 조직이므로 Individual로 변경되었습니다.

### 8. 클래스 관계 제약 (Class Axioms)

OWL 2의 고급 기능을 활용하여 클래스 간의 관계를 명확히 정의하고 모델의 논리적 정합성을 강화합니다.

-   **상호 배타 클래스 (Disjoint Classes)**: 특정 개체가 두 개 이상의 클래스에 동시에 속할 수 없도록 정의하여 모호성을 제거합니다.
    -   주택 유형: `NationalHousing`, `PrivateHousing`는 서로 상호 배타적입니다.
    -   세대구성원: `HeadOfHousehold`, `NonHeadOfHouseholdMember`은 서로 상호 배타적입니다.
    -   **주택 소유 상태**: `HousingOwner`, `NonHousingOwner`는 서로 상호 배타적입니다. (Closed World 구현)
    -   **주택 소유 이력**: `HousingOwnershipHistoryHolder`, `NeverOwnedHousingPerson`은 서로 상호 배타적입니다. (Closed World 구현)
    -   자산 유형: `LandAsset`, `BuildingAsset`, `VehicleAsset`는 서로 상호 배타적입니다.
    -   선정 방식: `PointBasedSelection`, `LotteryBasedSelection`은 서로 상호 배타적입니다.
    -   특별공급 유형: `InstitutionalRecommendation`, `MultiChildHouseholdSupply`, `NewlywedCoupleSupply`, `SupportingAgedParentsSupply`, `FirstTimeHomeBuyerSupply`는 서로 상호 배타적입니다.

**참고**: 
- 지역(Seoul, Gyeonggi, Incheon)은 이제 Individual이므로 클래스 간 Disjoint 선언이 제거되었습니다.
- 추천 기관도 Individual로 변경되어 클래스 간 Disjoint 선언이 제거되었습니다.

-   **상호 배타 합집합 (Disjoint Union)**: 어떤 클래스가 하위 클래스들의 완전한 집합이면서, 동시에 각 하위 클래스들이 서로 배타적임을 정의합니다.
    -   `HouseholdMember`는 `HeadOfHousehold`와 `NonHeadOfHouseholdMember`의 상호 배타 합집합입니다. 즉, 모든 세대구성원은 반드시 세대주이거나 세대원 둘 중 하나여야 하며, 둘 다일 수는 없습니다.

-   **Covering Axiom을 통한 Closed World 구현**: OWL의 Open World Assumption(OWA) 문제를 해결하기 위해, 특정 속성에 대해 Disjoint + Covering을 사용합니다.
    -   `HouseholdMember`는 `HousingOwner` 또는 `NonHousingOwner` 중 하나에 속해야 합니다.
    -   `HouseholdMember`는 `HousingOwnershipHistoryHolder` 또는 `NeverOwnedHousingPerson` 중 하나에 속해야 합니다.
    -   **인스턴스 데이터 요구사항**: 모든 `HouseholdMember` 인스턴스에는 위 클래스들의 타입이 명시적으로 선언되어야 합니다. 이를 통해 `hasMember only NonHousingOwner`와 같은 조건이 정상적으로 추론됩니다.

**참고**:
- `MetropolitanArea`의 DisjointUnion 선언이 제거되었습니다. Seoul, Gyeonggi, Incheon이 Individual로 변경되었기 때문입니다. 대신 각 Individual은 `MetropolitanArea` 타입을 가집니다.

**참고**: 당첨 이력의 계약 완료/포기 구분, 자녀 연령별 분류 등은 `defined_classes.md`를 참조하십시오.

-   **커버링 공리 (Covering Axiom)**: 특정 클래스가 하위 클래스들로 완전히 커버됨을 정의합니다.
    -   모든 `SpecialSupply`는 5가지 하위 클래스 중 하나입니다.
    -   모든 `SelectionMethod`는 `PointBasedSelection` 또는 `LotteryBasedSelection` 중 하나입니다.
