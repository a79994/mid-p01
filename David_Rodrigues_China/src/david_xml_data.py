#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper module generating all 12 BaseX XML containers for David Rodrigues (China).
Each container complies strictly with David_Rodrigues_China/models/china_logistics_trade.xsd
"""

def get_xml_containers():
    c53 = """<?xml version="1.0" encoding="utf-8"?>
<ChineseSeaportsCatalog>
  <PortComplex unlocode="CNSHA" customsDistrictCode="2200" provinceCodeGB="310000">
    <PortName en="Shanghai Port" zh="上海港"/>
    <AnnualThroughputMillionTEU>49.15</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="SHA-YS-P4" operator="Shanghai International Port Group (SIPG)" maxDraftMeters="17.5" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEU1" alliance="Ocean Alliance (COSCO / CMA CGM / Evergreen / OOCL)" destinationPortPT="PTSIN" transitDaysSuez="25" transitDaysGoodHope="37"/>
          <LinerService serviceCode="FAL3" alliance="Ocean Alliance" destinationPortPT="PTLEI" transitDaysSuez="27" transitDaysGoodHope="39"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
      <Terminal terminalId="SHA-WGQ-P5" operator="SIPG Outer Gaoqiao Logistics" maxDraftMeters="15.0" automatedAGVs="false">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="FE2" alliance="THE Alliance / Premier" destinationPortPT="PTSIN" transitDaysSuez="28" transitDaysGoodHope="40"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
  <PortComplex unlocode="CNNGB" customsDistrictCode="3100" provinceCodeGB="330000">
    <PortName en="Ningbo-Zhoushan Port" zh="宁波舟山港"/>
    <AnnualThroughputMillionTEU>35.30</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="NGB-MSH-01" operator="Ningbo Zhoushan Port Co., Ltd. (Meishan Phase 2)" maxDraftMeters="17.8" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEU3" alliance="Ocean Alliance" destinationPortPT="PTSIN" transitDaysSuez="26" transitDaysGoodHope="38"/>
          <LinerService serviceCode="MD2" alliance="2M / Gemini Alliance" destinationPortPT="PTSIN" transitDaysSuez="27" transitDaysGoodHope="39"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
      <Terminal terminalId="NGB-BL-P4" operator="Ningbo Beilun Container Terminal" maxDraftMeters="16.0" automatedAGVs="false">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEX1" alliance="Independent" destinationPortPT="PTSIN" transitDaysSuez="29" transitDaysGoodHope="41"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
  <PortComplex unlocode="CNSZX" customsDistrictCode="5300" provinceCodeGB="440000">
    <PortName en="Shenzhen Port (Yantian &amp; Shekou)" zh="深圳港"/>
    <AnnualThroughputMillionTEU>30.01</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="SZX-YICT-P3" operator="Hutchison Ports Yantian" maxDraftMeters="17.6" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEU7" alliance="Ocean Alliance" destinationPortPT="PTSIN" transitDaysSuez="23" transitDaysGoodHope="35"/>
          <LinerService serviceCode="BYD-RORO" alliance="BYD Shipping Special Charter" destinationPortPT="PTSIN" transitDaysSuez="24" transitDaysGoodHope="36"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
      <Terminal terminalId="SZX-SCT-01" operator="China Merchants Port Group (Shekou)" maxDraftMeters="15.5" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="Lion-SZX" alliance="MSC Independent Service" destinationPortPT="PTSIN" transitDaysSuez="24" transitDaysGoodHope="36"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
  <PortComplex unlocode="CNQDG" customsDistrictCode="4200" provinceCodeGB="370000">
    <PortName en="Qingdao Port" zh="青岛港"/>
    <AnnualThroughputMillionTEU>28.70</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="QDG-QW-AUTO" operator="Shandong Port Group Qingdao Automation Terminal" maxDraftMeters="18.0" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEU5" alliance="Ocean Alliance" destinationPortPT="PTSIN" transitDaysSuez="28" transitDaysGoodHope="40"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
  <PortComplex unlocode="CNTXG" customsDistrictCode="0200" provinceCodeGB="120000">
    <PortName en="Tianjin Port" zh="天津港"/>
    <AnnualThroughputMillionTEU>22.18</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="TXG-SEC-C" operator="Tianjin Port Group Smart Zero-Carbon Terminal" maxDraftMeters="16.5" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="NEU4" alliance="Ocean Alliance" destinationPortPT="PTSIN" transitDaysSuez="30" transitDaysGoodHope="42"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
  <PortComplex unlocode="CNGZG" customsDistrictCode="5100" provinceCodeGB="440000">
    <PortName en="Guangzhou Port (Nansha)" zh="广州港南沙"/>
    <AnnualThroughputMillionTEU>25.40</AnnualThroughputMillionTEU>
    <DeepWaterTerminals>
      <Terminal terminalId="GZG-NS-P4" operator="Guangzhou Port Group Nansha Automated Port" maxDraftMeters="16.0" automatedAGVs="true">
        <DirectLinerRoutesToPortugal>
          <LinerService serviceCode="AEU2" alliance="Ocean Alliance" destinationPortPT="PTSIN" transitDaysSuez="24" transitDaysGoodHope="36"/>
        </DirectLinerRoutesToPortugal>
      </Terminal>
    </DeepWaterTerminals>
  </PortComplex>
</ChineseSeaportsCatalog>"""

    c54 = """<?xml version="1.0" encoding="utf-8"?>
<MaritimeVoyagesRegistry>
  <MaritimeVoyage voyageId="VOY-COSCO-UNIV-2026-01" vesselImo="9795610" serviceLoop="AEU1-Loop">
    <VesselDetails>
      <VesselName>COSCO SHIPPING UNIVERSE</VesselName>
      <CarrierLine>COSCO SHIPPING Lines Co., Ltd.</CarrierLine>
      <FlagState>Hong Kong (HKG)</FlagState>
      <NominalCapacityTEU>21237</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNSHA" timestampCSTorUTC="2026-03-24T08:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="CNNGB" timestampCSTorUTC="2026-03-26T14:30:00+08:00" operation="Departure"/>
      <PortCall seq="3" unlocode="SGSIN" timestampCSTorUTC="2026-04-02T10:00:00+08:00" operation="Bunkering"/>
      <PortCall seq="4" unlocode="ZACPT" timestampCSTorUTC="2026-04-16T18:00:00+02:00" operation="Transit Cape of Good Hope"/>
      <PortCall seq="5" unlocode="PTSIN" timestampCSTorUTC="2026-04-29T06:00:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="VLSFO 0.5% S + Biofuel B24" consumedMetricTons="4850.50" voyageRoute="Cape of Good Hope Diversion (Red Sea Security Bypass)"/>
  </MaritimeVoyage>
  <MaritimeVoyage voyageId="VOY-BYD-EXP-2026-01" vesselImo="9842105" serviceLoop="BYD-Direct-Loop">
    <VesselDetails>
      <VesselName>BYD EXPLORER NO.1</VesselName>
      <CarrierLine>BYD Auto Shipping / Zodiac Maritime</CarrierLine>
      <FlagState>Liberia (LBR)</FlagState>
      <NominalCapacityTEU>7000</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNSZX" timestampCSTorUTC="2026-03-28T12:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="SGSIN" timestampCSTorUTC="2026-04-02T04:00:00+08:00" operation="Bunkering LNG"/>
      <PortCall seq="3" unlocode="EGPSD" timestampCSTorUTC="2026-04-14T20:00:00+02:00" operation="Suez Canal Convoy"/>
      <PortCall seq="4" unlocode="PTSIN" timestampCSTorUTC="2026-04-21T07:30:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="Dual-Fuel LNG (Clean Energy)" consumedMetricTons="1680.00" voyageRoute="Suez Canal Maritime Highway"/>
  </MaritimeVoyage>
  <MaritimeVoyage voyageId="VOY-COSCO-SOLAR-2026-02" vesselImo="9795634" serviceLoop="AEU3-Loop">
    <VesselDetails>
      <VesselName>COSCO SHIPPING SOLAR</VesselName>
      <CarrierLine>COSCO SHIPPING Lines Co., Ltd.</CarrierLine>
      <FlagState>Hong Kong (HKG)</FlagState>
      <NominalCapacityTEU>21237</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNSHA" timestampCSTorUTC="2026-04-02T09:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="CNNGB" timestampCSTorUTC="2026-04-04T16:00:00+08:00" operation="Departure"/>
      <PortCall seq="3" unlocode="ZACPT" timestampCSTorUTC="2026-04-24T12:00:00+02:00" operation="Transit Cape of Good Hope"/>
      <PortCall seq="4" unlocode="PTSIN" timestampCSTorUTC="2026-05-08T14:00:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="VLSFO 0.5% S" consumedMetricTons="4920.00" voyageRoute="Cape of Good Hope Bypass"/>
  </MaritimeVoyage>
  <MaritimeVoyage voyageId="VOY-COSCO-PISCES-2026-01" vesselImo="9795646" serviceLoop="AEU7-Loop">
    <VesselDetails>
      <VesselName>COSCO SHIPPING PISCES</VesselName>
      <CarrierLine>COSCO SHIPPING Lines Co., Ltd.</CarrierLine>
      <FlagState>Hong Kong (HKG)</FlagState>
      <NominalCapacityTEU>20119</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNSZX" timestampCSTorUTC="2026-03-10T11:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="ZACPT" timestampCSTorUTC="2026-04-01T08:00:00+02:00" operation="Transit Cape of Good Hope"/>
      <PortCall seq="3" unlocode="PTSIN" timestampCSTorUTC="2026-04-18T16:00:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="VLSFO 0.5% S" consumedMetricTons="4710.00" voyageRoute="Cape of Good Hope Diversion"/>
  </MaritimeVoyage>
  <MaritimeVoyage voyageId="VOY-BYD-CHGZ-2026-01" vesselImo="9842117" serviceLoop="BYD-Direct-Loop">
    <VesselDetails>
      <VesselName>BYD CHANGZHOU</VesselName>
      <CarrierLine>BYD Auto Shipping</CarrierLine>
      <FlagState>Liberia (LBR)</FlagState>
      <NominalCapacityTEU>7000</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNSZX" timestampCSTorUTC="2026-04-10T10:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="EGPSD" timestampCSTorUTC="2026-04-26T22:00:00+02:00" operation="Suez Canal Convoy"/>
      <PortCall seq="3" unlocode="PTSIN" timestampCSTorUTC="2026-05-03T09:00:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="Dual-Fuel LNG" consumedMetricTons="1650.00" voyageRoute="Suez Canal Route"/>
  </MaritimeVoyage>
  <MaritimeVoyage voyageId="VOY-COSCO-TAURUS-2026-02" vesselImo="9795622" serviceLoop="AEU1-Loop">
    <VesselDetails>
      <VesselName>COSCO SHIPPING TAURUS</VesselName>
      <CarrierLine>COSCO SHIPPING Lines Co., Ltd.</CarrierLine>
      <FlagState>Hong Kong (HKG)</FlagState>
      <NominalCapacityTEU>20119</NominalCapacityTEU>
    </VesselDetails>
    <ItineraryRotation>
      <PortCall seq="1" unlocode="CNNGB" timestampCSTorUTC="2026-04-15T08:00:00+08:00" operation="Departure"/>
      <PortCall seq="2" unlocode="ZACPT" timestampCSTorUTC="2026-05-06T15:00:00+02:00" operation="Transit Cape of Good Hope"/>
      <PortCall seq="3" unlocode="PTSIN" timestampCSTorUTC="2026-05-20T11:00:00+01:00" operation="Discharge"/>
    </ItineraryRotation>
    <BunkerFuelAndEmissions fuelType="VLSFO 0.5% S" consumedMetricTons="4890.00" voyageRoute="Cape of Good Hope Route"/>
  </MaritimeVoyage>
</MaritimeVoyagesRegistry>"""

    c55 = """<?xml version="1.0" encoding="utf-8"?>
