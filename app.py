import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit setup
st.title("Stock Valuation and Financial Analysis Tool")

# Define the list of stocks
list_of_stocks = ['786', 'AABS', 'AAL', 'AASM', 'AATM', 'ABL', 'ABOT', 'ABSON', 'ACPL', 'ADAMS', 'ADMM', 'AGHA', 
                  'AGIC', 'AGIL', 'AGL', 'AGLNCPS', 'AGP', 'AGSML', 'AGTL', 'AHCL', 'AHL', 'AHTM', 'AICL', 'AIRLINK', 
                  'AKBL', 'AKDHL', 'AKDSL', 'AKGL', 'ALAC', 'ALIFE', 'ALNRS', 'ALTN', 'AMBL', 'AMSL', 'AMTEX', 'ANL', 
                  'ANLNV', 'ANLPS', 'ANNT', 'ANSM', 'ANTM', 'APL', 'APOT', 'ARCTM', 'ARPAK', 'ARPL', 'ARUJ', 'ASC',
                  'ASHT', 'ASIC', 'ASL', 'ASLCPS', 'ASLPS', 'ASTL', 'ASTM', 'ATBA', 'ATIL', 'ATLH', 'ATRL', 'AVN', 'AWTX',
                  'AZMT', 'BAFL', 'BAFS', 'BAHL', 'BAPL', 'BATA', 'BBFL', 'BCL', 'BECO', 'BELA', 'BERG', 'BFBIO',
                  'BFMOD', 'BGL', 'BHAT', 'BIFO', 'BIIC', 'BILF', 'BIPL', 'BML', 'BNL', 'BNWM', 'BOK', 'BOP', 'BPL',
                  'BRRG', 'BTL', 'BUXL', 'BWCL', 'BWHL', 'CASH', 'CCM', 'CENI', 'CEPB', 'CFL', 'CHAS', 'CHBL', 'CHCC',
                  'CJPL', 'CLCPS', 'CLOV', 'CLVL', 'CNERGY', 'COLG', 'CPHL', 'CPPL', 'CRTM', 'CSAP', 'CSIL', 'CTM',
                  'CWSM', 'CYAN', 'DAAG', 'DADX', 'DAWH', 'DBCI', 'DBSL', 'DCL', 'DCR', 'DCTL', 'DEL', 'DFML',
                  'DFSM', 'DGKC', 'DIIL', 'DINT', 'DKTM', 'DLL', 'DMTM', 'DMTX', 'DNCC', 'DOL', 'DSFL', 'DSIL', 'DSL',
                  'DSML', 'DWAE', 'DWSM', 'DWTM', 'DYNO', 'ECOP', 'EFERT', 'EFGH', 'EFUG', 'EFUL', 'ELCM', 'ELSM', 'EMCO',
                  'ENGL', 'ENGRO', 'EPCL', 'EPCLPS', 'EPQL', 'ESBL', 'EWIC', 'EXIDE', 'FABL', 'FAEL', 'FANM', 'FASM', 'FATIMA',
                  'FCCL', 'FCEL', 'FCEPL', 'FCIBL', 'FCL', 'FCONM', 'FCSC', 'FDPL', 'FECM', 'FECTC', 'FEM',
                  'FEROZ', 'FFBL', 'FFC', 'FFL', 'FFLM', 'FHAM', 'FIBLM', 'FIL', 'FIM', 'FIMM', 'FLYNG', 'FML', 'FNBM', 'FNEL', 'FPJM',
                  'FPRM', 'FRCL', 'FRSM', 'FSWL', 'FTHM', 'FTMM', 'FTSM', 'FZCM', 'GADT', 'GAL', 'GAMON', 'GATI', 'GATM', 'GCIL', 'GEMBCEM',
                  'GEMBLUEX', 'GEMMEL', 'GEMPAPL', 'GEMSPNL', 'GFIL', 'GGGL', 'GGL', 'GHGL', 'GHNI', 'GIL', 'GLAXO', 'GLOT', 'GLPL', 'GOC', 'GRR', 'GRYL',
                  'GSPM', 'GTYR', 'GUSM', 'GUTM', 'GVGL', 'GWLC', 'HABSM', 'HADC', 'HAEL', 'HAFL', 'HAJT', 'HALEON', 'HASCOL',
                  'HATM', 'HBL', 'HCAR', 'HCL', 'HGFA', 'HICL', 'HIFA', 'HINO', 'HINOON', 'HIRAT', 'HKKT', 'HMB', 'HMIM', 'HPL', 'HRPL', 'HSPI', 'HTL', 'HUBC', 'HUMNL', 'HUSI',
                  'HWQS', 'IBFL', 'IBLHL', 'ICCI', 'ICIBL', 'ICL', 'IDRT', 'IDSM', 'IDYM', 'IGIHL', 'IGIL', 'ILP', 'IMAGE', 'IML', 'INDU', 'INIL', 'INKL', 'INMF',
                  'IPAK', 'ISIL', 'ISL', 'ITTEFAQ', 'JATM', 'JDMT', 'JDWS', 'JGICL', 'JKSM', 'JLICL', 'JSBL', 'JSCL', 'JSCLPSA', 'JSGCL', 'JSIL', 'JSML',
                  'JUBS', 'JVDC', 'JVDCPS', 'KAKL', 'KAPCO', 'KCL', 'KEL', 'KHTC', 'KHYT', 'KML', 'KOHC', 'KOHE', 'KOHP', 'KOHTM', 'KOIL',
                  'KOSM', 'KPUS', 'KSBP', 'KSTM', 'KTML', 'LCI', 'LEUL', 'LMSM', 'LOADS', 'LOTCHEM', 'LPGL', 'LPL', 'LSECL', 'LSEFSL', 'LSEVL', 'LUCK', 'MACFL', 'MACTER', 'MARI',
                  'MCB', 'MCBIM', 'MDTL', 'MEBL', 'MEHT', 'MERIT', 'MFFL', 'MFL', 'MFTM', 'MIRKS', 'MLCF', 'MOHE', 'MQTM', 'MRNS', 'MSCL', 'MSOT', 'MSOTPS',
                  'MTL', 'MUBT', 'MUGHAL', 'MUREB', 'MWMP', 'NAFL', 'NAGC', 'NATF', 'NATM', 'NBP', 'NCL', 'NCML', 'NCPL', 'NESTLE', 'NETSOL', 'NEXT', 'NICL', 'NINA', 'NMFL', 'NML',
                  'NONS', 'NPL', 'NRL', 'NRSL', 'NSRM', 'OBOY', 'OCTOPUS', 'OGDC', 'OLPL', 'OLPM', 'OML', 'ORM', 'OTSU', 'PABC', 'PACE', 'PAEL', 'PAKD',
                  'PAKL', 'PAKOXY', 'PAKRI', 'PAKT', 'PASL', 'PASM', 'PCAL', 'PECO', 'PELPS', 'PGLC', 'PHDL', 'PIAHCLA', 'PIAHCLB', 'PIBTL', 'PICL', 'PICT', 'PIL', 'PIM', 'PINL', 'PIOC',
                  'PKGI', 'PKGP', 'PKGS', 'PMI', 'PMPK', 'PMRS', 'PNSC', 'POL', 'POML', 'POWER', 'POWERPS', 'PPL', 'PPP', 'PPVC', 'PREMA', 'PRET', 'PRIB', 'PRIC', 'PRL',
                  'PRWM', 'PSEL', 'PSO', 'PSX', 'PSYL', 'PTC', 'PTL', 'PUDF', 'QUET', 'QUICE', 'RCML', 'REDCO', 'REGAL', 'REWM', 'RICL', 'RMPL', 'RPL', 'RUBY', 'RUPL', 'SAIF', 'SANE', 'SANSM', 'SAPT',
                  'SARC', 'SASML', 'SAZEW', 'SBL', 'SCBPL', 'SCL', 'SDOT', 'SEARL', 'SEL', 'SEPL', 'SERT', 'SFAT', 'SFL', 'SGABL', 'SGF', 'SGPL',
                  'SHCI', 'SHCM', 'SHDT', 'SHEL', 'SHEZ', 'SHFA', 'SHJS', 'SHNI', 'SHSML', 'SIBL', 'SICL', 'SIEM', 'SILK', 'SINDM', 'SITC', 'SKRS', 'SLCL', 'SLCPA',
                  'SLGL', 'SLL', 'SLYT', 'SMCPL', 'SML', 'SNAI', 'SNBL', 'SNGP', 'SPEL', 'SPL', 'SPLC', 'SPWL', 'SRVI', 'SSGC', 'SSIC', 'SSML', 'SSOM', 'STCL', 'STJT',
                  'STML', 'STPL', 'STYLERS', 'SUHJ', 'SURAJ', 'SURC', 'SUTM', 'SYM', 'SYS', 'SZTM', 'TAJT', 'TATM', 'TBL', 'TCORP', 'TCORPCPS', 'TELE', 'TGL',
                  'THALL', 'THCCL', 'TICL', 'TOMCL', 'TOWL', 'TPL', 'TPLI', 'TPLP', 'TPLRF1', 'TPLT', 'TREET', 'TRG', 'TRIBL', 'TRIPF', 'TRSM', 'TSBL', 'TSMF', 'TSML',
                  'TSPL', 'UBDL', 'UBL', 'UCAPM', 'UDLI', 'UDPL', 'UNIC', 'UNITY', 'UPFL', 'USMT', 'UVIC', 'WAHN', 'WAVES', 'WAVESAPP', 'WTL', 'YOUW', 'ZAHID', 'ZELP']

