# 아파트 청약 자격 온톨로지 Competency Questions (CQs)

본 문서는 아파트 청약 자격 판단 온톨로지가 답변해야 하는 핵심적인 역량 질문(Competency Questions)을 정의합니다. 각 CQ는 현재 인스턴스 데이터와 Defined Class 정의를 기반으로 추론 가능하도록 설계되었습니다.

## A. 기본 자격 및 개인 현황 (Basic & Personal Status)

### CQ-A1: 성년 (Adult)
- **질문**: "김철수(45세)는 청약 신청이 가능한 '성년(Adult)'인가요?"
- **예상 답변**: 예 (age >= 19)
- **관련 인스턴스**: `Kim_ChulSoo`

### CQ-A2: 미성년 자녀 (MinorChild)
- **질문**: "김민지(17세)는 '미성년 자녀(MinorChild)'인가요?"
- **예상 답변**: 예 (Child이고 age < 19)
- **관련 인스턴스**: `Kim_MinJi`

### CQ-A3: 영유아 자녀 (InfantChild)
- **질문**: "박하늘(2세)은 '영유아 자녀(InfantChild)'인가요?"
- **예상 답변**: 예 (Child이고 age <= 6)
- **관련 인스턴스**: `Park_HaNeul`

### CQ-A4: 고령 부양가족 (ElderlyDependent)
- **질문**: "이동구(78세)는 '고령 부양가족(ElderlyDependent)'인가요?"
- **예상 답변**: 예 (QualifiedDependent이고 age >= 65)
- **관련 인스턴스**: `Lee_DongGu`

### CQ-A5: 인정 부양가족 (QualifiedDependent_Defined)
- **질문**: "강민정(40세, 장애인)은 '인정 부양가족(QualifiedDependent_Defined)'인가요?"
- **예상 답변**: 예 (hasDisability = true)
- **관련 인스턴스**: `Kang_MinJung`

## B. 세대 및 주택 소유 현황 (Household & Housing Ownership)

### CQ-B1: 무주택세대구성원 (HomelessHouseholdMember)
- **질문**: "박영호 세대의 구성원들은 '무주택세대구성원(HomelessHouseholdMember)'인가요?"
- **예상 답변**: 예 (모든 구성원이 NonHousingOwner)
- **관련 인스턴스**: `Park_YoungHo`, `Choi_SuJin`, `Park_HaNeul`

### CQ-B2: 무주택세대주 (HeadOfHomelessHousehold)
- **질문**: "이민수는 '무주택세대주(HeadOfHomelessHousehold)'인가요?"
- **예상 답변**: 예 (HeadOfHousehold이고 HomelessHouseholdMember)
- **관련 인스턴스**: `Lee_MinSoo`

### CQ-B3: 유주택 세대 (Non-HomelessHouseholdMember)
- **질문**: "최동현 세대의 구성원들은 '무주택세대구성원'이 아닌가요?"
- **예상 답변**: 예 (최동현이 HousingOwner이므로 세대 전체가 무주택세대 아님)
- **관련 인스턴스**: `Choi_DongHyun`, `Kim_EunJi`

### CQ-B4: 1인 가구 (SinglePersonHousehold_Defined)
- **질문**: "정수영 세대는 '1인 가구(SinglePersonHousehold_Defined)'인가요?"
- **예상 답변**: 예 (hasMember 카디널리티 = 1)
- **관련 인스턴스**: `Household_Jung`

### CQ-B5: 맞벌이 가구 (DualIncomeHousehold_Defined)
- **질문**: "김철수 세대는 '맞벌이 가구(DualIncomeHousehold_Defined)'인가요?"
- **예상 답변**: 예 (부부 모두 personalIncome > 0)
- **관련 인스턴스**: `Household_Kim`

## C. 지역 및 거주 현황 (Region & Residence)

### CQ-C1: 수도권 거주자 (MetropolitanAreaResident)
- **질문**: "김철수는 '수도권 거주자(MetropolitanAreaResident)'인가요?"
- **예상 답변**: 예 (livesIn Seoul, Seoul은 MetropolitanArea)
- **관련 인스턴스**: `Kim_ChulSoo`

### CQ-C2: 장기 거주자 (LongTermResident)
- **질문**: "이민수는 '장기 거주자(LongTermResident)'인가요?"
- **예상 답변**: 예 (거주 기간 24년 >= 3년)
- **관련 인스턴스**: `Lee_MinSoo`

### CQ-C3: 투기과열지구 (SpeculativeOverheatedZone_Defined)
- **질문**: "서울은 '투기과열지구(SpeculativeOverheatedZone_Defined)'인가요?"
- **예상 답변**: 예 (isSpeculativeOverheatedZone = true)
- **관련 인스턴스**: `Seoul`

### CQ-C4: 규제지역 (RegulatedRegion_Defined)
- **질문**: "경기도는 '규제지역(RegulatedRegion_Defined)'인가요?"
- **예상 답변**: 예 (isSubscriptionOverheatedArea = true)
- **관련 인스턴스**: `Gyeonggi`

## D. 특별공급 자격 (Special Supply Eligibility)

### CQ-D1: 생애최초 자격자 (FirstTimeHomeBuyer_Qualified)
- **질문**: "정수영은 '생애최초 자격자(FirstTimeHomeBuyer_Qualified)'인가요?"
- **예상 답변**: 예 (본인 및 세대원 전원 NeverOwnedHousingPerson)
- **관련 인스턴스**: `Jung_SooYoung`