<ElectronicBillsOfLading>
  <BillOfLading blNumber="COSU6288991101" gaccDeclarationId18="220120260000108801" invoiceNo="INV-CN-2026-8801" issueDate="2026-03-22">
    <Parties shipperUsccOrNif="91320413MA1M9Y2C4B" consigneeEoriOrUscc="PT517890123" notifyPartyTaxId="517890123"/>
    <Routing portOfLoading="CNSHA" portOfDischarge="PTSIN" placeOfDelivery="ZILS Sines Gigafactory Site, Portugal" vesselImo="9795610"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU8001101" sizeType="40HC" customsSealNo="CN-GACC-9011" packagesCount="5000" grossWeightKg="460000.00" volumeCbm="620.0">
        <HSCode6WCO>850760</HSCode6WCO>
        <CargoDescription>CALB L314Ah Zero-Carbon LFP Battery Pack Modules (UN3480)</CargoDescription>
      </Container>
      <Container isoNumber="COSU8001102" sizeType="40HC" customsSealNo="CN-GACC-9012" packagesCount="5000" grossWeightKg="460000.00" volumeCbm="620.0">
        <HSCode6WCO>850760</HSCode6WCO>
        <CargoDescription>CALB L314Ah Zero-Carbon LFP Battery Pack Modules (UN3480)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="158000.00" insuranceAmountUSD="20100.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991102" gaccDeclarationId18="530120260000108802" invoiceNo="INV-CN-2026-8802" issueDate="2026-03-27">
    <Parties shipperUsccOrNif="91440300192317458F" consigneeEoriOrUscc="PT500234567" notifyPartyTaxId="500234567"/>
    <Routing portOfLoading="CNSZX" portOfDischarge="PTSIN" placeOfDelivery="Setúbal / Carregado Auto Logistics Hub, PT" vesselImo="9842105"/>
    <ContainerizedCargoList>
      <Container isoNumber="BYDU9002201" sizeType="RORO-DECK" customsSealNo="CN-GACC-9021" packagesCount="400" grossWeightKg="890000.00" volumeCbm="5680.0">
        <HSCode6WCO>870380</HSCode6WCO>
        <CargoDescription>400x BYD Seal AWD Blade Battery Electric Sedans</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="210000.00" insuranceAmountUSD="35000.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991103" gaccDeclarationId18="220120260000108803" invoiceNo="INV-CN-2026-8803" issueDate="2026-03-24">
    <Parties shipperUsccOrNif="91610132724912345X" consigneeEoriOrUscc="PT502345678" notifyPartyTaxId="502345678"/>
    <Routing portOfLoading="CNSHA" portOfDischarge="PTSIN" placeOfDelivery="Parque Solar Cerca / EDP Renováveis, Alentejo, PT" vesselImo="9795610"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU8003301" sizeType="40HC" customsSealNo="CN-GACC-9031" packagesCount="18000" grossWeightKg="1700000.00" volumeCbm="2480.0">
        <HSCode6WCO>854143</HSCode6WCO>
        <CargoDescription>LONGi Hi-MO 7 Bifacial Solar Photovoltaic Modules</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="COLLECT" freightAmountUSD="92000.00" insuranceAmountUSD="14500.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991104" gaccDeclarationId18="310120260000108804" invoiceNo="INV-CN-2026-8804" issueDate="2026-03-31">
    <Parties shipperUsccOrNif="91350900587527783P" consigneeEoriOrUscc="PT502345678" notifyPartyTaxId="502345678"/>
    <Routing portOfLoading="CNNGB" portOfDischarge="PTLEI" placeOfDelivery="REN Subestação de Palmela / Alqueva ESS, PT" vesselImo="9795634"/>
    <ContainerizedCargoList>
      <Container isoNumber="CATU8004401" sizeType="40HC" customsSealNo="CN-GACC-9041" packagesCount="3200" grossWeightKg="355000.00" volumeCbm="480.0">
        <HSCode6WCO>850760</HSCode6WCO>
        <CargoDescription>CATL EnerOne Liquid Cooling BESS Modules (UN3480)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="84000.00" insuranceAmountUSD="18000.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991106" gaccDeclarationId18="310120260000108806" invoiceNo="INV-CN-2026-8806" issueDate="2026-04-03">
    <Parties shipperUsccOrNif="91330200778899112T" consigneeEoriOrUscc="PT500889911" notifyPartyTaxId="500889911"/>
    <Routing portOfLoading="CNNGB" portOfDischarge="PTSIN" placeOfDelivery="Martifer Metalomecânica, Oliveira de Frades, PT" vesselImo="9795634"/>
    <ContainerizedCargoList>
      <Container isoNumber="NBSU8006601" sizeType="20GP" customsSealNo="CN-GACC-9061" packagesCount="1200" grossWeightKg="2100000.00" volumeCbm="820.0">
        <HSCode6WCO>720838</HSCode6WCO>
        <CargoDescription>Hot-Rolled Structural Alloy Steel Coils (S355JR)</CargoDescription>
      </Container>
      <Container isoNumber="NBSU8006602" sizeType="20GP" customsSealNo="CN-GACC-9062" packagesCount="1200" grossWeightKg="2100000.00" volumeCbm="820.0">
        <HSCode6WCO>720838</HSCode6WCO>
        <CargoDescription>Hot-Rolled Structural Alloy Steel Coils (S355JR)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="72000.00" insuranceAmountUSD="9800.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991108" gaccDeclarationId18="530120260000108808" invoiceNo="INV-CN-2026-8808" issueDate="2026-04-06">
    <Parties shipperUsccOrNif="91440300618837699Q" consigneeEoriOrUscc="PT500456789" notifyPartyTaxId="500456789"/>
    <Routing portOfLoading="CNSZX" portOfDischarge="PTSIN" placeOfDelivery="MEO Altice Portugal Hub Bobadela, PT" vesselImo="9795646"/>
    <ContainerizedCargoList>
      <Container isoNumber="HWU8008801" sizeType="40HC" customsSealNo="CN-GACC-9081" packagesCount="450" grossWeightKg="18200.00" volumeCbm="68.0">
        <HSCode6WCO>851762</HSCode6WCO>
        <CargoDescription>Huawei 5G Massive MIMO Active Antenna Units (AAU)</CargoDescription>
      </Container>
      <Container isoNumber="HWU8008802" sizeType="40HC" customsSealNo="CN-GACC-9082" packagesCount="450" grossWeightKg="18200.00" volumeCbm="68.0">
        <HSCode6WCO>851762</HSCode6WCO>
        <CargoDescription>Huawei 5G Baseband Units (BBU) &amp; Optical Routers</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="38500.00" insuranceAmountUSD="12000.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991110" gaccDeclarationId18="510120260000108810" invoiceNo="INV-CN-2026-8810" issueDate="2026-04-08">
    <Parties shipperUsccOrNif="91440606190342599T" consigneeEoriOrUscc="PT500123456" notifyPartyTaxId="500123456"/>
    <Routing portOfLoading="CNGZG" portOfDischarge="PTSIN" placeOfDelivery="Worten Sonae Logistics Center, Azambuja, PT" vesselImo="9795646"/>
    <ContainerizedCargoList>
      <Container isoNumber="MDU8010001" sizeType="40HC" customsSealNo="CN-GACC-9101" packagesCount="2500" grossWeightKg="22400.00" volumeCbm="74.0">
        <HSCode6WCO>841510</HSCode6WCO>
        <CargoDescription>Midea Inverter Split Heat Pump Air Conditioners</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="26000.00" insuranceAmountUSD="4500.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991111" gaccDeclarationId18="010120260000108811" invoiceNo="INV-CN-2026-8811" issueDate="2026-04-14">
    <Parties shipperUsccOrNif="911100007178071858" consigneeEoriOrUscc="PT503456789" notifyPartyTaxId="503456789"/>
    <Routing portOfLoading="CNTXG" portOfDischarge="PTSIN" placeOfDelivery="Metropolitano de Lisboa / PMO Pontinha, PT" vesselImo="9795622"/>
    <ContainerizedCargoList>
      <Container isoNumber="CRCU8011101" sizeType="40OT" customsSealNo="CN-GACC-9111" packagesCount="120" grossWeightKg="29500.00" volumeCbm="65.0">
        <HSCode6WCO>860719</HSCode6WCO>
        <CargoDescription>CRRC Bogie Assemblies and Traction Motor Sets for Metro Trains</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="42000.00" insuranceAmountUSD="8500.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991113" gaccDeclarationId18="530120260000108813" invoiceNo="INV-CN-2026-8813" issueDate="2026-04-11">
    <Parties shipperUsccOrNif="91440300192317458F" consigneeEoriOrUscc="PT500234567" notifyPartyTaxId="500234567"/>
    <Routing portOfLoading="CNSZX" portOfDischarge="PTSIN" placeOfDelivery="Salvador Caetano Hub, Vila Nova de Gaia, PT" vesselImo="9842117"/>
    <ContainerizedCargoList>
      <Container isoNumber="BYDU9013301" sizeType="RORO-DECK" customsSealNo="CN-GACC-9131" packagesCount="350" grossWeightKg="755000.00" volumeCbm="4950.0">
        <HSCode6WCO>870380</HSCode6WCO>
        <CargoDescription>350x BYD Atto 3 Blade Battery Compact SUVs</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="185000.00" insuranceAmountUSD="29000.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288991114" gaccDeclarationId18="310120260000108814" invoiceNo="INV-CN-2026-8803" issueDate="2026-04-16">
    <Parties shipperUsccOrNif="91320400608131370B" consigneeEoriOrUscc="PT502345678" notifyPartyTaxId="502345678"/>
    <Routing portOfLoading="CNSHA" portOfDischarge="PTSIN" placeOfDelivery="Parque Solar Alcoutim / Neoen, Algarve, PT" vesselImo="9795622"/>
    <ContainerizedCargoList>
      <Container isoNumber="TSU8014401" sizeType="40HC" customsSealNo="CN-GACC-9141" packagesCount="17500" grossWeightKg="1670000.00" volumeCbm="2420.0">
        <HSCode6WCO>854143</HSCode6WCO>
        <CargoDescription>Trina Solar Vertex N TOPCon Photovoltaic Modules</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="COLLECT" freightAmountUSD="89000.00" insuranceAmountUSD="13800.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288992201" gaccDeclarationId18="220120261000990001" invoiceNo="INV-PT-2026-9901" issueDate="2026-03-24">
    <Parties shipperUsccOrNif="PT500265432" consigneeEoriOrUscc="91110000101123456N" notifyPartyTaxId="91110000101123456N"/>
    <Routing portOfLoading="PTLEI" portOfDischarge="CNSHA" placeOfDelivery="COFCO Wine Cellars, Shanghai Waigaoqiao FTZ" vesselImo="9795610"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU4455661" sizeType="40RF" customsSealNo="PT-AT-0411" packagesCount="24000" grossWeightKg="36000.00" volumeCbm="68.0">
        <HSCode6WCO>220421</HSCode6WCO>
        <CargoDescription>Vinho Tinto DOC Douro &amp; Porto Reserva Sogrape Vinhos S.A.</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="8500.00" insuranceAmountUSD="2100.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288992202" gaccDeclarationId18="220120261000990002" invoiceNo="INV-PT-2026-9902" issueDate="2026-03-28">
    <Parties shipperUsccOrNif="PT500876543" consigneeEoriOrUscc="91440300755673010C" notifyPartyTaxId="91440300755673010C"/>
    <Routing portOfLoading="PTSIN" portOfDischarge="CNSZX" placeOfDelivery="Shenzhen Qianhai Food Bonded Hub, China" vesselImo="9795634"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU4455662" sizeType="40RF" customsSealNo="PT-AT-0412" packagesCount="36000" grossWeightKg="42000.00" volumeCbm="70.0">
        <HSCode6WCO>150920</HSCode6WCO>
        <CargoDescription>Azeite Virgem Extra Oliveira da Serra (Sovena Portugal)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="7900.00" insuranceAmountUSD="1800.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288992203" gaccDeclarationId18="220120261000990003" invoiceNo="INV-PT-2026-9903" issueDate="2026-04-01">
    <Parties shipperUsccOrNif="PT500345678" consigneeEoriOrUscc="91330200778899112T" notifyPartyTaxId="91330200778899112T"/>
    <Routing portOfLoading="PTSET" portOfDischarge="CNNGB" placeOfDelivery="Zhejiang Paper Mills, Ningbo Bonded Port, China" vesselImo="9795634"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU4455663" sizeType="40HC" customsSealNo="PT-AT-0413" packagesCount="120000" grossWeightKg="125000.00" volumeCbm="210.0">
        <HSCode6WCO>470329</HSCode6WCO>
        <CargoDescription>Pasta de Madeira Química de Eucalipto (The Navigator Company)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="14200.00" insuranceAmountUSD="2900.00"/>
  </BillOfLading>
  <BillOfLading blNumber="COSU6288992207" gaccDeclarationId18="220120261000990005" invoiceNo="INV-PT-2026-9905" issueDate="2026-04-18">
    <Parties shipperUsccOrNif="PT500123999" consigneeEoriOrUscc="91110000101123456N" notifyPartyTaxId="91110000101123456N"/>
    <Routing portOfLoading="PTLEI" portOfDischarge="CNNGB" placeOfDelivery="Ningbo Meishan Bonded Port Wine Packaging Base" vesselImo="9795622"/>
    <ContainerizedCargoList>
      <Container isoNumber="COSU4455665" sizeType="40HC" customsSealNo="PT-AT-0417" packagesCount="85000" grossWeightKg="48000.00" volumeCbm="92.0">
        <HSCode6WCO>450410</HSCode6WCO>
        <CargoDescription>Rolhas e Aglomerados de Cortiça Natural (Corticeira Amorim)</CargoDescription>
      </Container>
    </ContainerizedCargoList>
    <FreightCharges paymentTerms="PREPAID" freightAmountUSD="6800.00" insuranceAmountUSD="1400.00"/>
  </BillOfLading>