# Streamlit dropdown for stock selection
stock_symbol = st.selectbox("Select a stock symbol:", options=list_of_stocks)

# Function to fetch financial data
def get_financial_data(stock_symbol):
    urls = {
        "income_statement": f"https://stockanalysis.com/quote/psx/{stock_symbol}/financials/",
        "balance_sheet": f"https://stockanalysis.com/quote/psx/{stock_symbol}/financials/balance-sheet/",
        "cash_flow": f"https://stockanalysis.com/quote/psx/{stock_symbol}/financials/cash-flow-statement/",
        "ratios": f"https://stockanalysis.com/quote/psx/{stock_symbol}/financials/ratios/"
    }
    data = {}
    for key, url in urls.items():
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            # Make the request with headers
            response = requests.get(url, headers=headers)
            data[key] = pd.read_html(response.text)[0]
            # dropping the second header
            data[key].columns = data[key].columns.droplevel(1)

            # transpose the dataframe and reset the column
            data[key] = data[key].T
            data[key].columns = data[key].iloc[0]
            data[key] = data[key][1:]

            # Cleaning the data (for converting object data to numeric)
            # Find all columns where '%' sign is present
            percent_columns = [col for col in data[key].columns if data[key][col].astype(object).str.contains('%').any()]

            # Add '%' sign to column names
            data[key].rename(columns={col: f"{col} (%)" for col in percent_columns}, inplace=True)

            # dropping last row that contains "Upgrade" in all columns
            data[key].drop(index = data[key].index[-1], axis = 0, inplace = True)

            # replacing empty data with 0
            data[key].replace('-', '0', inplace=True)

            # replacing % with ''
            data[key] = data[key].replace('%', '', regex=True)
            data[key].head()

            data[key] = data[key].astype(float)
            data[key]['Year'] = ['TTM', '2024', '2023', '2022', '2021', '2020']
        except Exception as e:
            st.error(f"Error retrieving data from {url}: {e}")
    return data