### CQ-D2: 생애최초 자격 불충족 (Non-FirstTimeHomeBuyer)
- **질문**: "김철수는 '생애최초 자격자'인가요?"
- **예상 답변**: 아니오 (HousingOwnershipHistoryHolder - 과거 소유 이력 있음)
- **관련 인스턴스**: `Kim_ChulSoo`

### CQ-D3: 예비신혼부부 신청자 (ProspectiveNewlywedApplicant)
- **질문**: "윤재호는 '예비신혼부부 신청자(ProspectiveNewlywedApplicant)'인가요?"
- **예상 답변**: 예 (미혼, hasFianceCommitment = true, expectedMarriageDate 있음)
- **관련 인스턴스**: `Yoon_JaeHo`

### CQ-D4: 한부모가족 신청자 (SingleParentFamilyApplicant)
- **질문**: "한지영은 '한부모가족 신청자(SingleParentFamilyApplicant)'인가요?"
- **예상 답변**: 예 (isSingleParent = true, 영유아 자녀 한서윤(5세) 있음)
- **관련 인스턴스**: `Han_JiYoung`

### CQ-D5: 노부모 부양자 (ElderlyParentSupporter)
- **질문**: "이민수는 '노부모 부양자(ElderlyParentSupporter)'인가요?"
- **예상 답변**: 예 (hasElderlyDependent로 이동구(78세) 연결)
- **관련 인스턴스**: `Lee_MinSoo`

### CQ-D6: 노부모부양 특별공급 신청자 (SupportingAgedParentsApplicant)
- **질문**: "이민수는 '노부모부양 특별공급 신청자(SupportingAgedParentsApplicant)'인가요?"
- **예상 답변**: 예 (ElderlyParentSupporter이고 HeadOfHomelessHousehold)
- **관련 인스턴스**: `Lee_MinSoo`

### CQ-D7: 무순위 청약 신청자 (UnrankedSubscriptionApplicant)
- **질문**: "임무는 '무순위 청약 신청자(UnrankedSubscriptionApplicant)'인가요?"
- **예상 답변**: 예 (Applicant, Adult, HomelessHouseholdMember)
- **관련 인스턴스**: `Lim_Mu`

## E. 가점 관련 (Subscription Points)

### CQ-E1: 고득점 신청자 (HighPointApplicant)
- **질문**: "이민수(59점)는 '고득점 신청자(HighPointApplicant)'인가요?"
- **예상 답변**: 아니오 (totalSubscriptionPoints = 59 < 60)
- **관련 인스턴스**: `Lee_MinSoo`

### CQ-E2: 무주택 기간 만점 (MaxHomelessPeriodPoints)
- **질문**: "이민수는 '무주택 기간 만점(MaxHomelessPeriodPoints)'인가요?"
- **예상 답변**: 예 (homelessPeriodInYears = 15, homelessPeriodPoints = 32)
- **관련 인스턴스**: `Lee_MinSoo`

## F. 주택 특성 (Housing Characteristics)

### CQ-F1: 소형주택 (SmallSizeHousing_Defined)
- **질문**: "서울 A 아파트(59㎡)는 '소형주택(SmallSizeHousing_Defined)'인가요?"
- **예상 답변**: 예 (area <= 85.0)
- **관련 인스턴스**: `Housing_Project_A`

### CQ-F2: 중형주택 (MediumSizeHousing_Defined)
- **질문**: "경기 D 아파트(102㎡)는 '중형주택(MediumSizeHousing_Defined)'인가요?"
- **예상 답변**: 예 (85.0 < area <= 102.0)
- **관련 인스턴스**: `Housing_Project_D`

### CQ-F3: 대형주택 (LargeSizeHousing_Defined)
- **질문**: "반포래미안트리니원(114㎡)은 '대형주택(LargeSizeHousing_Defined)'인가요?"
- **예상 답변**: 예 (area > 102.0)
- **관련 인스턴스**: `Housing_Banpo_Raemian_Trinity`

### CQ-F4: 소형저가주택 (SmallLowPriceHousing_Defined)
- **질문**: "경기 소형저가주택(55㎡, 1.2억원)은 '소형저가주택(SmallLowPriceHousing_Defined)'인가요?"
- **예상 답변**: 예 (area <= 60, price <= 1.3억, 수도권 소재)
- **관련 인스턴스**: `Housing_SmallLowPrice`

## G. 집계 쿼리 (Aggregation Queries)

### CQ-G1: 전체 무주택세대주 목록
- **질문**: "현재 데이터에서 '무주택세대주'는 몇 명이고 누구인가요?"
- **예상 답변**: 9명 (김철수, 박영호, 이민수, 정수영, 한지영, 윤재호, 강민정, 장광, 임무)

### CQ-G2: 전체 생애최초 자격자 목록
- **질문**: "현재 데이터에서 '생애최초 자격자'는 몇 명이고 누구인가요?"
- **예상 답변**: 7명 (박영호, 이민수, 정수영, 한지영, 윤재호, 강민정, 임무 - 김철수와 장광은 제외)

### CQ-G3: 소형주택 목록
- **질문**: "현재 데이터에서 '소형주택'은 몇 채이고 어떤 것들인가요?"
- **예상 답변**: 다수 (area <= 85㎡인 모든 주택)