</ElectronicBillsOfLading>"""

    c56 = """<?xml version="1.0" encoding="utf-8"?>
<BRIRailwayConsignments>
  <RailConsignmentCIMSMGS cimSmgsNoteNo="CIMSMGS-YW2026-07" trainBlockCode="X8020-YIWU-MAD-ENT" gaccEntryId18="292120260000108807" departureDate="2026-03-15">
    <RouteCorridor originTerminalCN="Yiwu West Railway Port (CNYIW)" destinationTerminalPT="Terminal Ferroviário do Entroncamento (PTENT)" totalDistanceKm="13052" transitDays="21"/>
    <BorderGaugeBreakStations>
      <GaugeChange borderCrossing="Alashankou / Dostyk (China-Kazakhstan)" fromGaugeMm="1435" toGaugeMm="1520"/>
      <GaugeChange borderCrossing="Brest / Malaszewicze (Belarus-Poland)" fromGaugeMm="1520" toGaugeMm="1435"/>
      <GaugeChange borderCrossing="Irun / Hendaye (France-Spain Iberian Transshipment)" fromGaugeMm="1435" toGaugeMm="1668"/>
    </BorderGaugeBreakStations>
    <WagonContainers>
      <RailContainer isoNumber="YIWU4007701" wagonUicNo="31844556012" shipperUscc="91330782098765432W" consigneeEoriPT="PT500345678" hsCode6="610910" grossWeightKg="24800.00"/>
      <RailContainer isoNumber="YIWU4007702" wagonUicNo="31844556013" shipperUscc="91330782098765432W" consigneeEoriPT="PT500345678" hsCode6="620462" grossWeightKg="23500.00"/>
    </WagonContainers>
  </RailConsignmentCIMSMGS>
  <RailConsignmentCIMSMGS cimSmgsNoteNo="CIMSMGS-YW2026-12" trainBlockCode="X8020-YIWU-MAD-LIS" gaccEntryId18="292120260000108812" departureDate="2026-04-05">
    <RouteCorridor originTerminalCN="Yiwu West Railway Port (CNYIW)" destinationTerminalPT="Terminal Intermodal da Bobadela (PTLIS)" totalDistanceKm="13120" transitDays="21"/>
    <BorderGaugeBreakStations>
      <GaugeChange borderCrossing="Alashankou / Dostyk" fromGaugeMm="1435" toGaugeMm="1520"/>
      <GaugeChange borderCrossing="Brest / Malaszewicze" fromGaugeMm="1520" toGaugeMm="1435"/>
      <GaugeChange borderCrossing="Irun / Hendaye" fromGaugeMm="1435" toGaugeMm="1668"/>
    </BorderGaugeBreakStations>
    <WagonContainers>
      <RailContainer isoNumber="YIWU4012201" wagonUicNo="31844556088" shipperUscc="91330782098765432W" consigneeEoriPT="PT500987654" hsCode6="950300" grossWeightKg="19500.00"/>
      <RailContainer isoNumber="YIWU4012202" wagonUicNo="31844556089" shipperUscc="91330782098765432W" consigneeEoriPT="PT500987654" hsCode6="850440" grossWeightKg="22100.00"/>
    </WagonContainers>
  </RailConsignmentCIMSMGS>
  <RailConsignmentCIMSMGS cimSmgsNoteNo="CIMSMGS-XA2026-03" trainBlockCode="X9011-XI'AN-DUIS-LIS" gaccEntryId18="220120260000108803" departureDate="2026-03-20">
    <RouteCorridor originTerminalCN="Xi'an International Trade Logistics Park (CNXIY)" destinationTerminalPT="Terminal de Leixões Medway (PTLEI)" totalDistanceKm="12800" transitDays="19"/>
    <BorderGaugeBreakStations>
      <GaugeChange borderCrossing="Khorgos / Altynkol (China-Kazakhstan)" fromGaugeMm="1435" toGaugeMm="1520"/>
      <GaugeChange borderCrossing="Brest / Malaszewicze" fromGaugeMm="1520" toGaugeMm="1435"/>
      <GaugeChange borderCrossing="Irun / Hendaye" fromGaugeMm="1435" toGaugeMm="1668"/>
    </BorderGaugeBreakStations>
    <WagonContainers>
      <RailContainer isoNumber="XACU4003301" wagonUicNo="31844557100" shipperUscc="91610132724912345X" consigneeEoriPT="PT502345678" hsCode6="854143" grossWeightKg="26200.00"/>
    </WagonContainers>
  </RailConsignmentCIMSMGS>
  <RailConsignmentCIMSMGS cimSmgsNoteNo="CIMSMGS-CD2026-04" trainBlockCode="X8002-CD-POZ-LIS" gaccEntryId18="510120260000108810" departureDate="2026-04-02">
    <RouteCorridor originTerminalCN="Chengdu Qingbaijiang Railway Container Center" destinationTerminalPT="Terminal da Bobadela (PTLIS)" totalDistanceKm="12650" transitDays="18"/>
    <BorderGaugeBreakStations>
      <GaugeChange borderCrossing="Alashankou / Dostyk" fromGaugeMm="1435" toGaugeMm="1520"/>
      <GaugeChange borderCrossing="Brest / Malaszewicze" fromGaugeMm="1520" toGaugeMm="1435"/>
      <GaugeChange borderCrossing="Irun / Hendaye" fromGaugeMm="1435" toGaugeMm="1668"/>
    </BorderGaugeBreakStations>
    <WagonContainers>
      <RailContainer isoNumber="CDGU4004401" wagonUicNo="31844558200" shipperUscc="91440606190342599T" consigneeEoriPT="PT500123456" hsCode6="841510" grossWeightKg="21400.00"/>
    </WagonContainers>
  </RailConsignmentCIMSMGS>
  <RailConsignmentCIMSMGS cimSmgsNoteNo="CIMSMGS-ZZ2026-05" trainBlockCode="X8001-ZZ-HAM-ENT" gaccEntryId18="010120260000108811" departureDate="2026-04-12">
    <RouteCorridor originTerminalCN="Zhengzhou Putian Railway Container Terminal" destinationTerminalPT="Terminal do Entroncamento (PTENT)" totalDistanceKm="12900" transitDays="20"/>
    <BorderGaugeBreakStations>
      <GaugeChange borderCrossing="Erlianhot / Zamiin-Uud (China-Mongolia)" fromGaugeMm="1435" toGaugeMm="1520"/>
      <GaugeChange borderCrossing="Brest / Malaszewicze" fromGaugeMm="1520" toGaugeMm="1435"/>
      <GaugeChange borderCrossing="Irun / Hendaye" fromGaugeMm="1435" toGaugeMm="1668"/>
    </BorderGaugeBreakStations>
    <WagonContainers>
      <RailContainer isoNumber="ZZCU4005501" wagonUicNo="31844559300" shipperUscc="911100007178071858" consigneeEoriPT="PT503456789" hsCode6="860719" grossWeightKg="28000.00"/>
    </WagonContainers>
  </RailConsignmentCIMSMGS>
</BRIRailwayConsignments>"""

    c57 = """<?xml version="1.0" encoding="utf-8"?>
<AirCargoManifestsIATA>
  <AirWaybillManifest masterAwb="047-88991105" gaccEntryId18="010120260000108805" shipperUscc="91110108551385082Q" consigneeEoriPT="PT500123456">
    <FlightRouting airlineName="Beijing Capital Airlines (BCA)" flightNumber="JD431" originAirportIATA="HGH" destinationAirportIATA="LIS" departureUTC="2026-04-10T02:30:00Z"/>
    <ULDCargoLots>
      <ULD uldCode="PMC44111CA" chargeableWeightKg="2450.00" natureOfGoods="Xiaomi 15 Pro 5G Mobile Phones &amp; Accessories" temperatureControlC="+15C to +25C"/>
      <ULD uldCode="PMC44112CA" chargeableWeightKg="2350.00" natureOfGoods="Xiaomi Pad 6S Tablets &amp; Smartwatches" temperatureControlC="+15C to +25C"/>
    </ULDCargoLots>
  </AirWaybillManifest>
  <AirWaybillManifest masterAwb="047-88991109" gaccEntryId18="010120260000108809" shipperUscc="91110108551385082Q" consigneeEoriPT="PT500123456">
    <FlightRouting airlineName="Air China Cargo" flightNumber="CA1091" originAirportIATA="PEK" destinationAirportIATA="LIS" departureUTC="2026-04-18T05:00:00Z"/>
    <ULDCargoLots>
      <ULD uldCode="PAG55201CA" chargeableWeightKg="3100.00" natureOfGoods="Consumer Electronics &amp; High-End Laptops" temperatureControlC="+18C to +22C"/>
      <ULD uldCode="PAG55202CA" chargeableWeightKg="2900.00" natureOfGoods="IoT Smart Home Hubs and Security Sensors" temperatureControlC="+18C to +22C"/>
    </ULDCargoLots>
  </AirWaybillManifest>
  <AirWaybillManifest masterAwb="871-33221100" gaccEntryId18="530120260000108815" shipperUscc="91440300755673010C" consigneeEoriPT="PT500077568">
    <FlightRouting airlineName="Cainiao Smart Logistics / Atlas Air Charter" flightNumber="5Y8911" originAirportIATA="SZX" destinationAirportIATA="LIS" departureUTC="2026-04-20T21:15:00Z"/>
    <ULDCargoLots>
      <ULD uldCode="AKH33011CN" chargeableWeightKg="4200.00" natureOfGoods="Cross-Border E-Commerce Consolidation Express (AliExpress)" temperatureControlC="Ambient"/>
      <ULD uldCode="AKH33012CN" chargeableWeightKg="3950.00" natureOfGoods="Cross-Border E-Commerce Direct-Packs (Shein/Temu)" temperatureControlC="Ambient"/>
    </ULDCargoLots>
  </AirWaybillManifest>
  <AirWaybillManifest masterAwb="047-99112201" gaccEntryId18="220120261000990001" shipperUscc="91110000101123456N" consigneeEoriPT="PT500265432">
    <FlightRouting airlineName="TAP Cargo / Beijing Capital Airlines Alliance" flightNumber="JD432" originAirportIATA="LIS" destinationAirportIATA="HGH" departureUTC="2026-04-12T11:00:00Z"/>
    <ULDCargoLots>
      <ULD uldCode="PMC99101TP" chargeableWeightKg="1850.00" natureOfGoods="High-End Douro Vintage Wine &amp; Gourmet Olive Oil" temperatureControlC="+12C to +16C"/>
    </ULDCargoLots>
  </AirWaybillManifest>
  <AirWaybillManifest masterAwb="047-99112204" gaccEntryId18="220120261000990004" shipperUscc="91310000132234561L" consigneeEoriPT="PT500234567">
    <FlightRouting airlineName="Cargolux Airlines" flightNumber="CV7821" originAirportIATA="LIS" destinationAirportIATA="PVG" departureUTC="2026-04-22T14:40:00Z"/>
    <ULDCargoLots>
      <ULD uldCode="PAG99201CL" chargeableWeightKg="2100.00" natureOfGoods="Portuguese High-Precision Auto Components &amp; Sensors" temperatureControlC="+15C to +25C"/>
    </ULDCargoLots>
  </AirWaybillManifest>