# Plotting function
def plot_dataframe(data):
    income_metrics = ['Revenue', 'Revenue Growth (YoY) (%)', 'Gross Margin (%)', 'Operating Margin (%)', 'Profit Margin (%)', 'Interest Expense']
    balance_metrics = ['Cash & Equivalents', 'Property, Plant & Equipment', 'Long-Term Debt', 'Retained Earnings', 'Book Value Per Share']
    cash_metrics = ['Free Cash Flow', 'Free Cash Flow Per Share']
    ratio_metrics = ['Debt / Equity Ratio', 'Current Ratio', 'Return on Equity (ROE) (%)', 'Return on Assets (ROA) (%)', 'Return on Capital (ROIC) (%)']

    for key, df in data.items():
        if st.checkbox(f"Show plots for {key.replace('_', ' ').title()}"):
            st.write(f"Available columns in {key}: {', '.join(df.columns)}")
            if key == 'income_statement':
                for metric in income_metrics:
                    if metric in df.columns:
                        st.bar_chart(df, x='Year', y=metric)
            elif key == 'balance_sheet':
                for metric in balance_metrics:
                    if metric in df.columns:
                        st.bar_chart(df, x='Year', y=metric)
            elif key == 'cash_flow':
                for metric in cash_metrics:
                    if metric in df.columns:
                        st.bar_chart(df, x='Year', y=metric)
            elif key == 'ratios':
                for metric in ratio_metrics:
                    if metric in df.columns:
                        st.bar_chart(df, x='Year', y=metric)

