#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full dataset for David Rodrigues (China Industrial, Customs & Logistics - Source D1: 20 SQL tables in 3NF).
Every tuple strictly satisfies all CHECK constraints, NOT NULL constraints, column counts,
and Foreign Key integrity to Afonso Bitoque's Portuguese data.
"""

def get_sql_data():
    data = {}

    # -------------------------------------------------------------------------
    # 33. cn_provinces_prefectures_cities (18 Provinces & Cities)
    # -------------------------------------------------------------------------
    data["provinces"] = [
        ("310000", "Shanghai Municipality", "上海市", "Shanghai", "Yangtze River Delta", 4721.87, 14.20, 14820.00),
        ("440300", "Guangdong Province", "广东省深圳市", "Shenzhen", "Pearl River Delta / Greater Bay Area", 3460.64, 18.50, 14250.00),
        ("440100", "Guangdong Province", "广东省广州市", "Guangzhou", "Pearl River Delta / Greater Bay Area", 3035.57, 11.40, 12680.00),
        ("440400", "Guangdong Province", "广东省珠海市", "Zhuhai (Hengqin)", "Pearl River Delta / Greater Bay Area", 423.32, 4.10, 11950.00),
        ("440600", "Guangdong Province", "广东省佛山市", "Foshan (Shunde)", "Pearl River Delta / Greater Bay Area", 1268.45, 9.50, 11800.00),
        ("330200", "Zhejiang Province", "浙江省宁波市", "Ningbo", "Yangtze River Delta", 1645.28, 9.80, 12300.00),
        ("330100", "Zhejiang Province", "浙江省杭州市", "Hangzhou", "Yangtze River Delta", 2005.90, 12.40, 13100.00),
        ("330782", "Zhejiang Province", "浙江省义乌市", "Yiwu (Jinhua)", "Yangtze River Delta", 205.56, 7.60, 10850.00),
        ("320400", "Jiangsu Province", "江苏省常州市", "Changzhou", "Yangtze River Delta", 1011.64, 8.20, 11900.00),
        ("320100", "Jiangsu Province", "江苏省南京市", "Nanjing", "Yangtze River Delta", 1742.14, 9.40, 12850.00),
        ("320500", "Jiangsu Province", "江苏省苏州市", "Suzhou", "Yangtze River Delta", 2465.34, 12.80, 13600.00),
        ("350900", "Fujian Province", "福建省宁德市", "Ningde", "Pearl River Delta / Greater Bay Area", 380.73, 5.40, 10900.00),
        ("350200", "Fujian Province", "福建省厦门市", "Xiamen", "Pearl River Delta / Greater Bay Area", 806.64, 5.30, 11750.00),
        ("610100", "Shaanxi Province", "陕西省西安市", "Xi'an", "Western China", 1201.08, 4.50, 10200.00),
        ("370200", "Shandong Province", "山东省青岛市", "Qingdao", "Bohai Economic Rim", 1576.03, 6.70, 11100.00),
        ("110000", "Beijing Municipality", "北京市", "Beijing", "Bohai Economic Rim", 4376.07, 5.80, 15400.00),
        ("120000", "Tianjin Municipality", "天津市", "Tianjin", "Bohai Economic Rim", 1673.72, 7.20, 11600.00),
        ("820000", "Macao SAR", "澳门特别行政区", "Macao", "Special Administrative Region", 345.40, 3.80, 18500.00),
    ]

    # -------------------------------------------------------------------------
    # 34. cn_special_economic_ftz_zones (12 FTZ & Pilot Zones)
    # -------------------------------------------------------------------------
    data["zones"] = [
        (1, "CN-SH-WAIGAOQIAO", "Shanghai Waigaoqiao Free Trade Zone", "310000", "Pilot FTZ", 15.00, 2.00, "2013-09-29"),
        (2, "CN-GD-QIANHAI", "Shenzhen Qianhai Shekou Pilot FTZ", "440300", "Special Economic Zone", 15.00, 1.50, "2015-04-27"),
        (3, "CN-GD-HENGQIN-MO", "Hengqin Guangdong-Macao In-Depth Cooperation Zone", "440400", "Lusophone In-Depth Cooperation Zone", 15.00, 3.00, "2021-09-17"),
        (4, "CN-ZJ-NINGBO-CBZ", "Ningbo Meishan Comprehensive Bonded Zone", "330200", "Comprehensive Bonded Zone", 20.00, 2.00, "2010-02-24"),
        (5, "CN-ZJ-YIWU-CBEC", "Yiwu Cross-Border E-Commerce Comprehensive Pilot Zone", "330782", "Cross-Border E-Commerce Pilot Zone", 15.00, 4.00, "2018-07-24"),
        (6, "CN-JS-CHANGZHOU-HI", "Changzhou National High-Tech Industrial Zone (New Energy)", "320400", "Pilot FTZ", 15.00, 2.50, "2015-01-15"),
        (7, "CN-FJ-NINGDE-BATT", "Ningde Lithium-Ion Battery Special Industrial Zone", "350900", "Special Economic Zone", 15.00, 2.50, "2017-06-01"),
        (8, "CN-SN-XIAN-LANDPORT", "Xi'an International Inland Port Bonded Zone (BRI Rail)", "610100", "Comprehensive Bonded Zone", 15.00, 2.00, "2014-03-12"),
        (9, "CN-GD-NANSHA-CBZ", "Guangzhou Nansha Comprehensive Bonded Zone", "440100", "Comprehensive Bonded Zone", 15.00, 2.00, "2020-07-15"),
        (10, "CN-SD-QINGDAO-FTZ", "Qingdao Qianwan Comprehensive Bonded Zone", "370200", "Comprehensive Bonded Zone", 15.00, 2.00, "2019-08-30"),
        (11, "CN-TJ-DONGLI-CBZ", "Tianjin Port Free Trade Zone (Airport Logistics)", "120000", "Pilot FTZ", 15.00, 2.00, "2015-04-21"),
        (12, "CN-ZJ-HANGZHOU-CROSS", "Hangzhou Cross-Border E-Commerce Comprehensive Pilot Area", "330100", "Cross-Border E-Commerce Pilot Zone", 15.00, 3.50, "2015-03-07"),
    ]

    # -------------------------------------------------------------------------
    # 35. cn_enterprises_manufacturers (22 Chinese Industrial & Logistics Leaders)
    # -------------------------------------------------------------------------
    data["enterprises"] = [
        ("91320413MA1M9Y2C4B", "3204960012", "CALB Group Co., Ltd. (China Aviation Lithium Battery)", "中创新航科技集团股份有限公司", "Publicly Listed Tech Giant", "C384", "320400", 6, 177255.00, "Advanced Certified AEO", "2015-12-08"),
        ("91440300192317458F", "4403160088", "BYD Auto Industry Company Limited", "比亚迪汽车工业有限公司", "Publicly Listed Tech Giant", "C361", "440300", 2, 375800.00, "Advanced Certified AEO", "2006-08-03"),
        ("91350900587527783P", "3509960001", "Contemporary Amperex Technology Co., Limited (CATL)", "宁德时代新能源科技股份有限公司", "Publicly Listed Tech Giant", "C384", "350900", 7, 439800.00, "Advanced Certified AEO", "2011-12-16"),
        ("91610132724912345X", "6101960022", "LONGi Green Energy Technology Co., Ltd.", "隆基绿能科技股份有限公司", "Publicly Listed Tech Giant", "C382", "610100", 8, 758200.00, "Advanced Certified AEO", "2000-02-14"),
        ("91440300618837699Q", "4403960001", "Huawei Technologies Co., Ltd. (Solar & Digital Power)", "华为技术有限公司", "Private Domestic", "C396", "440300", 2, 4084110.00, "Advanced Certified AEO", "1987-09-15"),
        ("91110108551385082Q", "1108960055", "Xiaomi Communications Co., Ltd.", "小米通讯技术有限公司", "Publicly Listed Tech Giant", "C397", "110000", 1, 320000.00, "Advanced Certified AEO", "2010-08-25"),
        ("91330782098765432W", "3307960088", "Zhejiang China Commodities City Group (Yiwu CCCG)", "浙江中国小商品城集团股份有限公司", "SOE - State-Owned Enterprise", "F513", "330782", 5, 548600.00, "Advanced Certified AEO", "1993-12-28"),
        ("91330200778899112T", "3302960077", "Ningbo Iron & Steel Co., Ltd. (Hanggang Group)", "宁波钢铁有限公司", "SOE - State-Owned Enterprise", "C312", "330200", 4, 1180000.00, "General Certified AEO", "2003-02-18"),
        ("91110000101123456N", "1101960010", "COFCO Corporation (China National Cereals, Oils & Foodstuffs)", "中粮集团有限公司", "SOE - State-Owned Enterprise", "F512", "110000", 1, 1195500.00, "Advanced Certified AEO", "1983-07-06"),
        ("91440400MA56LUS01P", "4404960056", "Guangdong-Macao Traditional Chinese Medicine & Lusophone Park", "粤澳合作中医药科技产业园开发有限公司", "SOE - State-Owned Enterprise", "M731", "440400", 3, 250000.00, "General Certified AEO", "2011-11-28"),
        ("91310000132209876M", "3100960002", "COSCO SHIPPING Lines Co., Ltd.", "中远海运集装箱运输有限公司", "SOE - State-Owned Enterprise", "G551", "310000", 1, 2366000.00, "Advanced Certified AEO", "1997-11-11"),
        ("91110000100001146K", "1101960088", "China Three Gorges Corporation (CTG - EDP Strategic Partner)", "中国长江三峡集团有限公司", "SOE - State-Owned Enterprise", "D441", "110000", 1, 21150000.00, "Advanced Certified AEO", "1993-09-27"),
        ("91110000710931234R", "1101960099", "State Grid Corporation of China (SGCC - REN Stakeholder)", "国家电网有限公司", "SOE - State-Owned Enterprise", "D442", "110000", 1, 82950000.00, "Advanced Certified AEO", "2002-12-29"),
        ("91310000132234561L", "3100960005", "Fosun International Limited (Fidelidade & BCP Investor)", "复星国际有限公司", "Private Domestic", "L721", "310000", 1, 895000.00, "Advanced Certified AEO", "1992-11-06"),
        ("91320400608131370B", "3204960033", "Trina Solar Co., Ltd.", "天合光能股份有限公司", "Publicly Listed Tech Giant", "C382", "320400", 6, 217300.00, "Advanced Certified AEO", "1997-12-26"),
        ("91440606190342599T", "4406960021", "Midea Group Co., Ltd.", "美的集团股份有限公司", "Publicly Listed Tech Giant", "C385", "440600", 2, 701500.00, "Advanced Certified AEO", "2000-04-07"),
        ("91440400192548256N", "4404960011", "Gree Electric Appliances, Inc. of Zhuhai", "珠海格力电器股份有限公司", "Publicly Listed Tech Giant", "C385", "440400", 3, 563100.00, "Advanced Certified AEO", "1989-12-13"),
        ("91370200163562681G", "3702960015", "Haier Smart Home Co., Ltd.", "海尔智家股份有限公司", "Publicly Listed Tech Giant", "C385", "370200", 10, 943800.00, "Advanced Certified AEO", "1994-03-29"),
        ("911100007178071858", "1101960066", "CRRC Corporation Limited (Rolling Stock & Metro Cars)", "中国中车股份有限公司", "SOE - State-Owned Enterprise", "C371", "110000", 1, 2869800.00, "Advanced Certified AEO", "2007-12-28"),
        ("91440300755673010C", "4403960044", "Cainiao Smart Logistics Network (Shenzhen Hub)", "深圳市菜鸟供应链管理有限公司", "Private Domestic", "G599", "440300", 2, 100000.00, "Advanced Certified AEO", "2013-05-28"),
        ("91330100716105852F", "3301960018", "Alibaba (China) Technology Co., Ltd. (AliExpress)", "阿里巴巴（中国）网络技术有限公司", "Publicly Listed Tech Giant", "I642", "330100", 12, 1530000.00, "Advanced Certified AEO", "1999-09-09"),
        ("91120000103061234K", "1201960005", "Tianjin Port (Group) Co., Ltd.", "天津港（集团）有限公司", "SOE - State-Owned Enterprise", "G551", "120000", 11, 1420000.00, "Advanced Certified AEO", "1992-10-18"),
    ]

    # -------------------------------------------------------------------------
    # 36. cn_factory_production_facilities (16 Industrial Facilities)
    # -------------------------------------------------------------------------
    data["facilities"] = [
        (101, "91320413MA1M9Y2C4B", "CALB Changzhou Jintan Zero-Carbon Battery Base", "320400", 31.724500, 119.582100, 480000, 6200, 35000000, 1, 1, None, 0.3120),
        (102, "91440300192317458F", "BYD Shenzhen Pingshan New Energy Vehicle MegaPlant", "440300", 22.691200, 114.354100, 1120000, 18500, 500000, 1, 1, None, 0.3850),
        (103, "91350900587527783P", "CATL Ningde Zhangwan Lighthouse Battery Plant", "350900", 26.685300, 119.547800, 890000, 14200, 60000000, 1, 1, None, 0.2750),
        (104, "91610132724912345X", "LONGi Xi'an Jingwei Hi-MO Solar Module Factory", "610100", 34.432100, 108.973200, 410000, 5400, 18000000, 1, 1, None, 0.4410),
        (105, "91440300618837699Q", "Huawei Dongguan Songshan Lake Smart5G & Inverter Campus", "440300", 22.923100, 113.889100, 650000, 9800, 12000000, 1, 1, None, 0.3510),
        (106, "91110108551385082Q", "Xiaomi Beijing Changping Dark Smart Factory", "110000", 40.112500, 116.298100, 81000, 1100, 10000000, 1, 1, None, 0.3980),
        (107, "91330782098765432W", "Yiwu Futian Consumer Goods Consolidation & Textile Mill", "330782", 29.321400, 120.098200, 260000, 3100, 95000000, 1, 0, None, 0.5120),
        (108, "91330200778899112T", "Ningbo Beilun Special Structural Steel & Aluminum Smelter", "330200", 29.912300, 121.845200, 540000, 4300, 1200000, 1, 1, None, 0.6480),
        (109, "91110000101123456N", "COFCO Shanghai Waigaoqiao Bonded Cold-Chain Wine Hub", "310000", 31.341200, 121.589100, 95000, 420, 45000000, 1, 1, "CNSH001928374", 0.3600),
        (110, "91320400608131370B", "Trina Solar Changzhou Photovoltaic Cell Gigafactory", "320400", 31.812300, 119.982100, 350000, 4800, 25000000, 1, 1, None, 0.3250),
        (111, "91440606190342599T", "Midea Shunde Smart Home & Heat Pump HVAC Plant", "440600", 22.812300, 113.245100, 520000, 7500, 15000000, 1, 1, None, 0.3450),
        (112, "91440400192548256N", "Gree Zhuhai Qianshan Inverter & AC Base", "440400", 22.251200, 113.512400, 480000, 6800, 14000000, 1, 1, None, 0.3520),
        (113, "91370200163562681G", "Haier Qingdao Sino-German EcoPark Smart Appliance Base", "370200", 36.012300, 120.182300, 420000, 5100, 8000000, 1, 1, None, 0.3180),
        (114, "911100007178071858", "CRRC Qingdao Sifang High-Speed & Metro Rolling Stock Plant", "370200", 36.182400, 120.354100, 780000, 8900, 1500, 1, 1, None, 0.4200),
        (115, "91440300755673010C", "Cainiao Shenzhen Airport International Cross-Border Gateway", "440300", 22.632100, 113.812400, 180000, 1900, 120000000, 1, 1, None, 0.3300),
        (116, "91440400MA56LUS01P", "Hengqin Sino-Lusophone GMP Bio-Pharmaceutical Base", "440400", 22.141200, 113.541200, 120000, 850, 5000000, 1, 1, "CNGD008819283", 0.2900),
    ]

    # -------------------------------------------------------------------------
    # 37. cn_hs_tariff_schedule_gacc (20 GACC 10-digit HS Codes)
    # -------------------------------------------------------------------------
    data["hs_codes"] = [
        ("8507600090", "850760", "8507600090999", "锂离子蓄电池组 (新能源汽车及储能用)", "Lithium-ion electric accumulators (EV & ESS modules)", "piece / Jin", 6.00, 0.00, 13.00, 9.00, "B/4"),
        ("8541430000", "854143", "8541430000999", "已组装的光伏电池组件 (太阳能电池板)", "Photovoltaic cells assembled in modules or panels", "piece / Jin", 0.00, 0.00, 13.00, 9.00, "B"),
        ("8703800010", "870380", "8703800010101", "仅装有驱动电动机的载人机动车辆 (纯电动汽车)", "Motor vehicles propelled solely by electric motor (BEV)", "unit / Jin", 15.00, 0.00, 13.00, 13.00, "B/4/O"),
        ("8504403090", "850440", "8504403090999", "智能光伏逆变器及变流器", "Static converters and smart solar PV inverters", "piece / Jin", 5.00, 0.00, 13.00, 13.00, "B"),
        ("8517130000", "851713", "8517130000999", "蜂窝网络智能手机", "Smartphones for cellular networks (5G)", "piece / Jin", 0.00, 0.00, 13.00, 13.00, "B"),
        ("8471300000", "847130", "8471300000999", "重量不超过10公斤的便携式数字自动数据处理设备 (笔记本电脑)", "Portable automatic data processing machines <= 10kg (Laptops)", "piece / Jin", 0.00, 0.00, 13.00, 13.00, "B"),
        ("8415102100", "841510", "8415102100999", "分体式变频房间空气调节器 (热泵空调)", "Split-system inverter air conditioners (Heat Pumps)", "piece / Jin", 10.00, 0.00, 13.00, 13.00, "B"),
        ("8528722100", "852872", "8528722100999", "彩色液晶平板智能电视机", "Color smart LCD / OLED television receivers", "piece / Jin", 12.00, 0.00, 13.00, 13.00, "B"),
        ("6109100000", "610910", "6109100000999", "棉制针织T恤衫、汗衫及马甲", "T-shirts, singlets and other vests, knitted of cotton", "piece / Jin", 10.00, 0.00, 13.00, 13.00, "B"),
        ("9503002100", "950300", "9503002100999", "塑料制玩偶及拼插积木类智力玩具", "Dolls, scale models and plastic construction toy sets", "piece / Jin", 0.00, 0.00, 13.00, 13.00, "B"),
        ("7225409900", "722540", "7225409900999", "热轧其他合金钢平板轧材 (CBAM受控钢材)", "Flat-rolled alloy steel products, hot-rolled (CBAM scope)", "Jin / metric ton", 3.00, 0.00, 13.00, 0.00, "B"),
        ("7606125900", "760612", "7606125900999", "铝合金矩形板、片及带 (CBAM受控铝材)", "Aluminum alloy rectangular plates and sheets (CBAM scope)", "Jin / metric ton", 6.00, 0.00, 13.00, 0.00, "B"),
        ("8479899990", "847989", "8479899990999", "工业多关节机械手及自动装配机器人", "Industrial articulated multi-axis robots and assembly arms", "piece / Jin", 0.00, 0.00, 13.00, 13.00, "B"),
        ("8607191000", "860719", "8607191000999", "铁道机车及轨道交通客车用转向架总成", "Bogies and steerable wheelsets for railway locomotives and metro cars", "unit / Jin", 2.00, 0.00, 13.00, 9.00, "B"),
        ("6204620000", "620462", "6204620000999", "棉制女式长裤及工装裤", "Women's or girls' trousers and shorts of cotton", "piece / Jin", 8.00, 0.00, 13.00, 13.00, "B"),
        ("2204210000", "220421", "2204210000101", "装入2升及以下容器的鲜葡萄酿造的酒 (葡萄牙DOC葡萄酒)", "Wine of fresh grapes in containers <= 2L (Douro/Alentejo/Port)", "liter / bottle", 14.00, 0.00, 13.00, 0.00, "A/B/R"),
        ("1509200000", "150920", "1509200000102", "特级初榨橄榄油 (葡萄牙进口)", "Extra virgin olive oil chemically unmodified", "Jin / liter", 10.00, 0.00, 9.00, 0.00, "A/B/R"),
        ("4504900000", "450490", "4504900000105", "压制软木塞及天然软木制品", "Agglomerated cork stoppers and natural cork articles", "Jin / piece", 5.00, 0.00, 13.00, 0.00, "A"),
        ("4703290000", "470329", "4703290000101", "漂白桉木碱木浆 (葡萄牙造纸木浆)", "Semi-bleached or bleached non-coniferous eucalyptus wood pulp", "Jin / metric ton", 0.00, 0.00, 13.00, 0.00, "A"),
        ("0203290090", "020329", "0203290090101", "冻猪肉 (葡萄牙黑猪及必萨罗猪肉)", "Frozen meat of swine (Portuguese Iberico & Bisaro pork)", "Jin / kg", 8.00, 0.00, 9.00, 0.00, "A/P/R"),
    ]

    # -------------------------------------------------------------------------
    # 38. cn_products_industrial_catalog (18 Industrial Products - 12 columns)
    # -------------------------------------------------------------------------
    data["products"] = [
        ("CN-SKU-CALB-LFP314", "91320413MA1M9Y2C4B", 101, "8507600090", "CALB L314Ah Zero-Carbon LFP Prismatic Module Pack", "Lithium-Ion EV & Grid Storage Battery", 176.000, 0.0680, 4850.00, 680.00, "UN3480 Class 9", 142.500),
        ("CN-SKU-BYD-SEAL-EV", "91440300192317458F", 102, "8703800010", "BYD Seal 82.5kWh AWD Blade Battery Electric Sedan", "Battery Electric Vehicle (BEV)", 4370.000, 14.2000, 168000.00, 23600.00, "UN3171 Class 9", 6840.000),
        ("CN-SKU-CATL-ENERC", "91350900587527783P", 103, "8507600090", "CATL EnerC Plus 306Ah Utility-Scale Liquid Cooled Rack", "Grid Energy Storage System (ESS)", 6800.000, 5.4000, 245000.00, 34200.00, "UN3480 Class 9", 8920.000),
        ("CN-SKU-LONGI-HIMO7", "91610132724912345X", 104, "8541430000", "LONGi Hi-MO 7 Bifacial 590W N-Type Solar PV Panel", "Solar Photovoltaic Module", 65.000, 0.0820, 520.00, 72.80, None, 310.000),
        ("CN-SKU-HW-SUN2000", "91440300618837699Q", 105, "8504403090", "Huawei FusionSolar SUN2000-100KTL-M2 Smart String Inverter", "Three-Phase Solar Inverter", 184.000, 0.2400, 18900.00, 2650.00, None, 485.000),
        ("CN-SKU-XM-15PRO-5G", "91110108551385082Q", 106, "8517130000", "Xiaomi 15 Pro 5G 512GB Leica Optics EU Edition", "Consumer Electronics Smartphone", 0.440, 0.0012, 3450.00, 485.00, "UN3481 Class 9", 48.200),
        ("CN-SKU-NB-STEEL-S355", "91330200778899112T", 108, "7225409900", "Ningbo S355J2 Wind-Tower Heavy Structural Alloy Steel Plate (1 Ton)", "Heavy Structural Steel (CBAM)", 2000.000, 0.1280, 4680.00, 655.00, None, 1980.000),
        ("CN-SKU-NB-ALU-6061", "91330200778899112T", 108, "7606125900", "Ningbo 6061-T6 Aerospace & EV Battery Tray Aluminum Sheet (1 Ton)", "Industrial Aluminum Sheet (CBAM)", 2000.000, 0.3700, 19800.00, 2770.00, None, 8450.000),
        ("CN-SKU-YW-APPAREL-LOT", "91330782098765432W", 107, "6204620000", "Yiwu Export Cotton Garment & Retail Assortment Carton (100 pcs)", "Textile & Apparel Wholesale", 92.000, 0.1800, 2850.00, 400.00, None, 215.000),
        ("CN-SKU-TRINA-VERTEX", "91320400608131370B", 110, "8541430000", "Trina Solar Vertex N 700W Bifacial TOPCon PV Module", "Solar Photovoltaic Module", 72.000, 0.0910, 580.00, 81.20, None, 295.000),
        ("CN-SKU-MIDEA-SPLIT", "91440606190342599T", 111, "8415102100", "Midea All-Easy Pro 12000BTU Inverter A+++ Heat Pump Split AC", "HVAC Inverter Air Conditioner", 68.000, 0.1650, 2100.00, 294.00, "UN3363 Class 9", 260.000),
        ("CN-SKU-GREE-SPLIT", "91440400192548256N", 112, "8415102100", "Gree Amber Elite 3.5kW Ultra-Efficient Split AC", "HVAC Inverter Air Conditioner", 70.000, 0.1700, 2250.00, 315.00, "UN3363 Class 9", 275.000),
        ("CN-SKU-HAIER-TV65", "91370200163562681G", 113, "8528722100", "Haier 65-inch 4K QD-MiniLED Smart Google TV", "Consumer Electronics TV", 48.000, 0.2200, 3200.00, 448.00, None, 190.000),
        ("CN-SKU-CRRC-BOGIE", "911100007178071858", 114, "8607191000", "CRRC High-Floor Metro Bogie Set with Traction Motors", "Rail Transit Bogie Assembly", 14500.000, 12.5000, 385000.00, 53900.00, None, 12500.000),
        ("CN-SKU-XM-BOOKPRO", "91110108551385082Q", 106, "8471300000", "Xiaomi Book Pro 16 Intel Ultra-7 OLED Slim Laptop", "Consumer Electronics Laptop", 3.800, 0.0085, 6200.00, 868.00, "UN3481 Class 9", 85.000),
        ("CN-SKU-BYD-ATTO3", "91440300192317458F", 102, "8703800010", "BYD Atto 3 60.5kWh Blade Battery Compact Electric SUV", "Battery Electric Vehicle (BEV)", 3780.000, 13.8000, 142000.00, 19880.00, "UN3171 Class 9", 5920.000),
        ("CN-SKU-HW-5G-AAU", "91440300618837699Q", 105, "8504403090", "Huawei 5G Massive MIMO AAU5613 Active Antenna Unit", "Telecommunications Equipment", 84.000, 0.1150, 32500.00, 4550.00, None, 410.000),
        ("CN-SKU-YW-TOYS-LOT", "91330782098765432W", 107, "9503002100", "Yiwu Educational Plastic Building Block Toy Assortment", "Children Educational Toys", 60.000, 0.1400, 1850.00, 259.00, None, 110.000),
    ]

    # -------------------------------------------------------------------------
    # 39. cn_ccc_compulsory_certifications (12 CCC Certificates - 9 columns)
    # -------------------------------------------------------------------------
    data["ccc_certs"] = [
        ("2025010907881201", "CN-SKU-CALB-LFP314", "91320413MA1M9Y2C4B", "CQC - China Quality Certification Centre", "GB 38031-2020 / UN38.3", "2025-01-15", "2030-01-14", "Valid", 1),
        ("2024011101664420", "CN-SKU-BYD-SEAL-EV", "91440300192317458F", "CCAP - China Certification Centre for Automotive", "GB 18384-2020 / WVTA EU", "2024-06-20", "2029-06-19", "Valid", 1),
        ("2025010907772103", "CN-SKU-CATL-ENERC", "91350900587527783P", "CQC - China Quality Certification Centre", "GB/T 36276-2023", "2025-02-10", "2030-02-09", "Valid", 1),
        ("2024010305661004", "CN-SKU-LONGI-HIMO7", "91610132724912345X", "CQC - China Quality Certification Centre", "GB/T 9535 / IEC 61215", "2024-06-20", "2029-06-19", "Valid", 1),
        ("2025010907553311", "CN-SKU-HW-SUN2000", "91440300618837699Q", "CQC - China Quality Certification Centre", "GB/T 37408 / EN 50549", "2025-03-05", "2030-03-04", "Valid", 1),
        ("2025011606998812", "CN-SKU-XM-15PRO-5G", "91110108551385082Q", "CQC / SRRC Radio Type Approval", "GB 4943.1-2022", "2025-01-20", "2030-01-19", "Valid", 1),
        ("2024010805112234", "CN-SKU-YW-APPAREL-LOT", "91330782098765432W", "CQC - China Quality Certification Centre", "GB 18401-2010", "2024-09-12", "2029-09-11", "Valid", 1),
        ("2025010907334415", "CN-SKU-TRINA-VERTEX", "91320400608131370B", "CQC - China Quality Certification Centre", "IEC 61215 / IEC 61730", "2025-02-18", "2030-02-17", "Valid", 1),
        ("2025010703889922", "CN-SKU-MIDEA-SPLIT", "91440606190342599T", "CQC - China Quality Certification Centre", "GB 4706.32-2012 / EN 60335", "2025-03-12", "2030-03-11", "Valid", 1),
        ("2025010703889923", "CN-SKU-GREE-SPLIT", "91440400192548256N", "CQC - China Quality Certification Centre", "GB 4706.32 / CE Mark", "2025-03-15", "2030-03-14", "Valid", 1),
        ("2025010808554433", "CN-SKU-HAIER-TV65", "91370200163562681G", "CQC - China Quality Certification Centre", "GB 8898-2011 / RED Directive", "2025-01-25", "2030-01-24", "Valid", 1),
        ("2024011101664425", "CN-SKU-BYD-ATTO3", "91440300192317458F", "CCAP - China Center for Automobile Product Certification", "GB 18384-2020 / WVTA EU", "2024-08-15", "2029-08-14", "Valid", 1),
    ]

    # -------------------------------------------------------------------------
    # 40. cn_mofcom_trade_licenses_quotas (10 MOFCOM Licenses - 10 columns)
    # CHECK (license_direction IN ('Export Control Dual-Use', 'Strategic EV & Battery Export License', 'Automatic Import License', 'Agricultural Tariff Quota'))
    # -------------------------------------------------------------------------
    data["mofcom_licenses"] = [
        ("MOFCOM-EX-2026-JS001", "91320413MA1M9Y2C4B", "8507600090", "Strategic EV & Battery Export License", "PRT", 15000.000, 120000000.00, "2026-01-01", "2026-12-31", "Shanghai / Ningbo Ports"),
        ("MOFCOM-EX-2026-GD002", "91440300192317458F", "8703800010", "Strategic EV & Battery Export License", "PRT", 12000.000, 320000000.00, "2026-01-01", "2026-12-31", "Shenzhen Yantian / Shekou"),
        ("MOFCOM-IM-2026-BJ09101", "91110000101123456N", "2204210000", "Automatic Import License", "PRT", 2500.000, 18500000.00, "2026-01-01", "2026-12-31", "Shanghai / Shenzhen Ports"),
        ("MOFCOM-IM-2026-BJ09102", "91110000101123456N", "0203290090", "Agricultural Tariff Quota", "PRT", 4500.000, 19500000.00, "2026-01-01", "2026-12-31", "Shanghai Waigaoqiao Port"),
        ("MOFCOM-EX-2026-SN003", "91610132724912345X", "8541430000", "Strategic EV & Battery Export License", "PRT", 8000.000, 65000000.00, "2026-01-01", "2026-12-31", "Shanghai / Qingdao Ports"),
        ("MOFCOM-EX-2026-ZJ004", "91330200778899112T", "7225409900", "Export Control Dual-Use", "PRT", 25000.000, 35000000.00, "2026-01-01", "2026-12-31", "Ningbo Zhoushan Port"),
        ("MOFCOM-EX-2026-GD005", "91440300618837699Q", "8504403090", "Export Control Dual-Use", "PRT", 5000.000, 48000000.00, "2026-01-01", "2026-12-31", "Shenzhen Shekou Port"),
        ("MOFCOM-IM-2026-HQ006", "91440400MA56LUS01P", "1509200000", "Automatic Import License", "PRT", 3000.000, 15000000.00, "2026-01-01", "2026-12-31", "Hengqin Port"),
        ("MOFCOM-IM-2026-SH007", "91110000101123456N", "4504900000", "Automatic Import License", "PRT", 1200.000, 14000000.00, "2026-01-01", "2026-12-31", "Shanghai Waigaoqiao Port"),
        ("MOFCOM-IM-2026-QD008", "91370200163562681G", "4703290000", "Automatic Import License", "PRT", 80000.000, 48000000.00, "2026-01-01", "2026-12-31", "Qingdao Dagang Port"),
    ]

    # -------------------------------------------------------------------------
    # 41. cn_b2b_commercial_contracts (18 Contracts with Portuguese Partners - 11 columns)
    # -------------------------------------------------------------------------
    data["contracts"] = [
        ("CN-PT-CTR-2026-001", "91320413MA1M9Y2C4B", "PT517890123", "CALB Portugal - Fábrica de Baterias de Sines, S.A.", "CN_EXPORT_TO_PT", "2026-01-15", "CIF", "EUR", 18500000.00, "LC_AT_SIGHT", "Macau WTC"),
        ("CN-PT-CTR-2026-002", "91440300192317458F", "PT500234567", "Salvador Caetano Auto - Importação e Distribuição, S.A.", "CN_EXPORT_TO_PT", "2026-01-22", "CIF", "EUR", 28320000.00, "30_TT_70_BL", "CIETAC Beijing"),
        ("CN-PT-CTR-2026-003", "91610132724912345X", "PT500697256", "EDP Renováveis & Energia Solar Portugal, S.A.", "CN_EXPORT_TO_PT", "2026-02-05", "FOB", "USD", 7280000.00, "LC_AT_SIGHT", "SHIAC Shanghai"),
        ("CN-PT-CTR-2026-004", "91350900587527783P", "PT503412890", "REN - Redes Energéticas Nacionais, SGPS, S.A.", "CN_EXPORT_TO_PT", "2026-02-18", "CIF", "EUR", 10260000.00, "LC_AT_SIGHT", "CAC Lisboa"),
        ("CN-PT-CTR-2026-005", "91110108551385082Q", "PT500246810", "Worten - Equipamentos para o Lar, S.A. (Grupo Sonae)", "CN_EXPORT_TO_PT", "2026-03-01", "CIP", "EUR", 4850000.00, "OA_60_DAYS", "SHIAC Shanghai"),
        ("CN-PT-CTR-2026-006", "91330200778899112T", "PT500191827", "Mota-Engil Engenharia e Construção, S.A.", "CN_EXPORT_TO_PT", "2026-03-10", "CIF", "USD", 5425000.00, "30_TT_70_BL", "CIETAC Beijing"),
        ("CN-PT-CTR-2026-007", "91330782098765432W", "PT504998877", "Varziela Chinarte - Centro Grossista de Vila do Conde, Lda.", "CN_EXPORT_TO_PT", "2026-03-18", "FOB", "CNY", 14250000.00, "30_TT_70_BL", "Macau WTC"),
        ("CN-PT-CTR-2026-008", "91110000101123456N", "PT500265432", "Symington Family Estates - Vinhos do Douro e Porto, S.A.", "CN_IMPORT_FROM_PT", "2026-02-12", "FOB", "EUR", 3450000.00, "LC_AT_SIGHT", "Macau WTC"),
        ("CN-PT-CTR-2026-009", "91110000101123456N", "PT500077889", "Corticeira Amorim, SGPS, S.A.", "CN_IMPORT_FROM_PT", "2026-02-25", "CIF", "EUR", 4120000.00, "OA_60_DAYS", "CAC Lisboa"),
        ("CN-PT-CTR-2026-010", "91440400MA56LUS01P", "PT500112233", "Sovena Consumer Goods - Azeites de Portugal, S.A.", "CN_IMPORT_FROM_PT", "2026-03-08", "CIF", "EUR", 2680000.00, "LC_AT_SIGHT", "Macau WTC"),
        ("CN-PT-CTR-2026-011", "91110000101123456N", "PT508112244", "Maporal - Matadouro de Porco Alentejano, S.A.", "CN_IMPORT_FROM_PT", "2026-03-15", "CIF", "EUR", 4200000.00, "LC_AT_SIGHT", "Macau WTC"),
        ("CN-PT-CTR-2026-012", "91110000101123456N", "PT500214890", "Sogrape Vinhos, S.A.", "CN_IMPORT_FROM_PT", "2026-03-22", "CIF", "EUR", 3100000.00, "LC_AT_SIGHT", "CAC Lisboa"),
        ("CN-PT-CTR-2026-013", "91370200163562681G", "PT500055214", "The Navigator Company, S.A.", "CN_IMPORT_FROM_PT", "2026-03-28", "CIF", "EUR", 6500000.00, "OA_60_DAYS", "CIETAC Beijing"),
        ("CN-PT-CTR-2026-014", "91440300618837699Q", "PT500697256", "EDP Renováveis, S.A.", "CN_EXPORT_TO_PT", "2026-04-02", "CIF", "EUR", 4800000.00, "LC_AT_SIGHT", "CAC Lisboa"),
        ("CN-PT-CTR-2026-015", "91110108551385082Q", "PT500246810", "Worten - Equipamentos para o Lar, S.A.", "CN_EXPORT_TO_PT", "2026-04-05", "CIP", "EUR", 6200000.00, "OA_60_DAYS", "SHIAC Shanghai"),
        ("CN-PT-CTR-2026-016", "91440606190342599T", "PT500246810", "Worten - Equipamentos para o Lar, S.A.", "CN_EXPORT_TO_PT", "2026-04-10", "CIF", "EUR", 3800000.00, "LC_AT_SIGHT", "CAC Lisboa"),
        ("CN-PT-CTR-2026-017", "911100007178071858", "PT503412890", "REN - Redes Energéticas Nacionais, SGPS, S.A.", "CN_EXPORT_TO_PT", "2026-04-14", "CIF", "EUR", 8500000.00, "LC_AT_SIGHT", "CAC Lisboa"),
        ("CN-PT-CTR-2026-018", "91440300192317458F", "PT500234567", "Salvador Caetano Auto, S.A.", "CN_EXPORT_TO_PT", "2026-04-18", "CIF", "EUR", 18500000.00, "30_TT_70_BL", "CIETAC Beijing"),
    ]

    # -------------------------------------------------------------------------
    # 42. cn_commercial_invoices (18 Invoices matching Contracts & DAUs - 11 columns)
    # -------------------------------------------------------------------------
    data["invoices"] = [
        ("INV-CN-2026-8801", "CN-PT-CTR-2026-001", "2026-03-20", "91320413MA1M9Y2C4B", "PT517890123", "EUR", 6120000.00, 145000.00, 18500.00, 6283500.00, 7.820000),
        ("INV-CN-2026-8802", "CN-PT-CTR-2026-002", "2026-03-25", "91440300192317458F", "PT500234567", "EUR", 9440000.00, 260000.00, 32000.00, 9732000.00, 7.820000),
        ("INV-CN-2026-8803", "CN-PT-CTR-2026-003", "2026-04-02", "91610132724912345X", "PT500697256", "USD", 3640000.00, 0.00, 0.00, 3640000.00, 7.210000),
        ("INV-CN-2026-8804", "CN-PT-CTR-2026-004", "2026-04-10", "91350900587527783P", "PT503412890", "EUR", 3420000.00, 88000.00, 12000.00, 3520000.00, 7.835000),
        ("INV-CN-2026-8805", "CN-PT-CTR-2026-005", "2026-04-15", "91110108551385082Q", "PT500246810", "EUR", 2425000.00, 42000.00, 6500.00, 2473500.00, 7.840000),
        ("INV-CN-2026-8806", "CN-PT-CTR-2026-006", "2026-04-18", "91330200778899112T", "PT500191827", "USD", 2655000.00, 95000.00, 11000.00, 2761000.00, 7.220000),
        ("INV-CN-2026-8807", "CN-PT-CTR-2026-007", "2026-04-22", "91330782098765432W", "PT504998877", "CNY", 7125000.00, 0.00, 0.00, 7125000.00, 1.000000),
        ("INV-PT-2026-9901", "CN-PT-CTR-2026-008", "2026-04-05", "91110000101123456N", "PT500265432", "EUR", 1480000.00, 38000.00, 4500.00, 1522500.00, 7.830000),
        ("INV-PT-2026-9902", "CN-PT-CTR-2026-009", "2026-04-12", "91110000101123456N", "PT500077889", "EUR", 1850000.00, 32000.00, 3800.00, 1885800.00, 7.830000),
        ("INV-PT-2026-9903", "CN-PT-CTR-2026-010", "2026-04-20", "91440400MA56LUS01P", "PT500112233", "EUR", 1120000.00, 29000.00, 3200.00, 1152200.00, 7.840000),
        ("INV-PT-2026-9905", "CN-PT-CTR-2026-011", "2026-04-24", "91110000101123456N", "PT508112244", "EUR", 1600000.00, 45000.00, 5000.00, 1650000.00, 7.835000),
        ("INV-PT-2026-9906", "CN-PT-CTR-2026-012", "2026-04-28", "91110000101123456N", "PT500214890", "EUR", 1240000.00, 36000.00, 4000.00, 1280000.00, 7.835000),
        ("INV-PT-2026-9904", "CN-PT-CTR-2026-013", "2026-04-30", "91370200163562681G", "PT500055214", "EUR", 2040000.00, 55000.00, 5000.00, 2100000.00, 7.830000),
        ("INV-CN-2026-8808", "CN-PT-CTR-2026-014", "2026-05-02", "91440300618837699Q", "PT500697256", "EUR", 1780000.00, 52000.00, 8000.00, 1840000.00, 7.840000),
        ("INV-CN-2026-8809", "CN-PT-CTR-2026-015", "2026-05-04", "91110108551385082Q", "PT500246810", "EUR", 3140000.00, 52000.00, 8000.00, 3200000.00, 7.840000),
        ("INV-CN-2026-8810", "CN-PT-CTR-2026-016", "2026-05-06", "91440606190342599T", "PT500246810", "EUR", 1400000.00, 45000.00, 5000.00, 1450000.00, 7.840000),
        ("INV-CN-2026-8811", "CN-PT-CTR-2026-017", "2026-05-08", "911100007178071858", "PT503412890", "EUR", 4050000.00, 88000.00, 12000.00, 4150000.00, 7.840000),
        ("INV-CN-2026-8813", "CN-PT-CTR-2026-018", "2026-05-12", "91440300192317458F", "PT500234567", "EUR", 8680000.00, 240000.00, 30000.00, 8950000.00, 7.840000),
    ]

    # -------------------------------------------------------------------------
    # 43. cn_commercial_invoice_lines (26 Itemized Invoice Lines - 12 columns)
    # -------------------------------------------------------------------------
    data["invoice_lines"] = [
        (1, "INV-CN-2026-8801", 1, "CN-SKU-CALB-LFP314", "8507600090", "CALB L314Ah Zero-Carbon LFP Battery Pack Modules for Sines Assembly", 10000.00, 1760000.000, 1840000.000, 612.0000, 6120000.00, "LOT-CALB-2026-03A"),
        (2, "INV-CN-2026-8802", 1, "CN-SKU-BYD-SEAL-EV", "8703800010", "BYD Seal AWD Electric Passenger Vehicles (EU Spec WVTA)", 400.00, 1748000.000, 1780000.000, 23600.0000, 9440000.00, "LOT-BYD-2026-03B"),
        (3, "INV-CN-2026-8803", 1, "CN-SKU-LONGI-HIMO7", "8541430000", "LONGi Hi-MO 7 590W Bifacial Solar PV Modules for Alentejo Solar Park", 50000.00, 3250000.000, 3420000.000, 72.8000, 3640000.00, "LOT-LONGI-2026-04A"),
        (4, "INV-CN-2026-8804", 1, "CN-SKU-CATL-ENERC", "8507600090", "CATL EnerC Plus Grid-Scale Battery Storage Containers for REN Grid", 100.00, 680000.000, 710000.000, 34200.0000, 3420000.00, "LOT-CATL-2026-04B"),
        (5, "INV-CN-2026-8805", 1, "CN-SKU-XM-15PRO-5G", "8517130000", "Xiaomi 15 Pro 5G Smartphones PT/EU Retail Packaging", 5000.00, 2200.000, 3100.000, 485.0000, 2425000.00, "LOT-XM-2026-04C"),
        (6, "INV-CN-2026-8806", 1, "CN-SKU-NB-STEEL-S355", "7225409900", "Ningbo S355J2 Structural Alloy Steel Plates for Sines Industrial Plant", 2000.00, 4000000.000, 4020000.000, 655.0000, 1310000.00, "LOT-NBST-2026-04D"),
        (7, "INV-CN-2026-8806", 2, "CN-SKU-NB-ALU-6061", "7606125900", "Ningbo 6061-T6 Structural Aluminum Sheets (CBAM Regulated)", 485.56, 971120.000, 985000.000, 2770.0000, 1345000.00, "LOT-NBAL-2026-04E"),
        (8, "INV-CN-2026-8807", 1, "CN-SKU-YW-APPAREL-LOT", "6204620000", "Yiwu Textile & Cotton Apparel Assortment Cartons via BRI Rail", 2500.00, 230000.000, 248000.000, 2850.0000, 7125000.00, "LOT-YIWU-2026-04F"),
        (9, "INV-PT-2026-9901", 1, None, "2204210000", "Symington Graham's 20Y Tawny Port & Douro DOC Reserva Wine 750ml", 120000.00, 180000.000, 336000.000, 12.3333, 1480000.00, "LOT-SH-SYM-2026A"),
        (10, "INV-PT-2026-9902", 1, None, "4504900000", "Amorim Natural Cork TwinTop Wine Stoppers Sterile Packed", 15000000.00, 135000.000, 144000.000, 0.1233, 1850000.00, "LOT-SH-AMO-2026B"),
        (11, "INV-PT-2026-9903", 1, None, "1509200000", "Oliveira da Serra Extra Virgin Olive Oil Alentejo 750ml Bottles", 180000.00, 270000.000, 296000.000, 6.2222, 1120000.00, "LOT-HQ-SOV-2026C"),
        (12, "INV-PT-2026-9905", 1, None, "0203290090", "Maporal Frozen Bone-in & Boneless Iberico Pork Cuts (Belly/Shoulder)", 450000.00, 900000.000, 944000.000, 3.5555, 1600000.00, "LOT-TAO-MAP-2026D"),
        (13, "INV-PT-2026-9906", 1, None, "2204210000", "Sogrape Quinta da Leda Douro DOC & Grão Vasco Dão Red Wine 750ml", 95000.00, 142500.000, 266000.000, 13.0526, 1240000.00, "LOT-SH-SOG-2026E"),
        (14, "INV-PT-2026-9904", 1, None, "4703290000", "The Navigator Company Bleached Eucalyptus Kraft Pulp (BEKP 500kg Bales)", 4000.00, 4000000.000, 4040000.000, 510.0000, 2040000.00, "LOT-QD-NAV-2026F"),
        (15, "INV-CN-2026-8808", 1, "CN-SKU-HW-SUN2000", "8504403090", "Huawei FusionSolar Smart Inverters for EDP Alentejo Solar", 800.00, 147200.000, 156000.000, 2225.0000, 1780000.00, "LOT-HW-2026-05A"),
        (16, "INV-CN-2026-8809", 1, "CN-SKU-XM-BOOKPRO", "8471300000", "Xiaomi Book Pro Laptops for Worten Back-to-School Campaign", 4000.00, 15200.000, 22400.000, 785.0000, 3140000.00, "LOT-XM-2026-05B"),
        (17, "INV-CN-2026-8810", 1, "CN-SKU-MIDEA-SPLIT", "8415102100", "Midea Inverter Split Heat Pump Air Conditioners", 5000.00, 340000.000, 370000.000, 280.0000, 1400000.00, "LOT-MD-2026-05C"),
        (18, "INV-CN-2026-8811", 1, "CN-SKU-CRRC-BOGIE", "8607191000", "CRRC Metro Bogies with Traction Motors for Lisbon Metro Expansion", 80.00, 1160000.000, 1190000.000, 50625.0000, 4050000.00, "LOT-CRRC-2026-05D"),
        (19, "INV-CN-2026-8813", 1, "CN-SKU-BYD-ATTO3", "8703800010", "BYD Atto 3 Compact Electric SUVs for Salvador Caetano Distribution", 350.00, 1323000.000, 1350000.000, 24800.0000, 8680000.00, "LOT-BYD-2026-05E"),
        (20, "INV-CN-2026-8803", 2, "CN-SKU-TRINA-VERTEX", "8541430000", "Trina Solar 700W Bifacial PV Panels for Hybrid Wind-Solar", 20000.00, 1440000.000, 1520000.000, 75.0000, 1500000.00, "LOT-TRN-2026-04G"),
        (21, "INV-CN-2026-8805", 2, "CN-SKU-YW-TOYS-LOT", "9503002100", "Yiwu Intelligence Block Toy Assortment for Sonae Retail", 10000.00, 600000.000, 640000.000, 45.0000, 450000.00, "LOT-YW-2026-04H"),
        (22, "INV-CN-2026-8807", 2, "CN-SKU-YW-APPAREL-LOT", "6204620000", "Yiwu Women's Knitted Apparel B2B Lots via Rail", 1500.00, 138000.000, 148000.000, 2850.0000, 4275000.00, "LOT-YIWU-2026-04I"),
        (23, "INV-PT-2026-9901", 2, None, "2204210000", "Symington Cockburn's Special Reserve Port Wine 750ml", 60000.00, 90000.000, 168000.000, 9.5000, 570000.00, "LOT-SH-SYM-2026G"),
        (24, "INV-PT-2026-9903", 2, None, "1509200000", "Sovena Andorinha Portuguese Cold-Pressed Olive Oil 500ml", 120000.00, 120000.000, 135000.000, 4.2500, 510000.00, "LOT-HQ-SOV-2026H"),
        (25, "INV-PT-2026-9905", 2, None, "0203290090", "Maporal Frozen Prime Iberico Pork Loins (Lombo de Porco Preto)", 200000.00, 400000.000, 420000.000, 4.1000, 820000.00, "LOT-TAO-MAP-2026I"),
        (26, "INV-CN-2026-8801", 2, "CN-SKU-CALB-LFP314", "8507600090", "CALB L314Ah High-Capacity Energy Cell Spare Integration Units", 1000.00, 176000.000, 184000.000, 612.0000, 612000.00, "LOT-CALB-2026-03K"),
    ]

    # -------------------------------------------------------------------------
    # 44. cn_customs_export_declarations_gacc (15 GACC Export Declarations - 13 columns)
    # CHECK (clearance_channel IN ('Released Automatically', 'Doc Review', 'Physical Inspection'))
    # -------------------------------------------------------------------------
    data["gacc_exports"] = [
        ("220120260000108801", "INV-CN-2026-8801", "91320413MA1M9Y2C4B", "2201", 1774080000, "0110", "2 - Maritime", "COSU6288991101", "9795610", "PTSIN", 47858400.00, 6638000.00, "Released Automatically"),
        ("530120260000108802", "INV-CN-2026-8802", "91440300192317458F", "5301", 1774512000, "0110", "2 - Maritime", "COSU6288991102", "9842105", "PTSIN", 73820800.00, 10238000.00, "Doc Review"),
        ("220120260000108803", "INV-CN-2026-8803", "91610132724912345X", "2201", 1775116800, "0110", "2 - Maritime", "COSU6288991103", "9795610", "PTSIN", 26244400.00, 3640000.00, "Released Automatically"),
        ("310120260000108804", "INV-CN-2026-8804", "91350900587527783P", "3101", 1775808000, "0110", "2 - Maritime", "COSU6288991104", "9795634", "PTLEI", 26795700.00, 3710000.00, "Physical Inspection"),
        ("010120260000108805", "INV-CN-2026-8805", "91110108551385082Q", "0101", 1776240000, "0110", "5 - Air", "047-88991105", "JD431", "PTLIS", 19012000.00, 2630000.00, "Released Automatically"),
        ("310120260000108806", "INV-CN-2026-8806", "91330200778899112T", "3101", 1776499200, "0110", "2 - Maritime", "COSU6288991106", "9795634", "PTSIN", 19169100.00, 2655000.00, "Doc Review"),
        ("292120260000108807", "INV-CN-2026-8807", "91330782098765432W", "2921", 1776844800, "9710", "3 - Rail", "CIMSMGS-YW2026-07", "X8020-YIWU-IB", "PTENT", 7125000.00, 986800.00, "Released Automatically"),
        ("530120260000108808", "INV-CN-2026-8808", "91440300618837699Q", "5301", 1777017600, "0110", "2 - Maritime", "COSU6288991108", "9795646", "PTSIN", 14425600.00, 1998000.00, "Released Automatically"),
        ("010120260000108809", "INV-CN-2026-8809", "91110108551385082Q", "0101", 1777276800, "0110", "5 - Air", "047-88991109", "CA1091", "PTLIS", 25088000.00, 3474800.00, "Released Automatically"),
        ("510120260000108810", "INV-CN-2026-8810", "91440606190342599T", "5101", 1777449600, "0110", "2 - Maritime", "COSU6288991110", "9795646", "PTSIN", 11368000.00, 1574500.00, "Doc Review"),
        ("010120260000108811", "INV-CN-2026-8811", "911100007178071858", "0101", 1777708800, "0110", "2 - Maritime", "COSU6288991111", "9795622", "PTSIN", 32536000.00, 4506300.00, "Doc Review"),
        ("292120260000108812", "INV-CN-2026-8807", "91330782098765432W", "2921", 1777968000, "9710", "3 - Rail", "CIMSMGS-YW2026-12", "X8020-YIWU-MAD", "PTLIS", 4275000.00, 592000.00, "Released Automatically"),
        ("530120260000108813", "INV-CN-2026-8813", "91440300192317458F", "5301", 1778140800, "0110", "2 - Maritime", "COSU6288991113", "9842117", "PTSIN", 70168000.00, 9718500.00, "Doc Review"),
        ("310120260000108814", "INV-CN-2026-8803", "91320400608131370B", "3101", 1778313600, "0110", "2 - Maritime", "COSU6288991114", "9795622", "PTSIN", 11760000.00, 1628800.00, "Released Automatically"),
        ("530120260000108815", "INV-CN-2026-8805", "91440300755673010C", "5301", 1778486400, "9610", "5 - Air", "871-33221100", "5Y8911", "PTLIS", 8250000.00, 1142600.00, "Released Automatically"),
    ]

    # -------------------------------------------------------------------------
    # 45. cn_customs_import_declarations_gacc (10 GACC Import Declarations - 13 columns)
    # -------------------------------------------------------------------------
    data["gacc_imports"] = [
        ("220120261000990001", "91110000101123456N", "PT500265432", "CPRT18000102000101", "2204210000", "PTLEI", "2201", "COSU6288992201", 11921175.00, 1668964.50, 1510015.50, 1963019.90, "2026-05-04"),
        ("220120261000990002", "91110000101123456N", "PT500077889", "CPRT18009901000202", "4504900000", "PTLEI", "2201", "COSU6288992202", 14765814.00, 738290.70, 0.00, 2015533.61, "2026-05-10"),
        ("530420261000990003", "91440400MA56LUS01P", "PT500112233", "CPRT18000401000303", "1509200000", "PTSIN", "5304", "COSU6288992203", 9033248.00, 903324.80, 0.00, 894291.55, "2026-05-18"),
        ("310120261000990004", "91330200778899112T", "PT500334455", None, "4703290000", "PTLEI", "3101", "COSU6288992204", 22450000.00, 0.00, 0.00, 2918500.00, "2026-05-22"),
        ("220120261000990005", "91110000101123456N", "PT508112244", "CPRT18000101000505", "0203290090", "PTSIN", "2201", "COSU6288992205", 8420000.00, 673600.00, 0.00, 818424.00, "2026-05-26"),
        ("220120261000990006", "91110000101123456N", "PT500214890", "CPRT18000102000606", "2204210000", "PTLEI", "2201", "COSU6288992206", 9722400.00, 1361136.00, 1231494.00, 1600984.00, "2026-05-29"),
        ("370220261000990007", "91370200163562681G", "PT500055214", "CPRT18000301000707", "4703290000", "PTSET", "3702", "COSU6288992207", 16443000.00, 0.00, 0.00, 2137590.00, "2026-05-31"),
        ("530120261000990008", "91440300755673010C", "PT500876543", "CPRT15000104000505", "1509200000", "PTSIN", "5301", "COSU6288992202", 7250000.00, 725000.00, 0.00, 717750.00, "2026-06-02"),
        ("220120261000990009", "91310000132234561L", "PT500123999", "CPRT45000106000404", "4504900000", "PTLEI", "2201", "COSU6288992207", 6500000.00, 325000.00, 0.00, 887250.00, "2026-06-04"),
        ("370220261000990010", "91110000101123456N", "PT502889900", "CPRT18000201000505", "0203290090", "PTSIN", "3702", "COSU6288992205", 11125700.00, 890056.00, 0.00, 1081418.04, "2026-06-06"),
    ]

    # -------------------------------------------------------------------------
    # 46. cn_ciq_inspection_quarantine_records (14 CIQ Records - 11 columns)
    # CHECK (inspection_direction IN ('Outbound Export Inspection', 'Inbound Import Quarantine'))
    # CHECK (inspection_verdict IN ('Pass - Certificate Issued', 'Quarantine Treatment Required', 'Labeling Rectification Ordered', 'Rejected - Return to Portugal/Destroy'))
    # -------------------------------------------------------------------------
    data["ciq_records"] = [
        ("CIQ-2026-SH-001088", "220120260000108801", "Outbound Export Inspection", "Shanghai CIQ", "LAB-UN383-BAT-01", 0.0010, 1, 1, "ECIQ-CN20260320001", "Pass - Certificate Issued", "2026-03-21 10:30:00"),
        ("CIQ-2026-SZ-001089", "530120260000108802", "Outbound Export Inspection", "Guangdong Shenzhen CIQ", "LAB-EV-SAFETY-02", 0.0005, 1, 1, "ECIQ-CN20260326002", "Pass - Certificate Issued", "2026-03-26 14:15:00"),
        ("CIQ-2026-SH-001090", "220120260000108803", "Outbound Export Inspection", "Shanghai CIQ", "LAB-PV-IEC-03", 0.0000, 1, 1, "ECIQ-CN20260402003", "Pass - Certificate Issued", "2026-04-02 09:45:00"),
        ("CIQ-2026-NB-001091", "310120260000108804", "Outbound Export Inspection", "Ningbo CIQ", "LAB-HAZMAT-ESS-04", 0.0020, 1, 1, "ECIQ-CN20260410004", "Pass - Certificate Issued", "2026-04-10 16:40:00"),
        ("CIQ-2026-SH-009901", "220120261000990001", "Inbound Import Quarantine", "Shanghai Waigaoqiao CIQ", "LAB-WINE-SO2-01", 0.0120, 1, 1, "ECIQ-IM20260505101", "Pass - Certificate Issued", "2026-05-05 09:20:00"),
        ("CIQ-2026-SH-009902", "220120261000990002", "Inbound Import Quarantine", "Shanghai Waigaoqiao CIQ", "LAB-CORK-TCA-02", 0.0002, 1, 1, "ECIQ-IM20260511102", "Pass - Certificate Issued", "2026-05-11 11:00:00"),
        ("CIQ-2026-HQ-009903", "530420261000990003", "Inbound Import Quarantine", "Zhuhai Hengqin CIQ", "LAB-OLIVE-ACID-03", 0.0040, 1, 1, "ECIQ-IM20260519103", "Pass - Certificate Issued", "2026-05-19 15:10:00"),
        ("CIQ-2026-QD-009905", "220120261000990005", "Inbound Import Quarantine", "Shanghai Cold-Chain CIQ", "LAB-SWINE-PCR-05", 0.0080, 1, 0, "ECIQ-IM20260527105", "Labeling Rectification Ordered", "2026-05-27 17:45:00"),
        ("CIQ-2026-SH-009906", "220120261000990006", "Inbound Import Quarantine", "Shanghai Waigaoqiao CIQ", "LAB-WINE-DOURO-06", 0.0010, 1, 1, "ECIQ-IM20260529106", "Pass - Certificate Issued", "2026-05-29 11:30:00"),
        ("CIQ-2026-QD-009907", "370220261000990007", "Inbound Import Quarantine", "Qingdao Dagang CIQ", "LAB-WOOD-PULP-07", 0.0000, 1, 1, "ECIQ-IM20260531107", "Pass - Certificate Issued", "2026-05-31 14:20:00"),
        ("CIQ-2026-SZ-001092", "530120260000108808", "Outbound Export Inspection", "Shenzhen CIQ", "LAB-EMC-5G-08", 0.0000, 1, 1, "ECIQ-CN20260503008", "Pass - Certificate Issued", "2026-05-03 10:15:00"),
        ("CIQ-2026-BJ-001093", "010120260000108809", "Outbound Export Inspection", "Beijing Capital CIQ", "LAB-LITHIUM-AIR-09", 0.0005, 1, 1, "ECIQ-CN20260505009", "Pass - Certificate Issued", "2026-05-05 13:40:00"),
        ("CIQ-2026-GZ-001094", "510120260000108810", "Outbound Export Inspection", "Guangzhou Nansha CIQ", "LAB-HVAC-FGAS-10", 0.0000, 1, 1, "ECIQ-CN20260507010", "Pass - Certificate Issued", "2026-05-07 15:20:00"),
        ("CIQ-2026-TJ-001095", "010120260000108811", "Outbound Export Inspection", "Tianjin Port CIQ", "LAB-METRO-BOGIE-11", 0.0000, 1, 1, "ECIQ-CN20260509011", "Pass - Certificate Issued", "2026-05-09 16:00:00"),
    ]

    # -------------------------------------------------------------------------
    # 47. cn_vat_export_tax_rebates_sta (12 STA Tax Rebates - 9 columns)
    # CHECK (sta_approval_status IN ('Approved & Credited', 'Under Audit', 'Denied'))
    # -------------------------------------------------------------------------
    data["vat_rebates"] = [
        ("STA-REB-2026-001", "220120260000108801", "91320413MA1M9Y2C4B", "FAPIAO-3204-2026-8801", 47858400.00, 9.00, 4307256.00, "Approved & Credited", "2026-04-15"),
        ("STA-REB-2026-002", "530120260000108802", "91440300192317458F", "FAPIAO-4403-2026-8802", 73820800.00, 13.00, 9596704.00, "Approved & Credited", "2026-04-20"),
        ("STA-REB-2026-003", "220120260000108803", "91610132724912345X", "FAPIAO-6101-2026-8803", 26244400.00, 9.00, 2361996.00, "Approved & Credited", "2026-04-28"),
        ("STA-REB-2026-004", "310120260000108804", "91350900587527783P", "FAPIAO-3509-2026-8804", 26795700.00, 9.00, 2411613.00, "Approved & Credited", "2026-05-05"),
        ("STA-REB-2026-005", "010120260000108805", "91110108551385082Q", "FAPIAO-1101-2026-8805", 19012000.00, 13.00, 2471560.00, "Approved & Credited", "2026-05-10"),
        ("STA-REB-2026-006", "310120260000108806", "91330200778899112T", "FAPIAO-3302-2026-8806", 19169100.00, 0.00, 0.00, "Denied", "2026-05-15"),
        ("STA-REB-2026-007", "292120260000108807", "91330782098765432W", "FAPIAO-3307-2026-8807", 7125000.00, 13.00, 926250.00, "Under Audit", "2026-05-28"),
        ("STA-REB-2026-008", "530120260000108808", "91440300618837699Q", "FAPIAO-4403-2026-8808", 14425600.00, 13.00, 1875328.00, "Approved & Credited", "2026-06-02"),
        ("STA-REB-2026-009", "010120260000108809", "91110108551385082Q", "FAPIAO-1101-2026-8809", 25088000.00, 13.00, 3261440.00, "Approved & Credited", "2026-06-05"),
        ("STA-REB-2026-010", "510120260000108810", "91440606190342599T", "FAPIAO-4406-2026-8810", 11368000.00, 13.00, 1477840.00, "Approved & Credited", "2026-06-08"),
        ("STA-REB-2026-011", "010120260000108811", "911100007178071858", "FAPIAO-1101-2026-8811", 32536000.00, 13.00, 4229680.00, "Approved & Credited", "2026-06-12"),
        ("STA-REB-2026-013", "530120260000108813", "91440300192317458F", "FAPIAO-4403-2026-8813", 70168000.00, 13.00, 9121840.00, "Approved & Credited", "2026-06-16"),
    ]

    # -------------------------------------------------------------------------
    # 48. cn_fx_settlements_pboc_safe (16 Settlements Matching Afonso SWIFT/CIPS - 12 columns)
    # CHECK (settlement_channel IN ('SWIFT_EUR', 'SWIFT_USD', 'CIPS_DIRECT_RMB'))
    # -------------------------------------------------------------------------
    data["fx_settlements"] = [
        ("SAFE-2026-SH-90001", "97ed4827-7b6f-4491-a06f-b548d5a75001", "INV-CN-2026-8801", "91320413MA1M9Y2C4B", "517890123", "Bank of China (BOC) Jiangsu Branch", "SWIFT_EUR", "EUR", 6283500.00, 49136970.00, 7.820000, "2026-03-28"),
        ("SAFE-2026-SZ-90002", "97ed4827-7b6f-4491-a06f-b548d5a75002", "INV-CN-2026-8802", "91440300192317458F", "500234567", "ICBC Shenzhen Futian Branch", "SWIFT_EUR", "EUR", 9732000.00, 76104240.00, 7.820000, "2026-04-02"),
        ("SAFE-2026-XA-90003", "97ed4827-7b6f-4491-a06f-b548d5a75003", "INV-CN-2026-8803", "91610132724912345X", "500697256", "China Construction Bank (CCB) Shaanxi", "SWIFT_USD", "USD", 3640000.00, 26244400.00, 7.210000, "2026-04-09"),
        ("SAFE-2026-ND-90004", "97ed4827-7b6f-4491-a06f-b548d5a75004", "INV-CN-2026-8804", "91350900587527783P", "503412890", "Bank of China (BOC) Lisbon-Fujian Clearing", "SWIFT_EUR", "EUR", 3520000.00, 27579200.00, 7.835000, "2026-04-16"),
        ("SAFE-2026-BJ-90005", "97ed4827-7b6f-4491-a06f-b548d5a75005", "INV-CN-2026-8805", "91110108551385082Q", "500246810", "ICBC Beijing Head Office", "SWIFT_EUR", "EUR", 2473500.00, 19392240.00, 7.840000, "2026-04-22"),
        ("SAFE-2026-NB-90006", "97ed4827-7b6f-4491-a06f-b548d5a75006", "INV-CN-2026-8806", "91330200778899112T", "500191827", "Bank of Communications Ningbo", "SWIFT_USD", "USD", 2761000.00, 19934420.00, 7.220000, "2026-04-25"),
        ("SAFE-2026-YW-90007", "CIPS-RMB-20260428-YIWU-PT007", "INV-CN-2026-8807", "91330782098765432W", "504998877", "Bank of China Macau / Yiwu CIPS Direct", "CIPS_DIRECT_RMB", "CNY", 7125000.00, 7125000.00, 1.000000, "2026-04-28"),
        ("SAFE-2026-SH-90008", "97ed4827-7b6f-4491-a06f-b548d5a75008", "INV-PT-2026-9901", "91110000101123456N", "500265432", "Bank of China Shanghai FTZ Branch", "SWIFT_EUR", "EUR", 1522500.00, 11921175.00, 7.830000, "2026-05-06"),
        ("SAFE-2026-SH-90009", "97ed4827-7b6f-4491-a06f-b548d5a75009", "INV-PT-2026-9902", "91110000101123456N", "500077889", "Bank of China Shanghai FTZ Branch", "SWIFT_EUR", "EUR", 1885800.00, 14765814.00, 7.830000, "2026-05-12"),
        ("SAFE-2026-HQ-90010", "97ed4827-7b6f-4491-a06f-b548d5a75010", "INV-PT-2026-9903", "91440400MA56LUS01P", "500112233", "Bank of China Hengqin Branch", "SWIFT_EUR", "EUR", 1152200.00, 9033248.00, 7.840000, "2026-05-18"),
        ("SAFE-2026-QD-90011", "97ed4827-7b6f-4491-a06f-b548d5a75011", "INV-PT-2026-9905", "91110000101123456N", "508112244", "Agricultural Bank of China Qingdao", "SWIFT_EUR", "EUR", 1650000.00, 12927750.00, 7.835000, "2026-05-22"),
        ("SAFE-2026-SH-90012", "97ed4827-7b6f-4491-a06f-b548d5a75012", "INV-PT-2026-9904", "91370200163562681G", "500055214", "Bank of Communications Shanghai", "SWIFT_EUR", "EUR", 2100000.00, 16443000.00, 7.830000, "2026-05-26"),
        ("SAFE-2026-SZ-90013", "97ed4827-7b6f-4491-a06f-b548d5a75013", "INV-CN-2026-8808", "91440300618837699Q", "500697256", "ICBC Shenzhen Futian", "SWIFT_EUR", "EUR", 1840000.00, 14425600.00, 7.840000, "2026-05-29"),
        ("SAFE-2026-SZ-90014", "97ed4827-7b6f-4491-a06f-b548d5a75014", "INV-CN-2026-8813", "91440300192317458F", "500234567", "ICBC Shenzhen Pingshan", "SWIFT_EUR", "EUR", 8950000.00, 70168000.00, 7.840000, "2026-06-02"),
        ("SAFE-2026-BJ-90015", "97ed4827-7b6f-4491-a06f-b548d5a75015", "INV-CN-2026-8809", "91110108551385082Q", "500246810", "ICBC Beijing Haidian", "SWIFT_EUR", "EUR", 3200000.00, 25088000.00, 7.840000, "2026-06-05"),
        ("SAFE-2026-GZ-90016", "97ed4827-7b6f-4491-a06f-b548d5a75016", "INV-CN-2026-8810", "91440606190342599T", "500246810", "Bank of China Shunde", "SWIFT_EUR", "EUR", 1450000.00, 11368000.00, 7.840000, "2026-06-08"),
    ]

    # -------------------------------------------------------------------------
    # 49. cn_cargo_insurance_policies_sinosure (10 Insurance Policies - 9 columns)
    # CHECK (policy_type IN ('Marine All Risks ICC-A', 'Export Credit Risk SINOSURE', 'Railway Transit Risk'))
    # -------------------------------------------------------------------------
    data["insurances"] = [
        ("SINOSURE-2026-JS-1001", "SINOSURE", "CN-PT-CTR-2026-001", "220120260000108801", "Export Credit Risk SINOSURE", 7300000.00, 131400.00, 0, 0.00),
        ("PICC-MAR-2026-SZ-1002", "PICC Property & Casualty", "CN-PT-CTR-2026-002", "530120260000108802", "Marine All Risks ICC-A", 11260000.00, 230400.00, 0, 0.00),
        ("PINGAN-MAR-2026-ND-1004", "Ping An Marine", "CN-PT-CTR-2026-004", "310120260000108804", "Marine All Risks ICC-A", 4080000.00, 86400.00, 1, 185000.00),
        ("PICC-RAIL-2026-YW-1007", "PICC Property & Casualty", "CN-PT-CTR-2026-007", "292120260000108807", "Railway Transit Risk", 1085000.00, 28500.00, 0, 0.00),
        ("SINOSURE-2026-SN-1003", "SINOSURE", "CN-PT-CTR-2026-003", "220120260000108803", "Export Credit Risk SINOSURE", 4200000.00, 75600.00, 0, 0.00),
        ("PICC-MAR-2026-NB-1006", "PICC Property & Casualty", "CN-PT-CTR-2026-006", "310120260000108806", "Marine All Risks ICC-A", 3200000.00, 68000.00, 0, 0.00),
        ("PINGAN-MAR-2026-SZ-1008", "Ping An Marine", "CN-PT-CTR-2026-014", "530120260000108808", "Marine All Risks ICC-A", 2150000.00, 43000.00, 0, 0.00),
        ("SINOSURE-2026-SZ-1013", "SINOSURE", "CN-PT-CTR-2026-018", "530120260000108813", "Export Credit Risk SINOSURE", 10200000.00, 183600.00, 0, 0.00),
        ("PICC-AIR-2026-BJ-1005", "PICC Property & Casualty", "CN-PT-CTR-2026-005", "010120260000108805", "Marine All Risks ICC-A", 2850000.00, 39900.00, 0, 0.00),
        ("PINGAN-MAR-2026-GZ-1010", "Ping An Marine", "CN-PT-CTR-2026-016", "510120260000108810", "Marine All Risks ICC-A", 1680000.00, 33600.00, 0, 0.00),
    ]

    # -------------------------------------------------------------------------
    # 50. cn_state_industrial_subsidies (10 Subsidies - 7 columns)
    # -------------------------------------------------------------------------
    data["subsidies"] = [
        (1, "91320413MA1M9Y2C4B", "MIIT & Jiangsu Provincial New Energy Fund", "EV & Battery Innovation Grant", 2025, 185000000.00, "2025-09-15"),
        (2, "91440300192317458F", "Shenzhen Municipal NEV Global Expansion Program", "EV & Battery Innovation Grant", 2025, 310000000.00, "2025-11-20"),
        (3, "91610132724912345X", "Shaanxi Clean Tech Manufacturing Upgrade", "Photovoltaic Export Support", 2025, 95000000.00, "2025-08-10"),
        (4, "91330782098765432W", "Yiwu Municipal BRI China-Europe Railway Express Fund", "Belt & Road Rail Freight Subsidy", 2026, 18500000.00, "2026-02-01"),
        (5, "91330200778899112T", "Zhejiang Industrial Decarbonization Fund", "Green Factory Upgrade", 2026, 24000000.00, "2026-01-18"),
        (6, "91350900587527783P", "Fujian Energy Storage Technology Development Grant", "Grid Storage R&D Grant", 2025, 120000000.00, "2025-10-15"),
        (7, "91320400608131370B", "Jiangsu High-Efficiency Photovoltaic Innovation Program", "Photovoltaic Export Support", 2025, 65000000.00, "2025-07-22"),
        (8, "91440300618837699Q", "Guangdong Provincial Smart Grid R&D Incentive", "Renewable Electronics Grant", 2025, 88000000.00, "2025-12-05"),
        (9, "91440606190342599T", "Guangdong Green Appliance Export Decarbonization Subsidy", "Eco-Design & Energy Efficiency", 2026, 32000000.00, "2026-01-25"),
        (10, "911100007178071858", "National Rail Transit Core Technology Breakthrough Special Fund", "Rail Traction Systems Innovation", 2025, 150000000.00, "2025-06-30"),
    ]

    # -------------------------------------------------------------------------
    # 51. cn_outward_fdi_approvals_ndrc (8 FDI Approvals in Portugal - 9 columns)
    # CHECK (investment_mode IN ('M&A Equity Acquisition', 'Greenfield Gigafactory', 'Joint Venture', 'Port Terminal Concession'))
    # -------------------------------------------------------------------------
    data["fdi_approvals"] = [
        ("NDRC-ODI-2011-BJ-001", "91110000100001146K", "500697256", "EDP - Energias de Portugal, S.A. (21.4% Strategic Stake)", "M&A Equity Acquisition", 3510000000.00, 22464000000.00, "Energy Grid & Renewables", "2011-12-22"),
        ("NDRC-ODI-2012-BJ-002", "91110000710931234R", "503412890", "REN - Redes Energéticas Nacionais, SGPS, S.A. (25% Stake)", "M&A Equity Acquisition", 512000000.00, 3225600000.00, "National Transmission Grid", "2012-02-02"),
        ("NDRC-ODI-2014-SH-003", "91310000132234561L", "500918273", "Fidelidade - Companhia de Seguros, S.A. (85% Stake)", "M&A Equity Acquisition", 1360000000.00, 8432000000.00, "Financial Services & Insurance", "2014-05-15"),
        ("NDRC-ODI-2025-JS-004", "91320413MA1M9Y2C4B", "517890123", "CALB Portugal - Gigafábrica Zero-Carbon de Baterias em Sines (15 GWh)", "Greenfield Gigafactory", 2160000000.00, 15552000000.00, "New Energy EV Supply Chain", "2025-02-10"),
        ("NDRC-ODI-2014-SH-005", "91310000132234561L", "503112244", "Luz Saúde, S.A. (Hospital da Luz Acquisition)", "M&A Equity Acquisition", 610000000.00, 3782000000.00, "Healthcare Facilities", "2014-10-18"),
        ("NDRC-ODI-2016-SH-006", "91310000132234561L", "500998811", "Millennium bcp - Banco Comercial Português (29.95% Stake)", "M&A Equity Acquisition", 1120000000.00, 6944000000.00, "Banking & Commercial Finance", "2016-11-20"),
        ("NDRC-ODI-2020-BJ-007", "911100007178071858", "500191827", "Mota-Engil, SGPS, S.A. (32.4% Strategic Equity Stake)", "M&A Equity Acquisition", 205000000.00, 1312000000.00, "Global Construction & Infrastructure", "2020-11-27"),
        ("NDRC-ODI-2023-GD-008", "91440300192317458F", "509887766", "Kora Tech Hub Évora - Advanced Automotive R&D Center", "Joint Venture", 55000000.00, 396000000.00, "Automotive Software & R&D", "2023-04-12"),
    ]

    # -------------------------------------------------------------------------
    # 52. cn_green_manufacturing_esg_audits (10 ESG Audits - 9 columns)
    # -------------------------------------------------------------------------
    data["esg_audits"] = [
        (1, 101, 2025, 12500.00, 185000.00, 8420.500, 3903.500, 68.50, "China Quality Certification Centre (CQC-CNAS)"),
        (2, 102, 2025, 84000.00, 310000.00, 34200.000, 32340.000, 68.50, "SGS-CSTC Standards Technical Services Shenzhen"),
        (3, 103, 2025, 15000.00, 420000.00, 11200.000, 4125.000, 72.00, "TÜV Rheinland Greater China / CNAS"),
        (4, 104, 2025, 62000.00, 195000.00, 21500.000, 27342.000, 65.00, "CQC Xi'an Carbon Verification Bureau"),
        (5, 108, 2025, 295000.00, 82000.00, 168400.000, 191160.000, 85.00, "Sinocarbon Innovation & Investment Co. (CBAM Verifier)"),
        (6, 105, 2025, 45000.00, 280000.00, 18200.000, 19500.000, 70.00, "SGS-CSTC Standards Dongguan"),
        (7, 106, 2025, 38000.00, 165000.00, 14200.000, 16400.000, 68.50, "CQC Beijing Green Building Bureau"),
        (8, 110, 2025, 48000.00, 210000.00, 16500.000, 19800.000, 68.50, "TÜV NORD China CNAS"),
        (9, 111, 2025, 92000.00, 180000.00, 42000.000, 45200.000, 65.00, "China National Accreditation Service (CNAS)"),
        (10, 114, 2025, 185000.00, 95000.00, 82000.000, 91500.000, 75.00, "CQC Qingdao Industrial Energy Bureau"),
    ]

    # -------------------------------------------------------------------------
    # 91. cn_raw_materials_tier2_suppliers (8 Upstream Tier-2 Suppliers - 9 columns)
    # -------------------------------------------------------------------------
    data["tier2_suppliers"] = [
        ("SUP-T2-LI-001", "91360500716598112A", "Ganfeng Lithium Group Co., Ltd. (Jiangxi Refining)", "320400", "Battery Grade Lithium Carbonate", "Xinyu & Yichun Spodumene Refinery, Jiangxi", 120000.00, 1, 5.420),
        ("SUP-T2-LI-002", "91510900206360118B", "Tianqi Lithium Corporation (Sichuan Battery Grade)", "350900", "Battery Grade Lithium Carbonate", "Suining & Shehong Lithium Plant, Sichuan", 95000.00, 1, 5.180),
        ("SUP-T2-GR-003", "91440300723041998C", "BTR New Material Group Co., Ltd. (Shenzhen Anode)", "440300", "Anode Spherical Graphite", "Guangming High-Tech Park, Shenzhen", 180000.00, 1, 3.850),
        ("SUP-T2-LFP-004", "91320413MA1W88210D", "Hunan Yuneng New Energy Battery Material Co., Ltd.", "320400", "Cathode LFP Precursor", "Changzhou Jintan Cathode Industrial Park", 210000.00, 1, 4.120),
        ("SUP-T2-SI-005", "91510100679680114E", "Tongwei Solar & Yongxiang Polysilicon Co., Ltd.", "610100", "Solar Grade Polysilicon", "Leshan High-Purity Crystalline Silicon Base", 350000.00, 1, 8.950),
        ("SUP-T2-RE-006", "91150200701465882F", "China Northern Rare Earth (Group) High-Tech Co., Ltd.", "110000", "Rare Earth Neodymium Magnets", "Bayan Obo Rare Earth Complex, Baotou", 65000.00, 1, 11.200),
        ("SUP-T2-ST-007", "91310000132200821G", "Baoshan Iron & Steel Co., Ltd. (Baosteel Automotive)", "310000", "Automotive Grade Steel Coil", "Baoshan Special Steel Works, Shanghai", 850000.00, 1, 1.890),
        ("SUP-T2-GR-008", "91310000607388192H", "Shanghai Putailai New Energy Technology Co., Ltd.", "310000", "Anode Spherical Graphite", "Pudong Jinqiao Anode Coating Base, Shanghai", 140000.00, 1, 3.620),
    ]

    # -------------------------------------------------------------------------
    # 92. cn_production_lots_batch_genealogy (10 Production Lots - 9 columns)
    # -------------------------------------------------------------------------
    data["production_lots"] = [
        ("LOT-CALB-2026-03A", "CN-SKU-CALB-LFP314", 101, "SUP-T2-LI-001", "2026-03-05 08:00:00", "SHIFT-JINTAN-A1", 10000, 99.84, "SN-CALB314-202603A"),
        ("LOT-BYD-2026-03B", "CN-SKU-BYD-SEAL-EV", 102, "SUP-T2-GR-003", "2026-03-10 06:00:00", "SHIFT-PINGSHAN-B2", 400, 99.50, "VIN-LC0CE4DC-2026B"),
        ("LOT-LONGI-2026-04A", "CN-SKU-LONGI-HIMO7", 104, "SUP-T2-SI-005", "2026-03-20 07:30:00", "SHIFT-XIAN-PV1", 50000, 99.91, "SN-LG590W-202604A"),
        ("LOT-CATL-2026-04B", "CN-SKU-CATL-ENERC", 103, "SUP-T2-LI-002", "2026-03-28 08:00:00", "SHIFT-NINGDE-L1", 100, 99.95, "SN-ENERC-202604B"),
        ("LOT-XM-2026-04C", "CN-SKU-XM-15PRO-5G", 106, "SUP-T2-GR-008", "2026-04-04 09:00:00", "SHIFT-CHANGPING-DARK", 5000, 99.92, "IMEI-86994006-XM15"),
        ("LOT-NBST-2026-04D", "CN-SKU-NB-STEEL-S355", 108, "SUP-T2-ST-007", "2026-04-06 00:00:00", "SHIFT-BEILUN-BF2", 2000, 99.60, "HEAT-NBS355-202604D"),
        ("LOT-HW-2026-05A", "CN-SKU-HW-SUN2000", 105, "SUP-T2-RE-006", "2026-04-20 08:00:00", "SHIFT-SONGSHAN-S3", 800, 99.88, "SN-HWSUN2000-202605"),
        ("LOT-MD-2026-05C", "CN-SKU-MIDEA-SPLIT", 111, "SUP-T2-RE-006", "2026-04-25 07:00:00", "SHIFT-SHUNDE-AC1", 5000, 99.75, "SN-MIDEA12K-202605"),
        ("LOT-CRRC-2026-05D", "CN-SKU-CRRC-BOGIE", 114, "SUP-T2-ST-007", "2026-04-28 08:00:00", "SHIFT-SIFANG-BG1", 80, 100.00, "SN-CRRC-BOGIE-PT26"),
        ("LOT-BYD-2026-05E", "CN-SKU-BYD-ATTO3", 102, "SUP-T2-LFP-004", "2026-05-01 06:00:00", "SHIFT-PINGSHAN-A3", 350, 99.71, "VIN-LC0CE4CB-ATTO3"),
    ]

    # -------------------------------------------------------------------------
    # 93. cn_bill_of_materials_bom_structures (10 BOM Engineering Records - 8 columns)
    # -------------------------------------------------------------------------
    data["bom_structures"] = [
        ("BOM-CALB-314-01", "CN-SKU-CALB-LFP314", "SUP-T2-LI-001", "Battery-Grade Lithium Carbonate Li2CO3 Cathode Active Salt", "283691", 24.500, 38.40, 1),
        ("BOM-CALB-314-02", "CN-SKU-CALB-LFP314", "SUP-T2-LFP-004", "Iron Phosphate FePO4 Nano-Crystalline Precursor Powder", "283529", 68.000, 29.10, 1),
        ("BOM-CALB-314-03", "CN-SKU-CALB-LFP314", "SUP-T2-GR-003", "Coated Spherical Artificial Anode Graphite Powder", "380110", 36.200, 18.50, 1),
        ("BOM-BYD-SEAL-01", "CN-SKU-BYD-SEAL-EV", "SUP-T2-LFP-004", "BYD Blade LFP 82.5kWh Structural Battery Pack Assembly", "850760", 1120.000, 42.00, 1),
        ("BOM-BYD-SEAL-02", "CN-SKU-BYD-SEAL-EV", "SUP-T2-RE-006", "Permanent Magnet Synchronous Hairpin Traction Motor 230kW", "850153", 185.000, 19.80, 1),
        ("BOM-BYD-SEAL-03", "CN-SKU-BYD-SEAL-EV", "SUP-T2-ST-007", "Ultra-High-Strength Hot-Stamped Body-in-White Steel Frame", "870829", 1420.000, 24.50, 0),
        ("BOM-LONGI-PV-01", "CN-SKU-LONGI-HIMO7", "SUP-T2-SI-005", "N-Type HPDC Monocrystalline Silicon Solar Wafers M10", "381800", 14.800, 64.20, 1),
        ("BOM-CATL-ESS-01", "CN-SKU-CATL-ENERC", "SUP-T2-LI-002", "CATL 306Ah LFP Liquid-Cooled Cell Rack Cluster", "850760", 4850.000, 71.50, 1),
        ("BOM-HW-INV-01", "CN-SKU-HW-SUN2000", "SUP-T2-RE-006", "IGBT Power Module & Neodymium Inductive Reactor Core", "850490", 62.000, 58.00, 1),
        ("BOM-CRRC-BG-01", "CN-SKU-CRRC-BOGIE", "SUP-T2-ST-007", "Forged Alloy Steel Railway Wheelset & Frame Assembly", "860719", 9800.000, 82.40, 0),
    ]

    # -------------------------------------------------------------------------
    # 94. cn_letters_of_credit_ucp600_swift (10 UCP 600 Letters of Credit - 12 columns)
    # -------------------------------------------------------------------------
    data["letters_of_credit"] = [
        ("LC-BCP-BOC-2026-0001", "CN-PT-CTR-2026-001", "BCOMPTPLXXX", "BKCHCNBJ940", "PT517890123", "91320413MA1M9Y2C4B", "EUR", 18500000.00, "MT700 Issue", "2026-06-30", "2026-07-21", "Confirmed Irrevocable"),
        ("LC-CGD-CCB-2026-0003", "CN-PT-CTR-2026-003", "CGDIPTPLXXX", "PCBCCNBJSAX", "PT500697256", "91610132724912345X", "USD", 7280000.00, "MT700 Issue", "2026-05-30", "2026-06-15", "Confirmed Irrevocable"),
        ("LC-BPI-BOC-2026-0004", "CN-PT-CTR-2026-004", "BBPIPTPLXXX", "BKCHCNBJ720", "PT503412890", "91350900587527783P", "EUR", 10260000.00, "MT700 Issue", "2026-06-15", "2026-06-30", "Confirmed Irrevocable"),
        ("LC-BOC-BCP-2026-0008", "CN-PT-CTR-2026-008", "BKCHCNBJ300", "BCOMPTPLXXX", "91110000101123456N", "PT500265432", "EUR", 3450000.00, "MT700 Issue", "2026-05-15", "2026-05-31", "Confirmed Irrevocable"),
        ("LC-BOC-CGD-2026-0010", "CN-PT-CTR-2026-010", "BKCHCNBJ45A", "CGDIPTPLXXX", "91440400MA56LUS01P", "PT500112233", "EUR", 2680000.00, "MT700 Issue", "2026-05-25", "2026-06-10", "Unconfirmed Irrevocable"),
        ("LC-ABC-BPI-2026-0011", "CN-PT-CTR-2026-011", "ABOCCNBJ380", "BBPIPTPLXXX", "91110000101123456N", "PT508112244", "EUR", 4200000.00, "MT700 Issue", "2026-06-05", "2026-06-20", "Confirmed Irrevocable"),
        ("LC-BOC-BCP-2026-0012", "CN-PT-CTR-2026-012", "BKCHCNBJ300", "BCOMPTPLXXX", "91110000101123456N", "PT500214890", "EUR", 3100000.00, "MT707 Amend", "2026-06-10", "2026-06-25", "Confirmed Irrevocable"),
        ("LC-CGD-ICBC-2026-0014", "CN-PT-CTR-2026-014", "CGDIPTPLXXX", "ICBKCNBJSZN", "PT500697256", "91440300618837699Q", "EUR", 4800000.00, "MT700 Issue", "2026-06-20", "2026-07-05", "Confirmed Irrevocable"),
        ("LC-BCP-BOC-2026-0016", "CN-PT-CTR-2026-016", "BCOMPTPLXXX", "BKCHCNBJ400", "PT500246810", "91440606190342599T", "EUR", 3800000.00, "MT700 Issue", "2026-06-25", "2026-07-10", "Transferable LC"),
        ("LC-HTB-ICBC-2026-0017", "CN-PT-CTR-2026-017", "ESSIPTPLXXX", "ICBKCNBJBJM", "PT503412890", "911100007178071858", "EUR", 8500000.00, "MT700 Issue", "2026-07-01", "2026-07-15", "Confirmed Irrevocable"),
    ]

    # -------------------------------------------------------------------------
    # 95. cn_lc_documentary_presentations_discrepancies (10 Presentations - 9 columns)
    # -------------------------------------------------------------------------
    data["lc_presentations"] = [
        ("PRES-DOC-2026-001", "LC-BCP-BOC-2026-0001", "INV-CN-2026-8801", "COSU6288991101", "2026-03-25", 0, "Zero Discrepancies - Full UCP 600 Art. 14 Compliance", "Clean Presentation - Honored", "2026-03-28"),
        ("PRES-DOC-2026-003", "LC-CGD-CCB-2026-0003", "INV-CN-2026-8803", "COSU6288991103", "2026-04-06", 0, "Zero Discrepancies - eUCP 2.0 Electronic BL Validated", "Clean Presentation - Honored", "2026-04-09"),
        ("PRES-DOC-2026-004", "LC-BPI-BOC-2026-0004", "INV-CN-2026-8804", "COSU6288991104", "2026-04-13", 1, "Minor Typo in Notify Party Postal Code on Packing List (Waived by REN)", "Discrepant - Waived by Applicant", "2026-04-16"),
        ("PRES-DOC-2026-008", "LC-BOC-BCP-2026-0008", "INV-PT-2026-9901", "COSU6288992201", "2026-05-02", 0, "Zero Discrepancies - Symington Port Wine Origin & VI-1 Verified", "Clean Presentation - Honored", "2026-05-06"),
        ("PRES-DOC-2026-010", "LC-BOC-CGD-2026-0010", "INV-PT-2026-9903", "COSU6288992203", "2026-05-14", 0, "Zero Discrepancies - Hengqin FTZ Preferential Clearance", "Clean Presentation - Honored", "2026-05-18"),
        ("PRES-DOC-2026-011", "LC-ABC-BPI-2026-0011", "INV-PT-2026-9905", "COSU6288992205", "2026-05-19", 1, "Bilingual Mandarin Back-Label Font Height < 1.8mm (Rectified in Bond)", "Discrepant - Waived by Applicant", "2026-05-22"),
        ("PRES-DOC-2026-012", "LC-BOC-BCP-2026-0012", "INV-PT-2026-9906", "COSU6288992206", "2026-05-25", 0, "Zero Discrepancies - Full Compliance with UCP 600", "Clean Presentation - Honored", "2026-05-29"),
        ("PRES-DOC-2026-014", "LC-CGD-ICBC-2026-0014", "INV-CN-2026-8808", "COSU6288991108", "2026-05-26", 0, "Zero Discrepancies - Huawei Inverter IEC Certificate Attached", "Clean Presentation - Honored", "2026-05-29"),
        ("PRES-DOC-2026-016", "LC-BCP-BOC-2026-0016", "INV-CN-2026-8810", "COSU6288991110", "2026-06-04", 0, "Zero Discrepancies - Clean On-Board Bill of Lading", "Clean Presentation - Honored", "2026-06-08"),
        ("PRES-DOC-2026-017", "LC-HTB-ICBC-2026-0017", "INV-CN-2026-8811", "COSU6288991111", "2026-06-10", 0, "Documents Under Final Checking by Haitong Bank Lisbon", "Under Bank Examination", "2026-06-18"),
    ]

    # -------------------------------------------------------------------------
    # 96. cn_hk_macao_offshore_trading_intermediaries (8 Offshore Intermediaries - 9 columns)
    # -------------------------------------------------------------------------
    data["offshore_intermediaries"] = [
        ("OFF-MO-2026-001", "MO-SOE-28891-C", "Nam Kwong Lusophone International Trading Co., Ltd.", "Macao SAR", "91440400MA56LUS01P", "CN-PT-CTR-2026-010", 9033248.00, 1152200.00, "Bank of China Macau Branch (RMB Clearing Bank)"),
        ("OFF-HK-2026-002", "HK-CR-1928374", "BYD (H.K.) Co., Limited - Offshore Treasury & Auto Hub", "Hong Kong SAR", "91440300192317458F", "CN-PT-CTR-2026-002", 76104240.00, 9732000.00, "BOCHK Hong Kong Offshore CNH Clearing Center"),
        ("OFF-MO-2026-003", "MO-COM-88219-A", "Macau Legend & COFCO Lusophone Wine Distribution Lda.", "Macao SAR", "91110000101123456N", "CN-PT-CTR-2026-008", 11921175.00, 1522500.00, "BNU Macau / Banco Nacional Ultramarino"),
        ("OFF-HQ-2026-004", "HQ-FTZ-99102-Z", "Hengqin Sino-Portuguese Commodity Clearing Platform Ltd.", "Hengqin Offshore Zone", "91330782098765432W", "CN-PT-CTR-2026-007", 7125000.00, 910000.00, "ICBC Hengqin Free Trade Account (FTN) Center"),
        ("OFF-HK-2026-005", "HK-CR-2093811", "Xiaomi H.K. Limited - Global Supply Chain Treasury", "Hong Kong SAR", "91110108551385082Q", "CN-PT-CTR-2026-005", 19392240.00, 2473500.00, "HSBC Hong Kong Offshore Renminbi Desk"),
        ("OFF-MO-2026-006", "MO-INV-55412-B", "Chung Kiu (Macau) Agri-Food & Cork Import-Export Lda.", "Macao SAR", "91110000101123456N", "CN-PT-CTR-2026-009", 14765814.00, 1885800.00, "Luso International Banking Ltd. (LIB Macau)"),
        ("OFF-HK-2026-007", "HK-CR-3319022", "LONGi Solar Technology (H.K.) Limited", "Hong Kong SAR", "91610132724912345X", "CN-PT-CTR-2026-003", 26244400.00, 3640000.00, "Standard Chartered Bank (HK) CNH Settlement"),
        ("OFF-HQ-2026-008", "HQ-FTZ-77410-M", "China-Portugal Green Energy Equipment Leasing (Hengqin) Co.", "Hengqin Offshore Zone", "91320413MA1M9Y2C4B", "CN-PT-CTR-2026-001", 49136970.00, 6283500.00, "Bank of China Hengqin Cross-Border RMB Pool"),
    ]

    # -------------------------------------------------------------------------
    # 97. cn_freight_forwarders_nvocc_customs_brokers (8 NVOCC & Brokers - 8 columns)
    # -------------------------------------------------------------------------
    data["freight_forwarders"] = [
        ("BRK-CN-SINOTRANS-01", "91110000710930011X", "Sinotrans Limited (China National Foreign Trade Transportation)", "GACC-BRK-SH-0001", "MOC-NV00001", "CNSHA", "Advanced Certified Broker", 1450),
        ("BRK-CN-COSCO-LOG-02", "91310000710928812Y", "COSCO SHIPPING Logistics & Supply Chain Co., Ltd.", "GACC-BRK-NB-0008", "MOC-NV00012", "CNNGB", "Advanced Certified Broker", 1820),
        ("BRK-CN-KUEHNE-SZ-03", "91440300607411223Z", "Kuehne + Nagel (China) Ltd. Shenzhen Branch", "GACC-BRK-SZ-0042", "MOC-NV00105", "CNSZX", "Advanced Certified Broker", 940),
        ("BRK-CN-DHL-GLOBAL-04", "91310000607299104W", "DHL Global Forwarding (China) Co., Ltd.", "GACC-BRK-BJ-0019", "MOC-NV00088", "CNBJS", "Advanced Certified Broker", 1120),
        ("BRK-CN-YIWU-RAIL-05", "91330782558899110V", "Yiwu Timex Industrial Investment & BRI Rail Forwarding Co.", "GACC-BRK-YW-0102", "MOC-NV01822", "CNYIW", "General Certified Broker", 680),
        ("BRK-CN-CAINIAO-CB-06", "91440300MA5ECBEC6U", "Cainiao Customs Brokerage & Smart Clearance Shenzhen Ltd.", "GACC-BRK-SZ-0211", "MOC-NV02410", "CNSZX", "Advanced Certified Broker", 3200),
        ("BRK-CN-QINGDAO-PORT-07", "91370200163577889T", "Qingdao Port International Logistics & Customs Agency Co.", "GACC-BRK-QD-0015", "MOC-NV00319", "CNTAO", "Advanced Certified Broker", 790),
        ("BRK-CN-MACAO-CTS-08", "91440400192599001S", "China Travel Service (Macao/Zhuhai) Bonded Customs Brokers", "GACC-BRK-ZH-0033", "MOC-NV00944", "CNZUH", "General Certified Broker", 340),
    ]

    # -------------------------------------------------------------------------
    # 98. cn_packing_lists_pallet_carton_details (12 Granular Packing Lists - 10 columns)
    # -------------------------------------------------------------------------
    data["packing_lists"] = [
        ("PKL-CN-2026-8801", "INV-CN-2026-8801", "BRK-CN-SINOTRANS-01", "Heavy Duty Steel Skid", 250, 10000, 1936000.000, 2024000.000, 748.000, "CALB-SINES-PT // UN3480 LITHIUM // KEEP DRY // C/NO 1-250"),
        ("PKL-CN-2026-8802", "INV-CN-2026-8802", "BRK-CN-KUEHNE-SZ-03", "Heavy Duty Steel Skid", 400, 400, 1748000.000, 1780000.000, 5680.000, "BYD-CAETANO-PT // RO-RO DECK LASHING // WVTA EU"),
        ("PKL-CN-2026-8803", "INV-CN-2026-8803", "BRK-CN-SINOTRANS-01", "Fumigated Euro Pallet ISPM-15", 2100, 70000, 4690000.000, 4940000.000, 5920.000, "EDP-ALENTEJO-SOLAR // FRAGILE PV GLASS // IPPC CN-61001-HT"),
        ("PKL-CN-2026-8804", "INV-CN-2026-8804", "BRK-CN-COSCO-LOG-02", "Heavy Duty Steel Skid", 100, 100, 680000.000, 710000.000, 540.000, "REN-GRID-PORTUGAL // CATL ENERC // UN3480 CLASS 9"),
        ("PKL-CN-2026-8805", "INV-CN-2026-8805", "BRK-CN-DHL-GLOBAL-04", "Export Corrugated Master Carton", 45, 15000, 602200.000, 643100.000, 1406.000, "WORTEN-LISBOA // XIAOMI 5G // HIGH VALUE ELECTRONICS"),
        ("PKL-CN-2026-8806", "INV-CN-2026-8806", "BRK-CN-COSCO-LOG-02", "Heavy Duty Steel Skid", 320, 2485, 4971120.000, 5005000.000, 435.500, "MOTA-ENGIL-SINES // S355 STEEL & 6061 ALU // CBAM CERTIFIED"),
        ("PKL-CN-2026-8807", "INV-CN-2026-8807", "BRK-CN-YIWU-RAIL-05", "Export Corrugated Master Carton", 160, 4000, 368000.000, 396000.000, 720.000, "VARZIELA-PORTUGAL // YIXINOU BRI RAIL // COTTON APPAREL"),
        ("PKL-PT-2026-9901", "INV-PT-2026-9901", "BRK-CN-SINOTRANS-01", "Reefer Insulated Wine Case", 240, 30000, 270000.000, 504000.000, 410.000, "COFCO-SHANGHAI // SYMINGTON DOURO & PORT // REEFER +14C"),
        ("PKL-PT-2026-9902", "INV-PT-2026-9902", "BRK-CN-SINOTRANS-01", "Fumigated Euro Pallet ISPM-15", 180, 3000, 135000.000, 144000.000, 380.000, "AMORIM-CORK-PT // SO2 STERILE // FOOD GRADE STOPPER"),
        ("PKL-PT-2026-9903", "INV-PT-2026-9903", "BRK-CN-MACAO-CTS-08", "Reefer Insulated Wine Case", 210, 25000, 390000.000, 431000.000, 365.000, "HENGQIN-LUSOPHONE // SOVENA EXTRA VIRGIN OLIVE OIL"),
        ("PKL-PT-2026-9905", "INV-PT-2026-9905", "BRK-CN-QINGDAO-PORT-07", "Reefer Insulated Wine Case", 520, 32500, 1300000.000, 1364000.000, 890.000, "MAPORAL-PT // CIFER CPRT18000101000505 // KEEP FROZEN -18C"),
        ("PKL-PT-2026-9904", "INV-PT-2026-9904", "BRK-CN-QINGDAO-PORT-07", "Bulk Kraft Pulp Bale", 500, 4000, 4000000.000, 4040000.000, 2850.000, "NAVIGATOR-PULP-PT // FSC & EUDR CERTIFIED // QINGDAO PORT"),
    ]

    # -------------------------------------------------------------------------
    # 99. cn_processing_trade_manuals_handbook (8 E-Manuals - 9 columns)
    # -------------------------------------------------------------------------
    data["processing_manuals"] = [
        ("C23042600001", "91320413MA1M9Y2C4B", 6, "0615", "2836910000", "8507600090", 0.1392, 6420000.00, "Active Open Manual"),
        ("C53012600002", "91440300192317458F", 2, "0615", "8542319000", "8703800010", 4.0000, 12850000.00, "Active Open Manual"),
        ("C35092600003", "91350900587527783P", 7, "0615", "7410110000", "8507600090", 0.0850, 4920000.00, "Verified & Written Off"),
        ("C61012600004", "91610132724912345X", 8, "5034", "2804619000", "8541430000", 0.2250, 3180000.00, "Active Open Manual"),
        ("C44032600005", "91440300618837699Q", 2, "0615", "8542399000", "8504403090", 2.0000, 5640000.00, "Verified & Written Off"),
        ("C11012600006", "91110108551385082Q", 1, "0615", "8542319000", "8517130000", 1.0000, 8950000.00, "Active Open Manual"),
        ("C44062600007", "91440606190342599T", 2, "0214", "8414301900", "8415102100", 1.0000, 2150000.00, "Verified & Written Off"),
        ("C37022600008", "91370200163562681G", 10, "5034", "8529909090", "8528722100", 1.0000, 1940000.00, "Pending Bonded Balancing"),
    ]

    # -------------------------------------------------------------------------
    # 100. cn_gacc_aeo_mutual_recognition_registry (10 AEO MRA Links - 8 columns)
    # -------------------------------------------------------------------------
    data["aeo_mra_registry"] = [
        ("AEO-CN-JS-3204960012", "91320413MA1M9Y2C4B", "PT517890123", "CN-EU-AEO-MRA-2014", 0.80, 1, "2025-11-10", "2028-11-09"),
        ("AEO-CN-GD-4403160088", "91440300192317458F", "PT500234567", "CN-EU-AEO-MRA-2014", 1.20, 1, "2025-09-18", "2028-09-17"),
        ("AEO-CN-FJ-3509960001", "91350900587527783P", "PT503412890", "CN-EU-AEO-MRA-2014", 0.90, 1, "2025-10-22", "2028-10-21"),
        ("AEO-CN-SN-6101960022", "91610132724912345X", "PT500697256", "CN-EU-AEO-MRA-2014", 0.75, 1, "2025-08-14", "2028-08-13"),
        ("AEO-CN-BJ-1108960055", "91110108551385082Q", "PT500246810", "CN-EU-AEO-MRA-2014", 1.10, 1, "2025-12-01", "2028-11-30"),
        ("AEO-CN-BJ-1101960010", "91110000101123456N", "PT500265432", "CN-EU-AEO-MRA-2014", 1.00, 1, "2025-07-19", "2028-07-18"),
        ("AEO-CN-SH-3100960002", "91310000132209876M", "PT500077889", "CN-EU-AEO-MRA-2014", 0.65, 1, "2026-01-15", "2029-01-14"),
        ("AEO-CN-GD-4403960001", "91440300618837699Q", "PT500697256", "CN-EU-AEO-MRA-2014", 0.85, 1, "2025-06-30", "2028-06-29"),
        ("AEO-CN-SD-3702960015", "91370200163562681G", "PT500055214", "CN-EU-AEO-MRA-2014", 0.95, 1, "2025-10-05", "2028-10-04"),
        ("AEO-CN-BJ-1101960066", "911100007178071858", "PT500191827", "CN-EU-AEO-MRA-2014", 1.15, 1, "2025-11-28", "2028-11-27"),
    ]

    # -------------------------------------------------------------------------
    # 101. cn_export_control_dual_use_mofcom_permits (8 Dual-Use Permits - 9 columns)
    # -------------------------------------------------------------------------
    data["dual_use_permits"] = [
        ("DUAL-MOFCOM-2026-001", "91320413MA1M9Y2C4B", "220120260000108801", "CN-DU-2024-GRAPHITE-02", "Synthetic Spherical Anode Graphite Embedded in LFP Cells", "PT517890123", 1, "MOFCOM Bureau of Industry, Security, Import & Export Control", "2026-03-10"),
        ("DUAL-MOFCOM-2026-002", "91440300192317458F", "530120260000108802", "CN-DU-2025-NDM-05", "High-Coercivity Samarium-Cobalt / NdFeB Permanent Traction Magnets", "PT500234567", 1, "MOFCOM Bureau of Industry, Security, Import & Export Control", "2026-03-15"),
        ("DUAL-MOFCOM-2026-003", "91350900587527783P", "310120260000108804", "CN-DU-2025-LFP-CATHODE", "High-Compaction Density LFP Cathode Material (>300Wh/kg Tech)", "PT503412890", 1, "MOFCOM & MIIT Joint Strategic Technology Panel", "2026-04-01"),
        ("DUAL-MOFCOM-2026-004", "91330200778899112T", "310120260000108806", "CN-DU-2024-ALLOY-72", "High-Tensile Corrosion-Resistant Marine/Offshore Alloy Steel", "PT500191827", 1, "MOFCOM Zhejiang Provincial Department", "2026-04-10"),
        ("DUAL-MOFCOM-2026-005", "91440300618837699Q", "530120260000108808", "CN-DU-2024-GAN-RF09", "Gallium Nitride (GaN) High-Frequency Power Amplifier Modules", "PT500697256", 1, "MOFCOM Bureau of Industry, Security, Import & Export Control", "2026-04-22"),
        ("DUAL-MOFCOM-2026-006", "911100007178071858", "010120260000108811", "CN-DU-2025-RAIL-IGBT", "High-Voltage Traction Converter Control Units (3300V IGBT)", "PT503412890", 1, "MOFCOM Beijing Municipal Commission of Commerce", "2026-04-30"),
        ("DUAL-MOFCOM-2026-007", "91440300192317458F", "530120260000108813", "CN-DU-2025-NDM-05", "Rare-Earth Permanent Magnet Synchronous EV Drive Units", "PT500234567", 1, "MOFCOM Bureau of Industry, Security, Import & Export Control", "2026-05-05"),
        ("DUAL-MOFCOM-2026-008", "91610132724912345X", "220120260000108803", "CN-DU-2024-WAFER-INGOT", "Large-Diameter Monocrystalline Silicon Ingot Puller Specification", "PT500697256", 1, "MOFCOM Shaanxi Provincial Commerce Department", "2026-03-25"),
    ]

    # -------------------------------------------------------------------------
    # 102. cn_preferential_certificates_of_origin_ccpit (10 CO Certificates - 8 columns)
    # -------------------------------------------------------------------------
    data["certificates_of_origin"] = [
        ("CCPIT-CO-26320400101", "220120260000108801", "91320413MA1M9Y2C4B", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 86.00, "CCPIT Jiangsu Sub-Council (Changzhou)", "SHA256-9A8B7C6D5E4F3A2B1C0D9E8F7A6B5C4D"),
        ("CCPIT-CO-26440300202", "530120260000108802", "91440300192317458F", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 88.30, "CCPIT Shenzhen Municipal Committee", "SHA256-1F2E3D4C5B6A79880796857463524130"),
        ("GACC-CO-26610100303", "220120260000108803", "91610132724912345X", "GACC General Certificate of Origin", "PE - Produced Exclusively", 94.20, "Xi'an Customs District GACC", "SHA256-445566778899AABBCCDDEEFF00112233"),
        ("CCPIT-CO-26350900404", "310120260000108804", "91350900587527783P", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 91.50, "CCPIT Fujian Sub-Council (Ningde)", "SHA256-77889900112233445566778899AABBCC"),
        ("CCPIT-CO-26110100505", "010120260000108805", "91110108551385082Q", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 76.40, "CCPIT Beijing Sub-Council", "SHA256-AABBCCDDEEFF00112233445566778899"),
        ("GACC-CO-26330200606", "310120260000108806", "91330200778899112T", "GACC General Certificate of Origin", "WO - Wholly Obtained", 96.00, "Ningbo Customs District GACC", "SHA256-11223344556677889900AABBCCDDEEFF"),
        ("CCPIT-CO-26330700707", "292120260000108807", "91330782098765432W", "Non-Preferential CO CCPIT", "PE - Produced Exclusively", 98.50, "CCPIT Yiwu Chamber of International Commerce", "SHA256-99887766554433221100FFEEDDCCBBAA"),
        ("CCPIT-CO-26440300808", "530120260000108808", "91440300618837699Q", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 84.00, "CCPIT Shenzhen Municipal Committee", "SHA256-5566778899AABBCC0011223344556677"),
        ("GACC-CO-26440601010", "510120260000108810", "91440606190342599T", "GACC General Certificate of Origin", "PE - Produced Exclusively", 92.00, "Foshan Customs District GACC", "SHA256-3344556677889900AABBCCDDEEFF1122"),
        ("CCPIT-CO-26110101111", "010120260000108811", "911100007178071858", "Non-Preferential CO CCPIT", "PSR - Substantial Transformation", 95.10, "CCPIT Beijing Sub-Council", "SHA256-6677889900112233445566778899AABB"),
    ]

    # -------------------------------------------------------------------------
    # 103. cn_customs_tariff_quotas_antidumping_mofcom (8 MOFCOM Measures - 8 columns)
    # -------------------------------------------------------------------------
    data["mofcom_measures"] = [
        ("MOF-AD-2026-PORK-01", "0203290090", "220120261000990005", "MOFCOM Announcement No. 23 of 2024 (EU Pork Investigation)", "EU Pork Anti-Dumping Investigation Deposit", 4.90, 412580.00, "PT508112244"),
        ("MOF-AD-2026-PORK-02", "0203290090", "370220261000990010", "MOFCOM Announcement No. 23 of 2024 (EU Pork Investigation)", "EU Pork Anti-Dumping Investigation Deposit", 4.90, 545159.30, "PT502889900"),
        ("MOF-MFN-2026-WINE-03", "2204210000", "220120261000990001", "GACC Tariff Schedule 2026 (Table & Fortified Wine)", "MFN Standard Zero Measure", 0.00, 0.00, "PT500265432"),
        ("MOF-MFN-2026-CORK-04", "4504900000", "220120261000990002", "GACC Green Packaging Tariff Reduction 2026", "MFN Standard Zero Measure", 0.00, 0.00, "PT500077889"),
        ("MOF-TRQ-2026-OLIVE-05", "1509200000", "530420261000990003", "Hengqin Lusophone Foodstuff Facilitation Notice 2026", "Agricultural Tariff Rate Quota TRQ", 0.00, 0.00, "PT500112233"),
        ("MOF-MFN-2026-PULP-06", "4703290000", "370220261000990007", "GACC Zero-Tariff Raw Wood Pulp Schedule 2026", "MFN Standard Zero Measure", 0.00, 0.00, "PT500055214"),
        ("MOF-MFN-2026-WINE-07", "2204210000", "220120261000990006", "GACC Tariff Schedule 2026 (Douro DOC Wine)", "MFN Standard Zero Measure", 0.00, 0.00, "PT500214890"),
        ("MOF-TRQ-2026-OLIVE-08", "1509200000", "530120261000990008", "GACC Edible Oil Import Monitoring Schedule 2026", "Agricultural Tariff Rate Quota TRQ", 0.00, 0.00, "PT500876543"),
    ]

    # -------------------------------------------------------------------------
    # 104. cn_customs_tax_guarantees_consolidated_bonds (8 Customs Bonds - 8 columns)
    # -------------------------------------------------------------------------
    data["customs_bonds"] = [
        ("BOND-GACC-SH-2026-01", "91110000101123456N", "Bank of China Shanghai FTZ Branch", "Consolidated Monthly Taxation Bond", 50000000.00, 14250000.00, "2201", "2026-12-31"),
        ("BOND-GACC-QD-2026-02", "91110000101123456N", "Agricultural Bank of China Qingdao", "Anti-Dumping Provisional Security Bond", 15000000.00, 957739.30, "3702", "2026-12-31"),
        ("BOND-GACC-HQ-2026-03", "91440400MA56LUS01P", "Bank of China Zhuhai Hengqin Branch", "Consolidated Monthly Taxation Bond", 20000000.00, 3850000.00, "5304", "2026-12-31"),
        ("BOND-GACC-NB-2026-04", "91330200778899112T", "Bank of Communications Ningbo Branch", "Consolidated Monthly Taxation Bond", 40000000.00, 8120000.00, "3101", "2026-12-31"),
        ("BOND-GACC-QD-2026-05", "91370200163562681G", "China Construction Bank Qingdao", "Consolidated Monthly Taxation Bond", 60000000.00, 11400000.00, "3702", "2026-12-31"),
        ("BOND-GACC-SZ-2026-06", "91440300755673010C", "PICC Property & Casualty Tariff Bond Division", "Transit Customs Bond", 35000000.00, 6200000.00, "5301", "2026-12-31"),
        ("BOND-GACC-JS-2026-07", "91320413MA1M9Y2C4B", "Bank of China Changzhou Branch", "Transit Customs Bond", 80000000.00, 18500000.00, "2304", "2026-12-31"),
        ("BOND-GACC-SH-2026-08", "91310000132234561L", "Industrial Bank Shanghai Head Office", "Consolidated Monthly Taxation Bond", 30000000.00, 4120000.00, "2201", "2026-12-31"),
    ]

    # -------------------------------------------------------------------------
    # 105. cn_advance_rulings_classification_valuation_gacc (8 Advance Rulings - 8 columns)
    # -------------------------------------------------------------------------
    data["advance_rulings"] = [
        ("RUL-GACC-SH-2025-0101", "91320413MA1M9Y2C4B", "Tariff Classification HS10", "8507600090", "Integrated LFP Liquid-Cooled Prismatic Battery Module with BMS Slave Board", "Shanghai Customs Classification Center", "2025-06-01", 3),
        ("RUL-GACC-SZ-2025-0202", "91440300192317458F", "Tariff Classification HS10", "8703800010", "Dual-Motor All-Wheel-Drive Passenger BEV with CTB Blade Battery Architecture", "Shenzhen Customs Tariff Division", "2025-07-15", 3),
        ("RUL-GACC-SH-2025-0303", "91110000101123456N", "Customs Valuation Methodology", "2204210000", "Deductive & Transaction Value Ruling for Symington Port Wine Marketing Royalties", "Shanghai Customs Valuation Bureau", "2025-09-10", 3),
        ("RUL-GACC-GZ-2025-0404", "91440400MA56LUS01P", "Origin Determination", "1509200000", "Portuguese Alentejo DOP Extra Virgin Olive Oil Bottled for Macao-Hengqin CEPA", "Gongbei Customs Origin Office", "2025-10-20", 3),
        ("RUL-GACC-NB-2025-0505", "91350900587527783P", "Tariff Classification HS10", "8507600090", "Containerized 20ft Utility-Scale LFP BESS Outdoor Rack (Classified as Accumulator)", "Ningbo Customs Classification Center", "2025-11-05", 3),
        ("RUL-GACC-SZ-2025-0606", "91440300618837699Q", "Tariff Classification HS10", "8504403090", "Three-Phase 100kW String PV Inverter with PID Recovery & Arc-Fault Circuit Interrupter", "Shenzhen Customs Tariff Division", "2025-12-12", 3),
        ("RUL-GACC-QD-2026-0707", "91370200163562681G", "Origin Determination", "4703290000", "Wholly Obtained Portuguese Eucalyptus Globulus Bleached Kraft Pulp Bales", "Qingdao Customs Tariff & Origin Bureau", "2026-01-18", 3),
        ("RUL-GACC-BJ-2026-0808", "911100007178071858", "Tariff Classification HS10", "8607191000", "Complete Motorized Metro Bogie Sub-Assembly with Pneumatic Suspension", "Beijing Customs Tariff Division", "2026-02-05", 3),
    ]

    # -------------------------------------------------------------------------
    # 106. cn_post_clearance_audits_anti_smuggling_gacc (8 Post-Clearance Audits - 8 columns)
    # -------------------------------------------------------------------------
    data["post_clearance_audits"] = [
        ("PCA-GACC-2026-SH-001", "91320413MA1M9Y2C4B", "220120260000108801", "Shanghai Customs Enterprise Audit Bureau (Jicha)", "Export VAT Rebate Authenticity", "Compliant - No Adjustment", 0.00, "2026-05-10"),
        ("PCA-GACC-2026-SZ-002", "91440300192317458F", "530120260000108802", "Shenzhen Customs Post-Clearance Audit Division", "Transfer Pricing & Royalties Valuation", "Compliant - No Adjustment", 0.00, "2026-05-18"),
        ("PCA-GACC-2026-SH-003", "91110000101123456N", "220120261000990001", "Shanghai Waigaoqiao Customs Audit Bureau", "Transfer Pricing & Royalties Valuation", "Voluntary Disclosure Accepted", 42500.00, "2026-05-28"),
        ("PCA-GACC-2026-SH-004", "91110000101123456N", "220120261000990005", "Shanghai Port Cold-Chain Supervision Bureau", "CIFER Cold-Chain Traceability", "Compliant - No Adjustment", 0.00, "2026-06-04"),
        ("PCA-GACC-2026-YW-005", "91330782098765432W", "292120260000108807", "Hangzhou/Yiwu Customs Audit Division", "HS Code Misclassification Check", "Supplementary Tax Assessed", 18400.00, "2026-06-08"),
        ("PCA-GACC-2026-NB-006", "91330200778899112T", "310120260000108806", "Ningbo Customs Industrial Metals Audit Team", "Export VAT Rebate Authenticity", "Compliant - No Adjustment", 0.00, "2026-06-11"),
        ("PCA-GACC-2026-HQ-007", "91440400MA56LUS01P", "530420261000990003", "Gongbei/Hengqin Customs Bonded Audit Division", "CIFER Cold-Chain Traceability", "Compliant - No Adjustment", 0.00, "2026-06-14"),
        ("PCA-GACC-2026-QD-008", "91370200163562681G", "370220261000990007", "Qingdao Customs Enterprise Compliance Bureau", "Transfer Pricing & Royalties Valuation", "Compliant - No Adjustment", 0.00, "2026-06-16"),
    ]

    # -------------------------------------------------------------------------
    # 107. cn_excise_consumption_tax_sta (8 Consumption Tax Records - 8 columns)
    # -------------------------------------------------------------------------
    data["consumption_taxes"] = [
        ("CT-STA-2026-SH-001", "220120261000990001", "2204210000", "Imported Grape Wine Consumption Tax (进口葡萄酒消费税 10%)", 10.00, 0.00, 1510015.50, "STA-CT-3100-2026-990001"),
        ("CT-STA-2026-SH-002", "220120261000990006", "2204210000", "Imported Grape Wine Consumption Tax (进口葡萄酒消费税 10%)", 10.00, 0.00, 1231494.00, "STA-CT-3100-2026-990006"),
        ("CT-STA-2026-SH-003", "220120261000990002", "4504900000", "Exempt Industrial Cork Articles (软木制品免征消费税)", 0.00, 0.00, 0.00, "STA-CT-3100-2026-990002"),
        ("CT-STA-2026-HQ-004", "530420261000990003", "1509200000", "Exempt Edible Olive Oil (食用橄榄油免征消费税)", 0.00, 0.00, 0.00, "STA-CT-4404-2026-990003"),
        ("CT-STA-2026-SH-005", "220120261000990005", "0203290090", "Exempt Frozen Swine Meat (冻猪肉免征消费税)", 0.00, 0.00, 0.00, "STA-CT-3100-2026-990005"),
        ("CT-STA-2026-QD-006", "370220261000990007", "4703290000", "Exempt Wood Pulp Raw Material (木浆免征消费税)", 0.00, 0.00, 0.00, "STA-CT-3702-2026-990007"),
        ("CT-STA-2026-SZ-007", "530120261000990008", "1509200000", "Exempt Edible Olive Oil (食用橄榄油免征消费税)", 0.00, 0.00, 0.00, "STA-CT-4403-2026-990008"),
        ("CT-STA-2026-QD-008", "370220261000990010", "0203290090", "Exempt Frozen Swine Meat (冻猪肉免征消费税)", 0.00, 0.00, 0.00, "STA-CT-3702-2026-990010"),
    ]

    # -------------------------------------------------------------------------
    # 108. cn_ipr_customs_protection_recordations (8 GACC IPR Recordations - 8 columns)
    # -------------------------------------------------------------------------
    data["ipr_recordations"] = [
        ("IPR-GACC-2025-TM-001", "PT500265432", "GRAHAM'S PORT & SYMINGTON DOURO DOC", "Geographical Indication GI Douro/Porto", "CNIPA-GI-2019-DOURO01", "COFCO Wines & Spirits Import & Export Co., Ltd. (91110000101123456N)", "White-Listed Authorized Channel", "2034-12-31"),
        ("IPR-GACC-2025-TM-002", "PT500214890", "MATEUS ROSÉ & QUINTA DA LEDA SOGRAPE", "Registered Trademark CNIPA", "CNIPA-TM-11928374", "COFCO Wines & Spirits Import & Export Co., Ltd. (91110000101123456N)", "White-Listed Authorized Channel", "2033-10-15"),
        ("IPR-GACC-2025-PT-003", "PT500077889", "AMORIM NATURAL CORK & NDTECH ANTI-TCA", "Invention Patent CNIPA", "ZL202180019283.4", "COFCO Wines & Spirits / Fosun Wine & Spirits Shanghai", "Active Border Protection", "2035-06-30"),
        ("IPR-GACC-2025-TM-004", "PT500112233", "OLIVEIRA DA SERRA & ANDORINHA SOVENA", "Registered Trademark CNIPA", "CNIPA-TM-22839102", "Guangdong-Macao Lusophone Park Trading (91440400MA56LUS01P)", "White-Listed Authorized Channel", "2032-08-20"),
        ("IPR-GACC-2025-PT-005", "91440300192317458F", "BYD BLADE BATTERY & E-PLATFORM 3.0", "Invention Patent CNIPA", "ZL202010293847.1", "Salvador Caetano Auto S.A. Portugal (PT500234567)", "White-Listed Authorized Channel", "2035-12-31"),
        ("IPR-GACC-2025-PT-006", "91320413MA1M9Y2C4B", "CALB CIRRUS ULTRA-LOW CARBON LFP TABLESS CELL", "Invention Patent CNIPA", "ZL202310887766.5", "CALB Portugal S.A. Sines Gigafactory (PT517890123)", "White-Listed Authorized Channel", "2036-03-15"),
        ("IPR-GACC-2025-TM-007", "91110108551385082Q", "XIAOMI HYPEROS & MI LOGO", "Registered Trademark CNIPA", "CNIPA-TM-88371920", "Worten Equipamentos para o Lar S.A. (PT500246810)", "Active Border Protection", "2034-05-01"),
        ("IPR-GACC-2026-TM-008", "91330782098765432W", "LUXURY EUROPEAN FASHION BRAND PROTECTION (YIWU BORDER)", "Registered Trademark CNIPA", "CNIPA-TM-99001122", "Unauthorized Counterfeit Garment Alert on Rail Consignment", "Detention Triggered", "2031-12-31"),
    ]

    return data