</AirCargoManifestsIATA>"""

    c58 = """<?xml version="1.0" encoding="utf-8"?>
<CrossBorderECommerceDispatch>
  <ParcelBatch batchId="CBEC-CAINIAO-2026-05A" platformName="AliExpress / Cainiao Smart Logistics" iossNumberEU="IM5280001234" gaccRegimeCode="9610" consolidationHubCN="Dongguan Cainiao Global MegaHub">
    <Parcel s10TrackingNo="LP00667788901CN" sellerUscc="91330782098765432W" recipientPostalCodePT="1000-205" hsCode6="620462" declaredValueCNY="280.00" weightGrams="640"/>
    <Parcel s10TrackingNo="LP00667788902CN" sellerUscc="91110108551385082Q" recipientPostalCodePT="4000-120" hsCode6="851713" declaredValueCNY="960.00" weightGrams="490"/>
    <Parcel s10TrackingNo="LP00667788903CN" sellerUscc="91330782098765432W" recipientPostalCodePT="8005-139" hsCode6="620462" declaredValueCNY="195.00" weightGrams="510"/>
    <Parcel s10TrackingNo="LP00667788904CN" sellerUscc="91440300618837699Q" recipientPostalCodePT="3000-075" hsCode6="851762" declaredValueCNY="420.00" weightGrams="380"/>
    <Parcel s10TrackingNo="LP00667788905CN" sellerUscc="91110108551385082Q" recipientPostalCodePT="2900-340" hsCode6="847130" declaredValueCNY="1250.00" weightGrams="1100"/>
  </ParcelBatch>
  <ParcelBatch batchId="CBEC-SHEIN-2026-08B" platformName="Shein Fast-Fashion Logistics Hub" iossNumberEU="IM5280005678" gaccRegimeCode="9610" consolidationHubCN="Foshan Nanhai Automated Logistics Hub">
    <Parcel s10TrackingNo="LP00667788906CN" sellerUscc="91440606190342599T" recipientPostalCodePT="4700-312" hsCode6="610910" declaredValueCNY="145.00" weightGrams="320"/>
    <Parcel s10TrackingNo="LP00667788907CN" sellerUscc="91440606190342599T" recipientPostalCodePT="7000-501" hsCode6="620462" declaredValueCNY="210.00" weightGrams="450"/>
    <Parcel s10TrackingNo="LP00667788908CN" sellerUscc="91330782098765432W" recipientPostalCodePT="2500-111" hsCode6="950300" declaredValueCNY="180.00" weightGrams="580"/>
    <Parcel s10TrackingNo="LP00667788909CN" sellerUscc="91440300755673010C" recipientPostalCodePT="9000-025" hsCode6="610910" declaredValueCNY="310.00" weightGrams="720"/>
  </ParcelBatch>
  <ParcelBatch batchId="CBEC-TEMU-2026-11C" platformName="Temu / Pinduoduo Global Logistics" iossNumberEU="IM5280009012" gaccRegimeCode="9610" consolidationHubCN="Guangzhou Baiyun E-Commerce MegaCenter">
    <Parcel s10TrackingNo="LP00667788910CN" sellerUscc="91330782098765432W" recipientPostalCodePT="9500-101" hsCode6="950300" declaredValueCNY="95.00" weightGrams="260"/>
    <Parcel s10TrackingNo="LP00667788911CN" sellerUscc="91110108551385082Q" recipientPostalCodePT="3810-193" hsCode6="850440" declaredValueCNY="160.00" weightGrams="310"/>
    <Parcel s10TrackingNo="LP00667788912CN" sellerUscc="91440300618837699Q" recipientPostalCodePT="2000-045" hsCode6="851762" declaredValueCNY="240.00" weightGrams="390"/>
  </ParcelBatch>
</CrossBorderECommerceDispatch>"""

    c59 = """<?xml version="1.0" encoding="utf-8"?>
<SmartContainerTelemetryStreams>
  <ContainerTelemetry containerIso="COSU4455661" blNumber="COSU6288992201" beidouDeviceImei="860455041234561" cargoType="Reefer Container - Douro Vintage Wine">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-03-25T12:00:00Z" latitude="41.1822" longitude="-8.7011" internalTempC="13.5" humidityPct="65.0" shockG="0.12" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-05T08:00:00Z" latitude="14.8540" longitude="-17.5020" internalTempC="14.2" humidityPct="66.5" shockG="0.22" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-15T16:00:00Z" latitude="-34.3568" longitude="18.4892" internalTempC="22.8" humidityPct="78.0" shockG="1.45" anomalyAlert="REEFER_COMPRESSOR_TRIP_TEMP_EXCEEDED"/>
      <TelemetryPoint timestampUTC="2026-04-20T10:00:00Z" latitude="-10.2014" longitude="65.4021" internalTempC="14.0" humidityPct="67.0" shockG="0.18" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-05-04T06:00:00Z" latitude="31.3520" longitude="121.6540" internalTempC="13.8" humidityPct="65.5" shockG="0.10" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
  <ContainerTelemetry containerIso="COSU4455662" blNumber="COSU6288992202" beidouDeviceImei="860455041234562" cargoType="Reefer Deep-Freeze - Frozen Pork Sides">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-03-29T10:00:00Z" latitude="37.9540" longitude="-8.8680" internalTempC="-18.5" humidityPct="85.0" shockG="0.15" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-12T14:00:00Z" latitude="-34.2010" longitude="18.3500" internalTempC="-18.2" humidityPct="84.5" shockG="0.45" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-28T09:00:00Z" latitude="22.5431" longitude="114.0579" internalTempC="-18.0" humidityPct="86.0" shockG="0.12" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
  <ContainerTelemetry containerIso="COSU4455663" blNumber="COSU6288992203" beidouDeviceImei="860455041234563" cargoType="Dry Freight 40HC - Chemical Wood Pulp">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-04-02T11:00:00Z" latitude="38.5244" longitude="-8.8882" internalTempC="18.0" humidityPct="55.0" shockG="0.18" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-18T16:00:00Z" latitude="-34.1200" longitude="18.6000" internalTempC="24.5" humidityPct="62.0" shockG="0.55" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-05-02T08:00:00Z" latitude="29.8683" longitude="121.5440" internalTempC="21.0" humidityPct="58.0" shockG="0.15" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
  <ContainerTelemetry containerIso="COSU4455665" blNumber="COSU6288992207" beidouDeviceImei="860455041234565" cargoType="Dry Ventilated 40HC - Natural Cork Stoppers">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-04-19T14:00:00Z" latitude="41.1822" longitude="-8.7011" internalTempC="16.0" humidityPct="58.0" shockG="0.11" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-05-08T11:00:00Z" latitude="-34.0500" longitude="18.5200" internalTempC="21.0" humidityPct="64.0" shockG="0.32" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-05-22T07:30:00Z" latitude="29.8683" longitude="121.5440" internalTempC="19.5" humidityPct="60.0" shockG="0.10" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
  <ContainerTelemetry containerIso="COSU8001101" blNumber="COSU6288991101" beidouDeviceImei="860455041234501" cargoType="Hazmat Class 9 - LFP Battery Cells">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-03-24T10:00:00Z" latitude="31.2304" longitude="121.4737" internalTempC="20.5" humidityPct="45.0" shockG="0.14" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-14T15:00:00Z" latitude="-34.3500" longitude="18.5000" internalTempC="22.4" humidityPct="48.0" shockG="0.45" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-29T08:00:00Z" latitude="37.9540" longitude="-8.8680" internalTempC="21.5" humidityPct="46.0" shockG="0.12" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
  <ContainerTelemetry containerIso="CATU8004401" blNumber="COSU6288991104" beidouDeviceImei="860455041234504" cargoType="Hazmat Class 9 - ESS Battery Enclosure">
    <Waypoints>
      <TelemetryPoint timestampUTC="2026-04-01T12:00:00Z" latitude="29.8683" longitude="121.5440" internalTempC="19.8" humidityPct="42.0" shockG="0.11" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-04-22T16:00:00Z" latitude="-34.2200" longitude="18.4200" internalTempC="21.9" humidityPct="45.0" shockG="0.38" anomalyAlert="NONE"/>
      <TelemetryPoint timestampUTC="2026-05-08T10:00:00Z" latitude="41.1822" longitude="-8.7011" internalTempC="20.8" humidityPct="43.0" shockG="0.10" anomalyAlert="NONE"/>
    </Waypoints>
  </ContainerTelemetry>
</SmartContainerTelemetryStreams>"""

    c60 = """<?xml version="1.0" encoding="utf-8"?>
<ProductTechnicalDossiers>
  <TechnicalDossier productSkuCn="SKU-CALB-L314-LFP" manufacturerUscc="91320413MA1M9Y2C4B" cccCertNo="2025010907881201">
    <EngineeringSpecs nominalVoltageV="3.2" ratedPowerKw="1.0048" efficiencyPct="96.5" serviceLifeYears="15"/>
    <BillOfMaterials>
      <MaterialComponent componentName="Lithium Iron Phosphate (LiFePO4) Cathode Powder" originProvinceCN="Sichuan (SC)" massSharePct="42.0" criticalRawMaterial="YES - Lithium"/>
      <MaterialComponent componentName="Synthetic Graphite Anode Matrix" originProvinceCN="Inner Mongolia (NM)" massSharePct="24.5" criticalRawMaterial="YES - Natural/Synthetic Graphite"/>
      <MaterialComponent componentName="High-Purity Aluminum Battery Shell &amp; Foil" originProvinceCN="Henan (HA)" massSharePct="18.0" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Electrolytic Copper Foil Current Collector" originProvinceCN="Jiangxi (JX)" massSharePct="8.5" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Non-Aqueous Electrolyte (LiPF6 in EC/DMC)" originProvinceCN="Jiangsu (JS)" massSharePct="7.0" criticalRawMaterial="YES - Fluorine/Lithium"/>
    </BillOfMaterials>
  </TechnicalDossier>
  <TechnicalDossier productSkuCn="SKU-BYD-BLADE-01" manufacturerUscc="91440300192317458F" cccCertNo="2024011112345678">
    <EngineeringSpecs nominalVoltageV="570.0" ratedPowerKw="390.00" efficiencyPct="97.2" serviceLifeYears="12"/>
    <BillOfMaterials>
      <MaterialComponent componentName="Blade LFP Cell Pack Integration Matrix" originProvinceCN="Guangdong (GD)" massSharePct="48.0" criticalRawMaterial="YES - Lithium"/>
      <MaterialComponent componentName="High-Strength Aluminum Tray &amp; Upper Cover" originProvinceCN="Hubei (HB)" massSharePct="26.0" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Silicon Carbide (SiC) Power Inverter Modules" originProvinceCN="Shaanxi (SN)" massSharePct="14.0" criticalRawMaterial="YES - Silicon Carbide"/>
      <MaterialComponent componentName="Structural Aerogel Thermal Barrier" originProvinceCN="Jiangsu (JS)" massSharePct="12.0" criticalRawMaterial="NO"/>
    </BillOfMaterials>
  </TechnicalDossier>
  <TechnicalDossier productSkuCn="SKU-LONGI-HIMO7" manufacturerUscc="91610132724912345X" cccCertNo="2023010899112233">
    <EngineeringSpecs nominalVoltageV="43.8" ratedPowerKw="0.6100" efficiencyPct="22.8" serviceLifeYears="30"/>
    <BillOfMaterials>
      <MaterialComponent componentName="HPBC N-Type Monocrystalline Silicon Wafers" originProvinceCN="Shaanxi (SN)" massSharePct="28.5" criticalRawMaterial="YES - Polysilicon"/>
      <MaterialComponent componentName="Anti-Reflective Coated Solar Tempered Glass" originProvinceCN="Zhejiang (ZJ)" massSharePct="52.0" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Anodized Aluminum Structural Frame" originProvinceCN="Henan (HA)" massSharePct="12.5" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Silver Metallization Paste &amp; POE Encapsulant" originProvinceCN="Jiangsu (JS)" massSharePct="7.0" criticalRawMaterial="YES - Silver"/>
    </BillOfMaterials>
  </TechnicalDossier>
  <TechnicalDossier productSkuCn="SKU-CATL-ENERONE" manufacturerUscc="91350900587527783P" cccCertNo="2025010955667788">
    <EngineeringSpecs nominalVoltageV="896.0" ratedPowerKw="372.70" efficiencyPct="96.8" serviceLifeYears="20"/>
    <BillOfMaterials>
      <MaterialComponent componentName="LFP Long-Life Energy Storage Cells" originProvinceCN="Fujian (FJ)" massSharePct="54.0" criticalRawMaterial="YES - Lithium"/>
      <MaterialComponent componentName="Liquid Cooling Aluminum Plates &amp; BMS Board" originProvinceCN="Fujian (FJ)" massSharePct="21.0" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Galvanized High-Protection Steel Enclosure" originProvinceCN="Zhejiang (ZJ)" massSharePct="25.0" criticalRawMaterial="NO"/>
    </BillOfMaterials>
  </TechnicalDossier>
  <TechnicalDossier productSkuCn="SKU-HUAWEI-5G-AAU" manufacturerUscc="91440300618837699Q" cccCertNo="2024011666778899">
    <EngineeringSpecs nominalVoltageV="48.0" ratedPowerKw="1.4500" efficiencyPct="94.2" serviceLifeYears="10"/>
    <BillOfMaterials>
      <MaterialComponent componentName="Gallium Nitride (GaN) RF Power Amplifiers" originProvinceCN="Guangdong (GD)" massSharePct="16.5" criticalRawMaterial="YES - Gallium"/>
      <MaterialComponent componentName="Die-Cast Magnesium-Aluminum Heat Dissipator" originProvinceCN="Guangdong (GD)" massSharePct="58.0" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="High-Frequency Multilayer PTFE Antenna Substrate" originProvinceCN="Jiangsu (JS)" massSharePct="25.5" criticalRawMaterial="NO"/>
    </BillOfMaterials>
  </TechnicalDossier>
  <TechnicalDossier productSkuCn="SKU-STEEL-S355JR" manufacturerUscc="91330200778899112T" cccCertNo="2023010211223344">
    <EngineeringSpecs nominalVoltageV="0.0" ratedPowerKw="0.0000" efficiencyPct="100.0" serviceLifeYears="50"/>
    <BillOfMaterials>
      <MaterialComponent componentName="Hot-Rolled Structural Alloy Steel Melt" originProvinceCN="Zhejiang (ZJ)" massSharePct="97.5" criticalRawMaterial="NO"/>
      <MaterialComponent componentName="Manganese, Silicon and Niobium Micro-Alloys" originProvinceCN="Hebei (HE)" massSharePct="2.5" criticalRawMaterial="YES - Niobium/Manganese"/>
    </BillOfMaterials>
  </TechnicalDossier>