# Streamlit sidebar for valuation method selection
st.sidebar.header("Valuation Method")
method = st.sidebar.radio("Select Valuation Method:", options=["Gordon Growth Model (GGM)", "Discounted Cash Flow (DCF)", "PEG Ratio"])

# User inputs for valuation
if method == "Gordon Growth Model (GGM)":
    st.sidebar.subheader("Gordon Growth Model (GGM) Inputs")
    dividend = st.sidebar.number_input("Expected dividend next year (PKR):", min_value=0.0, step=0.1)
    growth_rate_ggm = st.sidebar.number_input("Dividend growth rate (%):", min_value=0.0, step=0.1) / 100
    required_rate = st.sidebar.number_input("Required rate of return (%):", min_value=0.1, step=0.1) / 100

    # Display GGM valuation result
    if st.sidebar.button("Calculate GGM"):
        if required_rate <= growth_rate_ggm:
            st.sidebar.error("Required return must be greater than the growth rate.")
        else:
            ggm_valuation = dividend / (required_rate - growth_rate_ggm)
            st.sidebar.success(f"GGM Valuation: PKR {ggm_valuation:,.2f}")

elif method == "Discounted Cash Flow (DCF)":
    st.sidebar.subheader("Discounted Cash Flow (DCF) Inputs")
    recent_free_cash_flow = st.sidebar.number_input("Most recent free cash flow (PKR):", min_value=0.0, step=1000.0)
    growth_rate_dcf = st.sidebar.number_input("Free cash flow growth rate (%):", min_value=0.0, step=0.1) / 100
    discount_rate_dcf = st.sidebar.number_input("Discount rate (%):", min_value=0.0, step=0.1) / 100

    # Display DCF valuation result
    if st.sidebar.button("Calculate DCF"):
        projected_cash_flows = []
        for year in range(1, 6):
            future_cash_flow = recent_free_cash_flow * ((1 + growth_rate_dcf) ** year)
            present_value = future_cash_flow / ((1 + discount_rate_dcf) ** year)
            projected_cash_flows.append(present_value)
        dcf_valuation = sum(projected_cash_flows)
        st.sidebar.success(f"DCF Valuation: PKR {dcf_valuation:,.2f}")

elif method == "PEG Ratio":
    st.sidebar.subheader("PEG Ratio Inputs")
    pe_ratio = st.sidebar.number_input("P/E Ratio:", min_value=0.0, step=0.1)
    growth_rate_peg = st.sidebar.number_input("Growth rate (%):", min_value=0.0, step=0.1)

    # Display PEG ratio result
    if st.sidebar.button("Calculate PEG"):
        if growth_rate_peg == 0:
            st.sidebar.error("Growth rate cannot be zero.")
        else:
            peg = pe_ratio / growth_rate_peg
            st.sidebar.success(f"PEG Ratio: {peg:.2f}")

# Fetch and display data
if stock_symbol:
    st.subheader(f"Financial Data for {stock_symbol}")
    data = get_financial_data(stock_symbol)
    if data:
        plot_dataframe(data)