</ProductTechnicalDossiers>"""

    c61 = """<?xml version="1.0" encoding="utf-8"?>
<InternationalTradeFairsChina>
  <TradeFairEdition fairCode="CIIE-2025" fairName="China International Import Expo (CIIE)" hostCity="Shanghai" year="2025">
    <MatchmakingDeals>
      <Deal ptCompanyEori="PT500265432" cnCompanyUscc="91110000101123456N" contractNoGenerated="CNT-2025-CIIE-01" intentValueUSD="1450000.00" sector="Agroalimentar (Vinhos do Douro e Porto Sogrape)"/>
      <Deal ptCompanyEori="PT502345678" cnCompanyUscc="91610132724912345X" contractNoGenerated="CNT-2025-CIIE-02" intentValueUSD="8200000.00" sector="Energias Renováveis (Painéis Solares LONGi EDP)"/>
    </MatchmakingDeals>
  </TradeFairEdition>
  <TradeFairEdition fairCode="CANTON-138" fairName="Canton Fair / China Import and Export Fair" hostCity="Guangzhou" year="2025">
    <MatchmakingDeals>
      <Deal ptCompanyEori="PT500123456" cnCompanyUscc="91110108551385082Q" contractNoGenerated="CNT-2025-CANTON-03" intentValueUSD="3500000.00" sector="Eletrónica de Consumo (Xiaomi Sonae/Worten)"/>
      <Deal ptCompanyEori="PT500345678" cnCompanyUscc="91330782098765432W" contractNoGenerated="CNT-2025-CANTON-04" intentValueUSD="1200000.00" sector="Têxteis e Vestuário Polo Varziela"/>
    </MatchmakingDeals>
  </TradeFairEdition>
  <TradeFairEdition fairCode="MIF-2025" fairName="Macao International Trade and Investment Fair (MIF)" hostCity="Macao SAR" year="2025">
    <MatchmakingDeals>
      <Deal ptCompanyEori="PT500198765" cnCompanyUscc="91110000101123456N" contractNoGenerated="CNT-2025-MIF-05" intentValueUSD="980000.00" sector="Agroalimentar (Carne de Porco Congelada Maporal)"/>
      <Deal ptCompanyEori="PT500234567" cnCompanyUscc="91440400MA56LUS01P" contractNoGenerated="CNT-2025-MIF-06" intentValueUSD="4500000.00" sector="Plataforma de Financiamento Lusófono BCP Macau"/>
    </MatchmakingDeals>
  </TradeFairEdition>
  <TradeFairEdition fairCode="GDTE-2025" fairName="Global Digital Trade Expo (GDTE)" hostCity="Hangzhou" year="2025">
    <MatchmakingDeals>
      <Deal ptCompanyEori="PT500077568" cnCompanyUscc="91440300755673010C" contractNoGenerated="CNT-2025-GDTE-07" intentValueUSD="2800000.00" sector="Logística Digital Transfronteiriça CTT Cainiao"/>
    </MatchmakingDeals>
  </TradeFairEdition>
  <TradeFairEdition fairCode="WCIF-2025" fairName="Western China International Fair (WCIF)" hostCity="Chengdu" year="2025">
    <MatchmakingDeals>
      <Deal ptCompanyEori="PT517890123" cnCompanyUscc="91320413MA1M9Y2C4B" contractNoGenerated="CNT-2025-WCIF-08" intentValueUSD="6800000.00" sector="Componentes e Maquinaria Fabril Sines"/>
    </MatchmakingDeals>
  </TradeFairEdition>
</InternationalTradeFairsChina>"""

    c62 = """<?xml version="1.0" encoding="utf-8"?>
<MacaoLusophonePlatformRegistry>
  <LusophoneOperation operationId="OP-MACAO-LUSO-2026-01" forumMacaoProgram="MIF Bilateral Agribusiness Corridor">
    <TriangularParties macaoIntermediaryId="MO-BNU-LUSO-01" mainlandEnterpriseUscc="91110000101123456N" portugueseEnterpriseEori="PT500265432"/>
    <FinancialFacilitation serviceType="RMB Cross-Border Trade Settlement &amp; Escrow" clearingAmountCNY="28500000.00" equivalentEUR="3950000.00" linkedContractNo="CNT-PTCN-2026-AGRO-01"/>
  </LusophoneOperation>
  <LusophoneOperation operationId="OP-MACAO-LUSO-2026-02" forumMacaoProgram="Greater Bay Area Lusophone Energy Transition Fund">
    <TriangularParties macaoIntermediaryId="MO-BCP-MACAU-02" mainlandEnterpriseUscc="91320413MA1M9Y2C4B" portugueseEnterpriseEori="PT517890123"/>
    <FinancialFacilitation serviceType="Syndicated Green Loan Guarantee" clearingAmountCNY="120000000.00" equivalentEUR="16630000.00" linkedContractNo="CNT-PTCN-2026-EV-01"/>
  </LusophoneOperation>
  <LusophoneOperation operationId="OP-MACAO-LUSO-2026-03" forumMacaoProgram="Macao Traditional Chinese Medicine &amp; Health Park Hengqin">
    <TriangularParties macaoIntermediaryId="MO-CCAM-03" mainlandEnterpriseUscc="91440400MA56LUS01P" portugueseEnterpriseEori="PT500456789"/>
    <FinancialFacilitation serviceType="Pharmaceutical Certification Clearing" clearingAmountCNY="14800000.00" equivalentEUR="2050000.00" linkedContractNo="CNT-PTCN-2026-PHARMA-03"/>
  </LusophoneOperation>
  <LusophoneOperation operationId="OP-MACAO-LUSO-2026-04" forumMacaoProgram="Hengqin-Macao Cross-Border E-Commerce Zone">
    <TriangularParties macaoIntermediaryId="MO-BOC-MACAU-04" mainlandEnterpriseUscc="91330782098765432W" portugueseEnterpriseEori="PT500345678"/>
    <FinancialFacilitation serviceType="Cross-Border CIPS Fast Remittance" clearingAmountCNY="8200000.00" equivalentEUR="1136000.00" linkedContractNo="CNT-PTCN-2026-ECOM-04"/>
  </LusophoneOperation>
  <LusophoneOperation operationId="OP-MACAO-LUSO-2026-05" forumMacaoProgram="Forum Macao Infrastructure Cooperation Framework">
    <TriangularParties macaoIntermediaryId="MO-ICBC-MACAU-05" mainlandEnterpriseUscc="91110000100001146K" portugueseEnterpriseEori="PT502345678"/>
    <FinancialFacilitation serviceType="Project Finance Debt Structuring" clearingAmountCNY="95000000.00" equivalentEUR="13166000.00" linkedContractNo="CNT-PTCN-2026-GRID-05"/>
  </LusophoneOperation>
</MacaoLusophonePlatformRegistry>"""

    c63 = """<?xml version="1.0" encoding="utf-8"?>
<ChineseBondedWarehouses>
  <BondedWarehouse warehouseCodeGacc="WH-SHA-WGQ-01" ftzZoneCode="ZN-SH-PUDONG" city="Shanghai">
    <PortugueseImportedLots>
      <StoredLot lotId="LOT-SHA-2026-001" gaccImportId18="220120261000990001" ptProducerEori="PT500265432" ciferCode="CPRT18000102000101" hsCode10Cn="2204210000" productName="Sogrape Casa Ferreirinha Douro Tinto Reserva" unitsInStock="24000" dutySuspendedCNY="425000.00"/>
      <StoredLot lotId="LOT-SHA-2026-002" gaccImportId18="220120261000990004" ptProducerEori="PT500198765" ciferCode="CPRT02000103000202" hsCode10Cn="0203290000" productName="Maporal Frozen Pork Cuts (Costela Suína)" unitsInStock="50000" dutySuspendedCNY="280000.00"/>
    </PortugueseImportedLots>
  </BondedWarehouse>
  <BondedWarehouse warehouseCodeGacc="WH-NGB-MSH-02" ftzZoneCode="ZN-ZJ-NINGBO" city="Ningbo">
    <PortugueseImportedLots>
      <StoredLot lotId="LOT-NGB-2026-003" gaccImportId18="220120261000990003" ptProducerEori="PT500345678" ciferCode="CPRT47000105000303" hsCode10Cn="4703290000" productName="The Navigator Company Bleached Eucalyptus Kraft Pulp (BEKP)" unitsInStock="120000" dutySuspendedCNY="610000.00"/>
      <StoredLot lotId="LOT-NGB-2026-004" gaccImportId18="220120261000990005" ptProducerEori="PT500123999" ciferCode="CPRT45000106000404" hsCode10Cn="4504100000" productName="Corticeira Amorim Technical Wine Corks" unitsInStock="85000" dutySuspendedCNY="195000.00"/>
    </PortugueseImportedLots>
  </BondedWarehouse>
  <BondedWarehouse warehouseCodeGacc="WH-SZX-QT-03" ftzZoneCode="ZN-GD-QIANHAI" city="Shenzhen">
    <PortugueseImportedLots>
      <StoredLot lotId="LOT-SZX-2026-005" gaccImportId18="220120261000990002" ptProducerEori="PT500876543" ciferCode="CPRT15000104000505" hsCode10Cn="1509200000" productName="Sovena Oliveira da Serra Extra Virgin Olive Oil" unitsInStock="36000" dutySuspendedCNY="310000.00"/>
    </PortugueseImportedLots>
  </BondedWarehouse>
  <BondedWarehouse warehouseCodeGacc="WH-ZH-HQ-04" ftzZoneCode="ZN-GD-HENGQIN" city="Zhuhai">
    <PortugueseImportedLots>
      <StoredLot lotId="LOT-ZH-2026-006" gaccImportId18="220120261000990006" ptProducerEori="PT500987654" ciferCode="CPRT19000108000606" hsCode10Cn="1905310000" productName="Dan Cake Butter Cookies &amp; Traditional Biscuits" unitsInStock="18000" dutySuspendedCNY="92000.00"/>
    </PortugueseImportedLots>
  </BondedWarehouse>
  <BondedWarehouse warehouseCodeGacc="WH-CAN-NS-05" ftzZoneCode="ZN-GD-NANSHA" city="Guangzhou">
    <PortugueseImportedLots>
      <StoredLot lotId="LOT-CAN-2026-007" gaccImportId18="220120261000990007" ptProducerEori="PT500265432" ciferCode="CPRT18000102000101" hsCode10Cn="2204210000" productName="Sogrape Sandeman Porto Tawny 20 Anos" unitsInStock="12000" dutySuspendedCNY="340000.00"/>
    </PortugueseImportedLots>
  </BondedWarehouse>
</ChineseBondedWarehouses>"""

    c64 = """<?xml version="1.0" encoding="utf-8"?>
<ExportPackagingAndHazmatCertificates>
  <CertificateRecord certificateId="CERT-HZ-2026-001" blNumber="COSU6288991101" containerIso="COSU8001101">
    <ISPM15WoodFumigation ippcMarkCode="CN-32004-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="58"/>
    <HazmatIMDGDeclaration isDangerousGoods="true" unNumber="UN3480" imdgClass="Class 9 - Lithium Ion Batteries" un383LithiumTested="true"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Full Container Weighbridge" verifiedGrossMassKg="463800.00" weighingTerminal="Shanghai Yangshan Phase 4 Automated Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-HZ-2026-002" blNumber="COSU6288991102" containerIso="BYDU9002201">
    <ISPM15WoodFumigation ippcMarkCode="CN-44003-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="56"/>
    <HazmatIMDGDeclaration isDangerousGoods="true" unNumber="UN3171" imdgClass="Class 9 - Battery-Powered Vehicle" un383LithiumTested="true"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 2 - Certified Vehicle Axle Weight" verifiedGrossMassKg="895400.00" weighingTerminal="Shenzhen Yantian Ro-Ro Ramp Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-003" blNumber="COSU6288991103" containerIso="COSU8003301">
    <ISPM15WoodFumigation ippcMarkCode="CN-61001-HT" treatmentMethod="Kiln Dried &amp; Heat Treated (ISPM-15)" exposureTempC="60"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 2 - Certified Cargo + Tare" verifiedGrossMassKg="1714200.00" weighingTerminal="Xi'an Inland Port Consolidation Weighbridge"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-HZ-2026-004" blNumber="COSU6288991104" containerIso="CATU8004401">
    <ISPM15WoodFumigation ippcMarkCode="CN-35009-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="57"/>
    <HazmatIMDGDeclaration isDangerousGoods="true" unNumber="UN3480" imdgClass="Class 9 - Lithium Ion Batteries" un383LithiumTested="true"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Full Container Weighbridge" verifiedGrossMassKg="358900.00" weighingTerminal="Ningbo Meishan Terminal Scale 02"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-005" blNumber="047-88991105" containerIso="PMC44111CA">
    <ISPM15WoodFumigation ippcMarkCode="CN-11005-HT" treatmentMethod="Kiln Dried ISPM-15 Wooden Pallet" exposureTempC="59"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Class 9 - Consumer Lithium Under 100Wh Section II" un383LithiumTested="true"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Air Cargo Scale" verifiedGrossMassKg="2450.00" weighingTerminal="Hangzhou Xiaoshan Airport Cargo Terminal Scale 1"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-006" blNumber="COSU6288991106" containerIso="NBSU8006601">
    <ISPM15WoodFumigation ippcMarkCode="CN-33002-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="58"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Heavy Industrial Weighbridge" verifiedGrossMassKg="2110500.00" weighingTerminal="Ningbo Beilun Steel Logistics Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-007" blNumber="CIMSMGS-YW2026-07" containerIso="YIWU4007701">
    <ISPM15WoodFumigation ippcMarkCode="CN-33015-HT" treatmentMethod="Heat Treatment ISPM-15" exposureTempC="58"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 2 - Rail Container Scale" verifiedGrossMassKg="27300.00" weighingTerminal="Yiwu Railway West Port Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-008" blNumber="COSU6288991108" containerIso="HWU8008801">
    <ISPM15WoodFumigation ippcMarkCode="CN-44012-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="57"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Container Weighbridge" verifiedGrossMassKg="18450.00" weighingTerminal="Shenzhen Yantian Terminal 2 Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-010" blNumber="COSU6288991110" containerIso="MDU8010001">
    <ISPM15WoodFumigation ippcMarkCode="CN-44020-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="56"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Class 2.2 - Non-flammable Gas Charge R32" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Full Container Weighbridge" verifiedGrossMassKg="22600.00" weighingTerminal="Guangzhou Nansha Phase 4 Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-011" blNumber="COSU6288991111" containerIso="CRCU8011101">
    <ISPM15WoodFumigation ippcMarkCode="CN-11008-HT" treatmentMethod="Kiln Dried Timber Crating ISPM-15" exposureTempC="60"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Heavy Heavyweight Scale" verifiedGrossMassKg="29800.00" weighingTerminal="Tianjin Port Smart Terminal Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-012" blNumber="CIMSMGS-YW2026-12" containerIso="YIWU4012201">
    <ISPM15WoodFumigation ippcMarkCode="CN-33015-HT" treatmentMethod="Heat Treatment ISPM-15" exposureTempC="58"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 2 - Rail Container Scale" verifiedGrossMassKg="21800.00" weighingTerminal="Yiwu Railway West Port Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-HZ-2026-013" blNumber="COSU6288991113" containerIso="BYDU9013301">
    <ISPM15WoodFumigation ippcMarkCode="CN-44003-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="56"/>
    <HazmatIMDGDeclaration isDangerousGoods="true" unNumber="UN3171" imdgClass="Class 9 - Battery-Powered Vehicle" un383LithiumTested="true"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 2 - Certified Vehicle Axle Weight" verifiedGrossMassKg="762000.00" weighingTerminal="Shenzhen Yantian Ro-Ro Ramp Scale"/>
  </CertificateRecord>
  <CertificateRecord certificateId="CERT-PK-2026-014" blNumber="COSU6288991114" containerIso="TSU8014401">
    <ISPM15WoodFumigation ippcMarkCode="CN-32011-HT" treatmentMethod="Heat Treatment 56C 30min (ISPM-15)" exposureTempC="58"/>
    <HazmatIMDGDeclaration isDangerousGoods="false" unNumber="NON-HAZMAT" imdgClass="Not Applicable" un383LithiumTested="false"/>
    <SOLASVerifiedGrossMass vgmMethod="Method 1 - Container Weighbridge" verifiedGrossMassKg="1689000.00" weighingTerminal="Shanghai Yangshan Terminal Scale"/>
  </CertificateRecord>
</ExportPackagingAndHazmatCertificates>"""

    c109 = """<?xml version="1.0" encoding="utf-8"?>
<ContainerLoadPlansCLP>
  <ContainerLoadPlan clpDocumentId="CLP-SH-2026-8001101" containerIso="COSU8001101" masterBlNo="COSU6288991101" stuffingDate="2026-03-21">
    <StuffingDepot depotName="CALB Changzhou Bonded CFS &amp; Shanghai Yangshan Depot" portUnlocode="CNSHA" eSealRfidCode="ESEAL-GACC-SH8801A" containerTareKg="3800.00"/>
    <LoadedPallets>
      <PalletPosition slotPosition="TIER1-ROW01-LEFT" packingListId="PKL-CN-2026-8801" batchLotNo="LOT-CALB-2026-03A" grossWeightKg="230000.00"/>
      <PalletPosition slotPosition="TIER1-ROW02-RIGHT" packingListId="PKL-CN-2026-8801" batchLotNo="LOT-CALB-2026-03K" grossWeightKg="230000.00"/>
    </LoadedPallets>
  </ContainerLoadPlan>
  <ContainerLoadPlan clpDocumentId="CLP-SZ-2026-9002201" containerIso="BYDU9002201" masterBlNo="COSU6288991102" stuffingDate="2026-03-26">
    <StuffingDepot depotName="Shenzhen Yantian Ro-Ro &amp; Auto Container Yard" portUnlocode="CNSZX" eSealRfidCode="ESEAL-GACC-SZ8802B" containerTareKg="4200.00"/>
    <LoadedPallets>
      <PalletPosition slotPosition="DECK3-LANE04-RACK1" packingListId="PKL-CN-2026-8802" batchLotNo="LOT-BYD-2026-03B" grossWeightKg="890000.00"/>
    </LoadedPallets>
  </ContainerLoadPlan>
  <ContainerLoadPlan clpDocumentId="CLP-SH-2026-8003301" containerIso="COSU8003301" masterBlNo="COSU6288991103" stuffingDate="2026-04-03">
    <StuffingDepot depotName="Xi'an Inland Port &amp; Shanghai Waigaoqiao CFS" portUnlocode="CNSHA" eSealRfidCode="ESEAL-GACC-SH8803C" containerTareKg="3900.00"/>
    <LoadedPallets>
      <PalletPosition slotPosition="TIER1-FULL-BAY" packingListId="PKL-CN-2026-8803" batchLotNo="LOT-LONGI-2026-04A" grossWeightKg="1710000.00"/>
    </LoadedPallets>
  </ContainerLoadPlan>
  <ContainerLoadPlan clpDocumentId="CLP-NB-2026-8004401" containerIso="CATU8004401" masterBlNo="COSU6288991104" stuffingDate="2026-04-11">
    <StuffingDepot depotName="Ningbo Meishan Hazardous Cargo CFS Depot" portUnlocode="CNNGB" eSealRfidCode="ESEAL-GACC-NB8804D" containerTareKg="4100.00"/>
    <LoadedPallets>
      <PalletPosition slotPosition="RACK-CENTER-LOCKED" packingListId="PKL-CN-2026-8804" batchLotNo="LOT-CATL-2026-04B" grossWeightKg="355000.00"/>
    </LoadedPallets>
  </ContainerLoadPlan>
  <ContainerLoadPlan clpDocumentId="CLP-NB-2026-8006601" containerIso="COSU8006601" masterBlNo="COSU6288991106" stuffingDate="2026-04-19">
    <StuffingDepot depotName="Ningbo Beilun Heavy Metals Coil Terminal" portUnlocode="CNNGB" eSealRfidCode="ESEAL-GACC-NB8806F" containerTareKg="4000.00"/>
    <LoadedPallets>
      <PalletPosition slotPosition="FLATBED-CRADLE-01" packingListId="PKL-CN-2026-8806" batchLotNo="LOT-NBST-2026-04D" grossWeightKg="2010000.00"/>
    </LoadedPallets>
  </ContainerLoadPlan>
</ContainerLoadPlansCLP>"""

    c110 = """<?xml version="1.0" encoding="utf-8"?>
<HouseBillsOfLadingConsolidation>
  <HouseBillOfLading hblNumber="HBL-SINOTRANS-SH2601" linkedMasterBlNo="COSU6288991101" containerIso="COSU8001101" serviceMode="CY/CY FCL-Multiple-HBL">
    <NVOCCConsolidator nvoccId="BRK-CN-SINOTRANS-01" nvoccName="Sinotrans Limited Shanghai Branch" ptReceivingAgentEori="PT500991122"/>
    <LCLCargoDetails shipperUscc="91320413MA1M9Y2C4B" consigneeEoriPT="PT517890123" packagesCount="5000" grossWeightKg="460000.00" volumeCbm="340.00" freightCollectEUR="0.00"/>
  </HouseBillOfLading>
  <HouseBillOfLading hblNumber="HBL-SINOTRANS-SH2602" linkedMasterBlNo="COSU6288991101" containerIso="COSU8001102" serviceMode="CY/CY FCL-Multiple-HBL">
    <NVOCCConsolidator nvoccId="BRK-CN-SINOTRANS-01" nvoccName="Sinotrans Limited Shanghai Branch" ptReceivingAgentEori="PT500991122"/>
    <LCLCargoDetails shipperUscc="91320413MA1M9Y2C4B" consigneeEoriPT="PT517890123" packagesCount="5000" grossWeightKg="460000.00" volumeCbm="340.00" freightCollectEUR="0.00"/>
  </HouseBillOfLading>
  <HouseBillOfLading hblNumber="HBL-KN-SZ2603" linkedMasterBlNo="COSU6288991108" containerIso="HWU8008801" serviceMode="CFS/CFS LCL Consolidation">
    <NVOCCConsolidator nvoccId="BRK-CN-KUEHNE-SZ-03" nvoccName="Kuehne + Nagel Shenzhen NVOCC" ptReceivingAgentEori="PT501223344"/>
    <LCLCargoDetails shipperUscc="91440300618837699Q" consigneeEoriPT="PT500697256" packagesCount="800" grossWeightKg="78000.00" volumeCbm="192.00" freightCollectEUR="14500.00"/>
  </HouseBillOfLading>
  <HouseBillOfLading hblNumber="HBL-TIMEX-YW2604" linkedMasterBlNo="CIMSMGS-YW2026-07" containerIso="CRXU9988771" serviceMode="RAIL-LCL Yiwu-Entroncamento">
    <NVOCCConsolidator nvoccId="BRK-CN-YIWU-RAIL-05" nvoccName="Yiwu Timex BRI Rail NVOCC" ptReceivingAgentEori="PT504998877"/>
    <LCLCargoDetails shipperUscc="91330782098765432W" consigneeEoriPT="PT504998877" packagesCount="2500" grossWeightKg="124000.00" volumeCbm="450.00" freightCollectEUR="18200.00"/>
  </HouseBillOfLading>
  <HouseBillOfLading hblNumber="HBL-COSCO-NB2605" linkedMasterBlNo="COSU6288991104" containerIso="CATU8004401" serviceMode="CY/DOOR Project Cargo">
    <NVOCCConsolidator nvoccId="BRK-CN-COSCO-LOG-02" nvoccName="COSCO SHIPPING Logistics Ningbo" ptReceivingAgentEori="PT503412890"/>
    <LCLCargoDetails shipperUscc="91350900587527783P" consigneeEoriPT="PT503412890" packagesCount="100" grossWeightKg="355000.00" volumeCbm="540.00" freightCollectEUR="0.00"/>
  </HouseBillOfLading>
</HouseBillsOfLadingConsolidation>"""

    c111 = """<?xml version="1.0" encoding="utf-8"?>
<CrossBorderThreeStreamMatching>
  <ThreeStreamDeclaration gaccCbecInventoryNo="CBEC-9610-2026-SZ001" supervisionRegime="9610 - B2C Direct Export" matchingVerdict="THREE_STREAMS_MATCHED_CLEARED">
    <OrderStream platformOrderNo="AE-ORD-2026-998801" ecommercePlatform="AliExpress (Alibaba)" buyerNifHashPT="NIF-HASH-PT-2458891" orderAmountEUR="68.50"/>
    <PaymentStream paymentTxId="ALIPAY-EU-20260418-01" paymentInstitution="Alipay Europe / SIBS MBWay" iossVatCollectedEUR="15.76"/>
    <LogisticsStream s10TrackingNo="LP00667788901CN" airWaybillNo="871-33221100" lastMileCarrierPT="CTT Expresso Portugal"/>
  </ThreeStreamDeclaration>
  <ThreeStreamDeclaration gaccCbecInventoryNo="CBEC-9610-2026-SZ002" supervisionRegime="9610 - B2C Direct Export" matchingVerdict="THREE_STREAMS_MATCHED_CLEARED">
    <OrderStream platformOrderNo="AE-ORD-2026-998802" ecommercePlatform="AliExpress (Alibaba)" buyerNifHashPT="NIF-HASH-PT-2114450" orderAmountEUR="112.00"/>
    <PaymentStream paymentTxId="ALIPAY-EU-20260418-02" paymentInstitution="Alipay Europe / Visa" iossVatCollectedEUR="25.76"/>
    <LogisticsStream s10TrackingNo="LP00667788902CN" airWaybillNo="871-33221100" lastMileCarrierPT="CTT Expresso Portugal"/>
  </ThreeStreamDeclaration>
  <ThreeStreamDeclaration gaccCbecInventoryNo="CBEC-9610-2026-GZ005" supervisionRegime="9610 - B2C Direct Export" matchingVerdict="THREE_STREAMS_MATCHED_CLEARED">
    <OrderStream platformOrderNo="SHN-ORD-2026-774105" ecommercePlatform="SHEIN Distribution Hub" buyerNifHashPT="NIF-HASH-PT-2689912" orderAmountEUR="84.90"/>
    <PaymentStream paymentTxId="ADYEN-SHN-20260420-05" paymentInstitution="Adyen NV / Multibanco" iossVatCollectedEUR="19.53"/>
    <LogisticsStream s10TrackingNo="LP00667788905CN" airWaybillNo="871-33221100" lastMileCarrierPT="CTT Expresso Portugal"/>
  </ThreeStreamDeclaration>
  <ThreeStreamDeclaration gaccCbecInventoryNo="CBEC-9710-2026-YW009" supervisionRegime="9710 - Cross-Border E-Commerce B2B Direct" matchingVerdict="THREE_STREAMS_MATCHED_CLEARED">
    <OrderStream platformOrderNo="TEMU-ORD-2026-551209" ecommercePlatform="Temu Whaleco EU" buyerNifHashPT="NIF-HASH-PT-2901134" orderAmountEUR="49.20"/>
    <PaymentStream paymentTxId="STRIPE-TMU-20260422-09" paymentInstitution="Stripe Payments Europe" iossVatCollectedEUR="11.32"/>
    <LogisticsStream s10TrackingNo="LP00667788909CN" airWaybillNo="871-33221100" lastMileCarrierPT="CTT Expresso Portugal"/>
  </ThreeStreamDeclaration>
  <ThreeStreamDeclaration gaccCbecInventoryNo="CBEC-1210-2026-SH012" supervisionRegime="1210 - Bonded Cross-Border E-Commerce" matchingVerdict="THREE_STREAMS_MATCHED_CLEARED">
    <OrderStream platformOrderNo="TMALL-GLOBAL-2026-12" ecommercePlatform="Tmall Global / JD Worldwide" buyerNifHashPT="PT500265432" orderAmountEUR="142.00"/>
    <PaymentStream paymentTxId="WECHAT-PAY-20260425-12" paymentInstitution="Tenpay / WeChat Pay CN" iossVatCollectedEUR="32.66"/>
    <LogisticsStream s10TrackingNo="LP00667788912CN" airWaybillNo="871-33221100" lastMileCarrierPT="CTT Expresso Portugal"/>
  </ThreeStreamDeclaration>
</CrossBorderThreeStreamMatching>"""

    c112 = """<?xml version="1.0" encoding="utf-8"?>
<TerminalOperatingSystemEvents>
  <ContainerTOSEvent tosEventId="TOS-SHA-2026-001" terminalId="SHA-YS-P4" containerIso="COSU8001101" blNumber="COSU6288991101">
    <GateInCODECO gateTimestampCST="2026-03-21T14:22:10+08:00" truckPlateCN="苏D-88219新能源" yardBlockSlot="Y4-BLK-A12-04-03"/>
    <VesselLoadCOARRI loadTimestampCST="2026-03-23T21:15:44+08:00" stsCraneId="STS-YANGSHAN-408" stowageBayRowTier="BAY-034-ROW-06-TIER-82" vesselImo="9795610"/>
  </ContainerTOSEvent>
  <ContainerTOSEvent tosEventId="TOS-SZX-2026-002" terminalId="SZX-YT-T3" containerIso="BYDU9002201" blNumber="COSU6288991102">
    <GateInCODECO gateTimestampCST="2026-03-26T09:10:05+08:00" truckPlateCN="粤B-99102D" yardBlockSlot="YT-RORO-Z2-18"/>
    <VesselLoadCOARRI loadTimestampCST="2026-03-27T18:40:12+08:00" stsCraneId="RAMP-YANTIAN-R02" stowageBayRowTier="DECK-05-LANE-12-POS-04" vesselImo="9842105"/>
  </ContainerTOSEvent>
  <ContainerTOSEvent tosEventId="TOS-SHA-2026-003" terminalId="SHA-WGQ-T2" containerIso="COSU8003301" blNumber="COSU6288991103">
    <GateInCODECO gateTimestampCST="2026-04-03T11:05:30+08:00" truckPlateCN="沪A-55321挂" yardBlockSlot="WGQ-B08-11-02"/>
    <VesselLoadCOARRI loadTimestampCST="2026-04-04T23:50:00+08:00" stsCraneId="STS-WGQ-204" stowageBayRowTier="BAY-058-ROW-02-TIER-86" vesselImo="9795610"/>
  </ContainerTOSEvent>
  <ContainerTOSEvent tosEventId="TOS-NGB-2026-004" terminalId="NGB-MS-T2" containerIso="CATU8004401" blNumber="COSU6288991104">
    <GateInCODECO gateTimestampCST="2026-04-11T08:30:00+08:00" truckPlateCN="浙B-77412挂" yardBlockSlot="MS-DG-HAZ-03-01"/>
    <VesselLoadCOARRI loadTimestampCST="2026-04-12T19:20:33+08:00" stsCraneId="STS-MEISHAN-112" stowageBayRowTier="BAY-042-ROW-08-TIER-84" vesselImo="9839131"/>
  </ContainerTOSEvent>
  <ContainerTOSEvent tosEventId="TOS-NGB-2026-006" terminalId="NGB-BL-T3" containerIso="COSU8006601" blNumber="COSU6288991106">
    <GateInCODECO gateTimestampCST="2026-04-19T15:45:19+08:00" truckPlateCN="浙B-33109挂" yardBlockSlot="BL-HEAVY-C02-09"/>
    <VesselLoadCOARRI loadTimestampCST="2026-04-20T22:10:08+08:00" stsCraneId="STS-BEILUN-305" stowageBayRowTier="BAY-018-ROW-04-TIER-12" vesselImo="9839131"/>
  </ContainerTOSEvent>
</TerminalOperatingSystemEvents>"""

    c113 = """<?xml version="1.0" encoding="utf-8"?>
<MaritimeTransshipmentHubOperations>
  <TransshipmentOperation transshipmentId="TSH-SINES-LEIXOES-001" hubPortUnlocode="PTSIN" hubPortName="Port of Sines PSA Terminal XXI (Feeder Relay)" containerIso="CATU8004401" blNumber="COSU6288991104">
    <InboundMotherVessel vesselName="COSCO SHIPPING SOLAR" vesselImo="9839131" dischargeDateUTC="2026-05-14"/>
    <OutboundFeederVessel feederName="PORTUGAL FEEDER EXPRESS" feederImo="9451123" reloadDateUTC="2026-05-16" finalDestinationPortPT="PTLEI"/>
  </TransshipmentOperation>
  <TransshipmentOperation transshipmentId="TSH-TANGER-LEIXOES-002" hubPortUnlocode="MAPTM" hubPortName="Tanger-Med Port Complex APM Terminals" containerIso="COSU4455661" blNumber="COSU6288992201">
    <InboundMotherVessel vesselName="IBERIA ATLANTIC FEEDER" vesselImo="9388210" dischargeDateUTC="2026-04-09"/>
    <OutboundFeederVessel feederName="COSCO SHIPPING SOLAR" feederImo="9839131" reloadDateUTC="2026-04-11" finalDestinationPortPT="CNSHA"/>
  </TransshipmentOperation>
  <TransshipmentOperation transshipmentId="TSH-SINGAPORE-SINES-003" hubPortUnlocode="SGSIN" hubPortName="PSA Singapore Tuas Mega Port Hub" containerIso="COSU8001101" blNumber="COSU6288991101">
    <InboundMotherVessel vesselName="COSCO SHIPPING UNIVERSE" vesselImo="9795610" dischargeDateUTC="2026-03-30"/>
    <OutboundFeederVessel feederName="COSCO SHIPPING UNIVERSE" feederImo="9795610" reloadDateUTC="2026-03-31" finalDestinationPortPT="PTSIN"/>
  </TransshipmentOperation>
  <TransshipmentOperation transshipmentId="TSH-ALGECIRAS-LEIXOES-004" hubPortUnlocode="ESALG" hubPortName="Port of Algeciras TTIA Hub" containerIso="COSU4455662" blNumber="COSU6288992202">
    <InboundMotherVessel vesselName="LUSITANIA COASTAL FEEDER" vesselImo="9412234" dischargeDateUTC="2026-04-15"/>
    <OutboundFeederVessel feederName="COSCO SHIPPING PISCES" feederImo="9795634" reloadDateUTC="2026-04-17" finalDestinationPortPT="CNSHA"/>
  </TransshipmentOperation>
  <TransshipmentOperation transshipmentId="TSH-SINES-SETUBAL-005" hubPortUnlocode="PTSIN" hubPortName="Port of Sines Terminal XXI" containerIso="HWU8008801" blNumber="COSU6288991108">
    <InboundMotherVessel vesselName="COSCO SHIPPING TAURUS" vesselImo="9795646" dischargeDateUTC="2026-05-28"/>
    <OutboundFeederVessel feederName="SADO CONTAINER SHUTTLE" feederImo="9521108" reloadDateUTC="2026-05-29" finalDestinationPortPT="PTSIN"/>
  </TransshipmentOperation>
</MaritimeTransshipmentHubOperations>"""

    c114 = """<?xml version="1.0" encoding="utf-8"?>
<ContainerEquipmentDemurrageRegistry>
  <EquipmentDemurrageRecord eirRecordId="EIR-SH-2026-990005" containerIso="COSU4455665" blNumber="COSU6288992205" portUnlocode="CNSHA">
    <FreeTimeAllowance freeDemurrageDays="7" freeDetentionDays="7" actualTurnaroundDays="11"/>
    <PenaltySettlement chargeableOverdueDays="4" dailyRateUSD="145.00" totalBilledUSD="580.00" delayReason="CIQ Mandarin Back-Label Font Rectification in Bonded Cold Storage"/>
  </EquipmentDemurrageRecord>
  <EquipmentDemurrageRecord eirRecordId="EIR-SIN-2026-880101" containerIso="COSU8001101" blNumber="COSU6288991101" portUnlocode="PTSIN">
    <FreeTimeAllowance freeDemurrageDays="10" freeDetentionDays="14" actualTurnaroundDays="4"/>
    <PenaltySettlement chargeableOverdueDays="0" dailyRateUSD="95.00" totalBilledUSD="0.00" delayReason="Cleared Within Free Time - AEO Green Lane Release"/>
  </EquipmentDemurrageRecord>
  <EquipmentDemurrageRecord eirRecordId="EIR-LEI-2026-880401" containerIso="CATU8004401" blNumber="COSU6288991104" portUnlocode="PTLEI">
    <FreeTimeAllowance freeDemurrageDays="7" freeDetentionDays="10" actualTurnaroundDays="10"/>
    <PenaltySettlement chargeableOverdueDays="3" dailyRateUSD="120.00" totalBilledUSD="360.00" delayReason="Joint Insurance &amp; Port Authority Physical Survey After Bay of Biscay Storm"/>
  </EquipmentDemurrageRecord>
  <EquipmentDemurrageRecord eirRecordId="EIR-SH-2026-990001" containerIso="COSU4455661" blNumber="COSU6288992201" portUnlocode="CNSHA">
    <FreeTimeAllowance freeDemurrageDays="7" freeDetentionDays="7" actualTurnaroundDays="9"/>
    <PenaltySettlement chargeableOverdueDays="2" dailyRateUSD="145.00" totalBilledUSD="290.00" delayReason="CIQ Organoleptic Wine Sampling Due to Cape of Good Hope Thermal Excursion"/>
  </EquipmentDemurrageRecord>
  <EquipmentDemurrageRecord eirRecordId="EIR-SIN-2026-880601" containerIso="COSU8006601" blNumber="COSU6288991106" portUnlocode="PTSIN">
    <FreeTimeAllowance freeDemurrageDays="10" freeDetentionDays="10" actualTurnaroundDays="6"/>
    <PenaltySettlement chargeableOverdueDays="0" dailyRateUSD="85.00" totalBilledUSD="0.00" delayReason="Direct Rail Evacuation to Sines ZILS Construction Site"/>
  </EquipmentDemurrageRecord>
</ContainerEquipmentDemurrageRegistry>"""

    c115 = """<?xml version="1.0" encoding="utf-8"?>
<CrossBorderReverseLogisticsReturns>
  <BondedReturnCase returnCaseId="RET-CBEC-2026-001" gaccReturnRegime="9610R - Cross-Border E-Commerce Export Return" returnDate="2026-05-18">
    <ReturnOriginPT originalExportOrS10Ref="LP00667788903CN" ptSenderEoriOrPostal="4000-120" returnReasonCode="CONSUMER_SIZE_EXCHANGE_14DAYS"/>
    <BondedWarehouseDisposition bondedZoneCode="CN-GD-QIANHAI" dispositionAction="Restocked in Cainiao Shenzhen Bonded Return Hub" dutyRefundOrCreditCNY="0.00"/>
  </BondedReturnCase>
  <BondedReturnCase returnCaseId="RET-CBEC-2026-002" gaccReturnRegime="9610R - Cross-Border E-Commerce Export Return" returnDate="2026-05-22">
    <ReturnOriginPT originalExportOrS10Ref="LP00667788907CN" ptSenderEoriOrPostal="1100-050" returnReasonCode="DEFECTIVE_DISPLAY_WARRANTY"/>
    <BondedWarehouseDisposition bondedZoneCode="CN-ZJ-HANGZHOU-CROSS" dispositionAction="Returned to Manufacturer Repair Center Under Bond" dutyRefundOrCreditCNY="420.00"/>
  </BondedReturnCase>
  <BondedReturnCase returnCaseId="RET-B2B-2026-003" gaccReturnRegime="4561 - Return of Exported Goods for Repair" returnDate="2026-05-29">
    <ReturnOriginPT originalExportOrS10Ref="COSU6288991108" ptSenderEoriOrPostal="PT500697256" returnReasonCode="FIRMWARE_CALIBRATION_REPLACEMENT"/>
    <BondedWarehouseDisposition bondedZoneCode="CN-GD-QIANHAI" dispositionAction="Huawei Songshan Lake Bonded RMA Replacement" dutyRefundOrCreditCNY="18500.00"/>
  </BondedReturnCase>
  <BondedReturnCase returnCaseId="RET-CBEC-2026-004" gaccReturnRegime="1210R - Bonded E-Commerce Return" returnDate="2026-06-03">
    <ReturnOriginPT originalExportOrS10Ref="LP00667788911CN" ptSenderEoriOrPostal="3000-210" returnReasonCode="UNCLAIMED_PARCEL_AT_CTT_LOCKER"/>
    <BondedWarehouseDisposition bondedZoneCode="CN-ZJ-YIWU-CBEC" dispositionAction="Consolidated Air Return via Cainiao Charter" dutyRefundOrCreditCNY="0.00"/>
  </BondedReturnCase>
  <BondedReturnCase returnCaseId="RET-B2B-2026-005" gaccReturnRegime="4561 - Return of Reusable Battery Skids" returnDate="2026-06-08">
    <ReturnOriginPT originalExportOrS10Ref="COSU6288991101" ptSenderEoriOrPostal="PT517890123" returnReasonCode="REUSABLE_STEEL_BATTERY_RACK_RETURN"/>
    <BondedWarehouseDisposition bondedZoneCode="CN-JS-CHANGZHOU-HI" dispositionAction="Cleaned and Re-entered into CALB Changzhou Loop" dutyRefundOrCreditCNY="64000.00"/>
  </BondedReturnCase>
</CrossBorderReverseLogisticsReturns>"""

    c116 = """<?xml version="1.0" encoding="utf-8"?>
<ColdChainSanitaryTraceabilityRegistry>
  <ColdChainTraceabilityLot traceCodeGacc="GACC-TRACE-SH-2026-9901" gaccImportId18="220120261000990001" ciferProducerCodePT="CPRT18000102000101" containerIso="COSU4455661">
    <PortSanitaryInspection entryPortCN="CNSHA" eciqCertNo="ECIQ-IM20260505101" coreTempMeasuredC="14.5" sanitaryDisinfectionPass="true"/>
    <DomesticDistributionChain coldStorageFacility="COFCO Shanghai Waigaoqiao Constant-Temp Wine Cellar" retailTraceabilityQrPrefix="QR-SHFDA-SYM-2026" destinationProvinceCN="Shanghai / Jiangsu"/>
  </ColdChainTraceabilityLot>
  <ColdChainTraceabilityLot traceCodeGacc="GACC-TRACE-SH-2026-9905" gaccImportId18="220120261000990005" ciferProducerCodePT="CPRT18000101000505" containerIso="COSU4455665">
    <PortSanitaryInspection entryPortCN="CNSHA" eciqCertNo="ECIQ-IM20260527105" coreTempMeasuredC="-18.1" sanitaryDisinfectionPass="true"/>
    <DomesticDistributionChain coldStorageFacility="Shanghai Pudong Cold-Chain Meat Logistics Hub" retailTraceabilityQrPrefix="QR-SHFDA-MAP-2026" destinationProvinceCN="Shanghai / Zhejiang"/>
  </ColdChainTraceabilityLot>
  <ColdChainTraceabilityLot traceCodeGacc="GACC-TRACE-HQ-2026-9903" gaccImportId18="530420261000990003" ciferProducerCodePT="CPRT18000401000303" containerIso="COSU4455663">
    <PortSanitaryInspection entryPortCN="CNZUH" eciqCertNo="ECIQ-IM20260519103" coreTempMeasuredC="16.2" sanitaryDisinfectionPass="true"/>
    <DomesticDistributionChain coldStorageFacility="Hengqin Lusophone Foodstuff Bonded Distribution Center" retailTraceabilityQrPrefix="QR-GDFDA-SOV-2026" destinationProvinceCN="Guangdong / Macao SAR"/>
  </ColdChainTraceabilityLot>
  <ColdChainTraceabilityLot traceCodeGacc="GACC-TRACE-SH-2026-9906" gaccImportId18="220120261000990006" ciferProducerCodePT="CPRT18000102000606" containerIso="COSU4455666">
    <PortSanitaryInspection entryPortCN="CNSHA" eciqCertNo="ECIQ-IM20260529106" coreTempMeasuredC="14.0" sanitaryDisinfectionPass="true"/>
    <DomesticDistributionChain coldStorageFacility="COFCO Shanghai Waigaoqiao Constant-Temp Wine Cellar" retailTraceabilityQrPrefix="QR-SHFDA-SOG-2026" destinationProvinceCN="Beijing / Shanghai"/>
  </ColdChainTraceabilityLot>
  <ColdChainTraceabilityLot traceCodeGacc="GACC-TRACE-QD-2026-9910" gaccImportId18="370220261000990010" ciferProducerCodePT="CPRT18000201000505" containerIso="COSU4455665">
    <PortSanitaryInspection entryPortCN="CNTAO" eciqCertNo="ECIQ-IM20260527105" coreTempMeasuredC="-18.3" sanitaryDisinfectionPass="true"/>
    <DomesticDistributionChain coldStorageFacility="Qingdao Qianwan Cold-Chain Port Hub" retailTraceabilityQrPrefix="QR-SDFDA-PORK-2026" destinationProvinceCN="Shandong / Hebei"/>
  </ColdChainTraceabilityLot>
</ColdChainSanitaryTraceabilityRegistry>"""

    return {
        "53_cn_seaports_terminals_xml.xml": c53,
        "54_cn_maritime_vessels_voyages_xml.xml": c54,
        "55_cn_master_bills_of_lading_xml.xml": c55,
        "56_cn_bri_railway_consignments_xml.xml": c56,
        "57_cn_air_cargo_manifests_xml.xml": c57,
        "58_cn_cross_border_ecommerce_parcels_xml.xml": c58,
        "59_cn_smart_containers_iot_telemetry_xml.xml": c59,
        "60_cn_b2b_supplier_product_specs_xml.xml": c60,
        "61_cn_trade_fairs_exhibitions_b2b_xml.xml": c61,
        "62_cn_macao_lusophone_platform_deals_xml.xml": c62,
        "63_cn_bonded_warehouse_inventories_xml.xml": c63,
        "64_cn_export_packaging_fumigation_certs_xml.xml": c64,
        "109_cn_container_stuffing_load_plans_clp_xml.xml": c109,
        "110_cn_house_bills_of_lading_hbl_consolidation_xml.xml": c110,
        "111_cn_cbec_three_stream_matching_9610_1210_xml.xml": c111,
        "112_cn_port_terminal_gate_events_tos_xml.xml": c112,
        "113_cn_maritime_transshipment_hub_events_xml.xml": c113,
        "114_cn_demurrage_detention_container_equipment_xml.xml": c114,
        "115_cn_reverse_logistics_bonded_returns_xml.xml": c115,
        "116_cn_cold_chain_sanitary_traceability_codes_xml.xml": c116
    }
