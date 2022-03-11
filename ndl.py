import nasdaqdatalink
import pandas as pd
import mariadb

nasdaqdatalink.read_key("C:/bin/api-keys/nasdaq-data-link")

# ticker = input("Which stock would you like Sharadar data for?\n>> ")

# data = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)

# df = data.iloc[1]
# name = df.loc['name']

def print_fin(ticker):
    nasdaq_info = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)
    company = nasdaq_info.iloc[1]
    name = company.loc['name']
    sicsector = company.loc['sicsector']
    sicindustry = company.loc['sicindustry']
    famaindustry = company.loc['famaindustry']
    sector = company.loc['sector']
    industry = company.loc['industry']
    scalemarketcap = company.loc['scalemarketcap']
    scalerevenue = company.loc['scalerevenue']


    financials = nasdaqdatalink.get_table('SHARADAR/SF1',dimension='MRY',ticker=ticker)
    nasdaq_financials = financials.iloc[1]
# financial data variables
    ticker = ticker
    date = str(nasdaq_financials.loc['calendardate'])
    datekey = nasdaq_financials.loc['datekey']
    reportperiod = nasdaq_financials.loc['reportperiod']
    lastupdated = nasdaq_financials.loc['lastupdated']
    accoci = int(nasdaq_financials.loc['accoci'])
    assets = int(nasdaq_financials.loc['assets'])
    assetsavg = int(nasdaq_financials.loc['assetsavg'])
    assetsc = int(nasdaq_financials.loc['assetsc'])
    assetsnc = int(nasdaq_financials.loc['assetsnc'])
    assetturnover = int(nasdaq_financials.loc['assetturnover'])
    bvps = int(nasdaq_financials.loc['bvps'])
    capex = int(nasdaq_financials.loc['capex'])
    cashneq = int(nasdaq_financials.loc['cashneq'])
    cashnequsd = int(nasdaq_financials.loc['cashnequsd'])
    cor = int(nasdaq_financials.loc['cor'])
    consolinc = int(nasdaq_financials.loc['consolinc'])
    currentratio = int(nasdaq_financials.loc['currentratio'])
    de = int(nasdaq_financials.loc['de'])
    debt = int(nasdaq_financials.loc['debt'])
    debtc = int(nasdaq_financials.loc['debtc'])
    debtnc = int(nasdaq_financials.loc['debtnc'])
    debtusd = int(nasdaq_financials.loc['debtusd'])
    deferredrev = int(nasdaq_financials.loc['deferredrev'])
    depamor = int(nasdaq_financials.loc['depamor'])
    deposits = int(nasdaq_financials.loc['deposits'])
    divyield = int(nasdaq_financials.loc['divyield'])
    dps = int(nasdaq_financials.loc['dps'])
    ebit = int(nasdaq_financials.loc['ebit'])
    ebitda = int(nasdaq_financials.loc['ebitda'])
    ebitdamargin = int(nasdaq_financials.loc['ebitdamargin'])
    ebitdausd = int(nasdaq_financials.loc['ebitdausd'])
    ebitusd = int(nasdaq_financials.loc['ebitusd'])
    ebt = int(nasdaq_financials.loc['ebt'])
    eps = int(nasdaq_financials.loc['eps'])
    epsdil = int(nasdaq_financials.loc['epsdil'])
    epsusd = int(nasdaq_financials.loc['epsusd'])
    equity = int(nasdaq_financials.loc['equity'])
    equityavg = int(nasdaq_financials.loc['equityavg'])
    equityusd = int(nasdaq_financials.loc['equityusd'])
    ev = int(nasdaq_financials.loc['ev'])
    evebit = int(nasdaq_financials.loc['evebit'])
    fcf = int(nasdaq_financials.loc['fcf'])
    fcfps = int(nasdaq_financials.loc['fcfps'])
    fxusd = int(nasdaq_financials.loc['fxusd'])
    gp = int(nasdaq_financials.loc['gp'])
    grossmargin = int(nasdaq_financials.loc['grossmargin'])
    intangibles = int(nasdaq_financials.loc['intangibles'])
    intexp = int(nasdaq_financials.loc['intexp'])
    invcap = int(nasdaq_financials.loc['invcap'])
    inventory = int(nasdaq_financials.loc['inventory'])
    investments = int(nasdaq_financials.loc['investments'])
    investmentsc = int(nasdaq_financials.loc['investmentsc'])
    investmentsnc = int(nasdaq_financials.loc['investmentsnc'])
    liabilities = int(nasdaq_financials.loc['liabilities'])
    liabilitiesc = int(nasdaq_financials.loc['liabilitiesc'])
    liabilitiesnc = int(nasdaq_financials.loc['liabilitiesnc'])
    marketcap = int(nasdaq_financials.loc['marketcap'])
    ncf = int(nasdaq_financials.loc['ncf'])
    ncfbus = int(nasdaq_financials.loc['ncfbus'])
    ncfcommon = int(nasdaq_financials.loc['ncfcommon'])
    ncfdebt = int(nasdaq_financials.loc['ncfdebt'])
    ncfdiv = int(nasdaq_financials.loc['ncfdiv'])
    ncff = int(nasdaq_financials.loc['ncff'])
    ncfi = int(nasdaq_financials.loc['ncfi'])
    ncfinv = int(nasdaq_financials.loc['ncfinv'])
    ncfo = int(nasdaq_financials.loc['ncfo'])
    ncfx = int(nasdaq_financials.loc['ncfx'])
    netinc = int(nasdaq_financials.loc['netinc'])
    netinccmn = int(nasdaq_financials.loc['netinccmn'])
    netinccmnusd = int(nasdaq_financials.loc['netinccmnusd'])
    netincdis = int(nasdaq_financials.loc['netincdis'])
    netincnci = int(nasdaq_financials.loc['netincnci'])
    netmargin = int(nasdaq_financials.loc['netmargin'])
    opex = int(nasdaq_financials.loc['opex'])
    opinc = int(nasdaq_financials.loc['opinc'])
    payables = int(nasdaq_financials.loc['payables'])
    payoutratio = int(nasdaq_financials.loc['payoutratio'])
    pb = int(nasdaq_financials.loc['pb'])
    pe = int(nasdaq_financials.loc['pe'])
    pe1 = int(nasdaq_financials.loc['pe1'])
    ppnenet = int(nasdaq_financials.loc['ppnenet'])
    prefdivis = int(nasdaq_financials.loc['prefdivis'])
    price = int(nasdaq_financials.loc['price'])
    ps = int(nasdaq_financials.loc['ps'])
    ps1 = int(nasdaq_financials.loc['ps1'])
    receivables = int(nasdaq_financials.loc['receivables'])
    retearn = int(nasdaq_financials.loc['retearn'])
    revenue = int(nasdaq_financials.loc['revenue'])
    revenueusd = int(nasdaq_financials.loc['revenueusd'])
    rnd = int(nasdaq_financials.loc['rnd'])
    roa = int(nasdaq_financials.loc['roa'])
    roe = int(nasdaq_financials.loc['roe'])
    roic = int(nasdaq_financials.loc['roic'])
    ros = int(nasdaq_financials.loc['ros'])
    sbcomp = int(nasdaq_financials.loc['sbcomp'])
    sgna = int(nasdaq_financials.loc['sgna'])
    sharefactor = int(nasdaq_financials.loc['sharefactor'])
    sharesbas = int(nasdaq_financials.loc['sharesbas'])
    shareswa = int(nasdaq_financials.loc['shareswa'])
    shareswadil = int(nasdaq_financials.loc['shareswadil'])
    sps = int(nasdaq_financials.loc['sps'])
    tangibles = int(nasdaq_financials.loc['tangibles'])
    taxassets = int(nasdaq_financials.loc['taxassets'])
    taxexp = int(nasdaq_financials.loc['taxexp'])
    taxliabilities = int(nasdaq_financials.loc['taxliabilities'])
    tbvps = int(nasdaq_financials.loc['tbvps'])
    workingcapital = int(nasdaq_financials.loc['workingcapital'])

    #     # cashneq, cashnequsd, cor, consolinc, currentratio, de, debt, debtc, \
    #     # debtnc, debtusd, deferredrev, depamor, deposits, divyield, dps, ebit, \
    #     # ebitda, ebitdamargin, ebitdausd, ebitusd, ebt, epsusd, epsdil, epsusd, \
    #     # equity, equityavg, equityusd, ev, evebit, fcf, fcfps, fxusd, gp, \
    #     # grossmargin, intangibles, intexp, invcap, inventory, investments, \
    #     # investmentsc, investmentsnc, liabilities, liabilitiesc, liabilitiesnc, \
    #     # marketcap, ncf, ncfbus, ncfcommon, ncfdebt, ncfdiv, ncff, ncfi, ncfinv, \
    #     # ncfo, ncfx, netinc, netinccmn, netinccmnusd, netincdis, netincnci, \
    #     # netmargin, opex, opinc, payables, payoutratio, pb, pe, pe1, ppnenet, \
    #     # prefdivis, price, ps, ps1, receivables, retearn, revenue, revenueusd, \
    #     # rnd, roa, roe, roic, ros, sbcomp, sgna, sharefactor, sharesbas, \
    #     # shareswa, shareswadil, sps, tangibles, taxassets, taxexp, \
    #     # taxliabilities, tbvps, workingcapital)
    #     cur.execute(statement,data)

# connect to db
    exists = False
    try:
        conn = mariadb.connect(
            user = 'Win',
            password = 'birdhouse',
            host = "192.168.190.198",
            port = 3306,
            database = 'stocks',
        )
        cur = conn.cursor()
    except mariadb.Error as e:
        print(f"Failed to connect to financials table: {e}")
# check if financials are already uploaded
    statement = "SELECT * from financials where ticker='"+ticker+"'"
    cur.execute(statement)
    row = cur.fetchone()
    if row:
      print("Already included in database.")
    else:
        try:
            statement = "INSERT INTO financials (ticker, date, accoci, assets, \
            assetsavg, assetsc, assetsnc, assetturnover, bvps, capex) VALUES \
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (ticker, date, accoci, assets, assetsavg, assetsc, assetsnc, \
            assetturnover, bvps, capex)
            cur.execute(statement,data)
            conn.commit()
            print("Successfully added first ten values of financials to database")
        except mariadb.Error as e:
            print(f"Error adding financials to database: {e}")
    # cashneq
        try:
            statement = "UPDATE financials SET cashneq='"+str(cashneq)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added cashneq: "+str(cashneq)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding cashneq: "+str(cashneq)+" to database: {e}")
    # cashnequsd
        try:
            statement = "UPDATE financials SET cashnequsd='"+str(cashnequsd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added cashnequsd: "+str(cashnequsd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding "+str(cashnequsd)+" to database: {e}")
    # cor
        try:
            statement = "UPDATE financials SET cor='"+str(cor)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added cor: "+str(cor)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding cor: "+str(cor)+" to database: {e}")
    # consolinc
        try:
            statement = "UPDATE financials SET consolinc='"+str(consolinc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added consolinc: "+str(consolinc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding consolinc: "+str(consolinc)+" to database: {e}")
    # currentratio
        try:
            statement = "UPDATE financials SET currentratio='"+str(currentratio)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added currentratio: "+str(currentratio)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding currentratio: "+str(currentratio)+" to database: {e}")
    # de
        try:
            statement = "UPDATE financials SET de='"+str(de)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added de: "+str(de)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding de: "+str(de)+" to database: {e}")
    # debt
        try:
            statement = "UPDATE financials SET debt='"+str(debt)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added debt: "+str(debt)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding debt: "+str(debt)+" to database: {e}")
    # debtc
        try:
            statement = "UPDATE financials SET debtc='"+str(debtc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added debtc: "+str(debtc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding debtc: "+str(debtc)+" to database: {e}")
    # debtnc
        try:
            statement = "UPDATE financials SET debtnc='"+str(debtnc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added debtnc: "+str(debtnc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding debtnc: "+str(debtnc)+" to database: {e}")
    # debtusd
        try:
            statement = "UPDATE financials SET debtusd='"+str(debtusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added debtusd: "+str(debtusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding debtusd: "+str(debtusd)+" to database: {e}")
    # deferredrev
        try:
            statement = "UPDATE financials SET deferredrev='"+str(deferredrev)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added deferredrev: "+str(deferredrev)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding deferredrev: "+str(deferredrev)+" to database: {e}")
    # depamor
        try:
            statement = "UPDATE financials SET depamor='"+str(depamor)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added depamor: "+str(depamor)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding depamor: "+str(depamor)+" to database: {e}")
    # deposits
        try:
            statement = "UPDATE financials SET deposits='"+str(deposits)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added deposits: "+str(deposits)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding deposits: "+str(deposits)+" to database: {e}")
    # divyield
        try:
            statement = "UPDATE financials SET divyield='"+str(divyield)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added divyield: "+str(divyield)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding divyield: "+str(divyield)+" to database: {e}")
    # dps
        try:
            statement = "UPDATE financials SET dps='"+str(dps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added dps: "+str(dps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding dps: "+str(dps)+" to database: {e}")
    # ebit
        try:
            statement = "UPDATE financials SET ebit='"+str(ebit)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ebit: "+str(ebit)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ebit: "+str(ebit)+" to database: {e}")
    # ebitda
        try:
            statement = "UPDATE financials SET ebitda='"+str(ebitda)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ebitda: "+str(ebitda)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ebitda: "+str(ebitda)+" to database: {e}")
    # ebitdamargin
        try:
            statement = "UPDATE financials SET ebitdamargin='"+str(ebitdamargin)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ebitdamargin: "+str(ebitdamargin)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ebitdamargin: "+str(ebitdamargin)+" to database: {e}")
    # ebitdausd
        try:
            statement = "UPDATE financials SET ebitdausd='"+str(ebitdausd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ebitdausd: "+str(ebitdausd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ebitdausd: "+str(ebitdausd)+" to database: {e}")
    # ebitusd
        try:
            statement = "UPDATE financials SET ebitusd='"+str(ebitusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ebitusd: "+str(ebitusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ebitusd: "+str(ebitusd)+" to database: {e}")
    # eps
        try:
            statement = "UPDATE financials SET eps='"+str(eps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added eps: "+str(eps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding eps: "+str(eps)+" to database: {e}")
    # epsdil
        try:
            statement = "UPDATE financials SET epsdil='"+str(epsdil)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added epsdil: "+str(epsdil)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding epsdil: "+str(epsdil)+" to database: {e}")
    # epsusd
        try:
            statement = "UPDATE financials SET epsusd='"+str(epsusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added epsusd: "+str(epsusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding epsusd: "+str(epsusd)+" to database: {e}")
    # equity
        try:
            statement = "UPDATE financials SET equity='"+str(equity)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added equity: "+str(equity)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding equity: "+str(equity)+" to database: {e}")
    # equityavg
        try:
            statement = "UPDATE financials SET equityavg='"+str(equityavg)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added equityavg: "+str(equityavg)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding equityavg: "+str(equityavg)+" to database: {e}")
    # equityusd
        try:
            statement = "UPDATE financials SET equityusd='"+str(equityusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added equityusd: "+str(equityusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding equityusd: "+str(equityusd)+" to database: {e}")
    # ev
        try:
            statement = "UPDATE financials SET ev='"+str(ev)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ev: "+str(ev)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ev: "+str(ev)+" to database: {e}")
    # evebit
        try:
            statement = "UPDATE financials SET evebit='"+str(evebit)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added evebit: "+str(evebit)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding evebit: "+str(evebit)+" to database: {e}")
    # fcf
        try:
            statement = "UPDATE financials SET fcf='"+str(fcf)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added fcf: "+str(fcf)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding fcf: "+str(fcf)+" to database: {e}")
    # fcfps
        try:
            statement = "UPDATE financials SET fcfps='"+str(fcfps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added fcfps: "+str(fcfps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding fcfps: "+str(fcfps)+" to database: {e}")
    # fxusd
        try:
            statement = "UPDATE financials SET fxusd='"+str(fxusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added fxusd: "+str(fxusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding fxusd: "+str(fxusd)+" to database: {e}")
    # gp
        try:
            statement = "UPDATE financials SET gp='"+str(gp)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added gp: "+str(gp)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding gp: "+str(gp)+" to database: {e}")
    # grossmargin
        try:
            statement = "UPDATE financials SET grossmargin='"+str(grossmargin)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added grossmargin: "+str(grossmargin)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding grossmargin: "+str(grossmargin)+" to database: {e}")
    # intangibles
        try:
            statement = "UPDATE financials SET intangibles='"+str(intangibles)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added intangibles: "+str(intangibles)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding intangibles: "+str(intangibles)+" to database: {e}")
    # intexp
        try:
            statement = "UPDATE financials SET intexp='"+str(intexp)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added intexp: "+str(intexp)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding intexp: "+str(intexp)+" to database: {e}")
    # invcap
        try:
            statement = "UPDATE financials SET invcap='"+str(invcap)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added invcap: "+str(invcap)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding invcap: "+str(invcap)+" to database: {e}")
    # inventory
        try:
            statement = "UPDATE financials SET inventory='"+str(inventory)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added inventory: "+str(inventory)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding inventory: "+str(inventory)+" to database: {e}")
    # investments
        try:
            statement = "UPDATE financials SET investments='"+str(investments)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added investments: "+str(investments)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding investments: "+str(investments)+" to database: {e}")
    # investmentsc
        try:
            statement = "UPDATE financials SET investmentsc='"+str(investmentsc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added investmentsc: "+str(investmentsc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding investmentsc: "+str(investmentsc)+" to database: {e}")
    # investmentsnc
        try:
            statement = "UPDATE financials SET investmentsnc='"+str(investmentsnc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added investmentsnc: "+str(investmentsnc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding investmentsnc: "+str(investmentsnc)+" to database: {e}")
    # liabilities
        try:
            statement = "UPDATE financials SET liabilities='"+str(liabilities)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added liabilities: "+str(liabilities)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding liabilities: "+str(liabilities)+" to database: {e}")
    # liabilitiesc
        try:
            statement = "UPDATE financials SET liabilitiesc='"+str(liabilitiesc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added liabilitiesc: "+str(liabilitiesc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding liabilitiesc: "+str(liabilitiesc)+" to database: {e}")
    # liabilitiesnc
        try:
            statement = "UPDATE financials SET liabilitiesnc='"+str(liabilitiesnc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added liabilitiesnc: "+str(liabilitiesnc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding liabilitiesnc: "+str(liabilitiesnc)+" to database: {e}")
    # marketcap
        try:
            statement = "UPDATE financials SET marketcap='"+str(marketcap)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added marketcap: "+str(marketcap)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding marketcap: "+str(marketcap)+" to database: {e}")
    # ncf
        try:
            statement = "UPDATE financials SET ncf='"+str(ncf)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncf: "+str(ncf)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncf: "+str(ncf)+" to database: {e}")
    # ncfbus
        try:
            statement = "UPDATE financials SET ncfbus='"+str(ncfbus)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfbus: "+str(ncfbus)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfbus: "+str(ncfbus)+" to database: {e}")
    # ncfcommon
        try:
            statement = "UPDATE financials SET ncfcommon='"+str(ncfcommon)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfcommon: "+str(ncfcommon)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfcommon: "+str(ncfcommon)+" to database: {e}")
    # ncfdebt
        try:
            statement = "UPDATE financials SET ncfdebt='"+str(ncfdebt)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfdebt: "+str(ncfdebt)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfdebt: "+str(ncfdebt)+" to database: {e}")
    # ncfdiv
        try:
            statement = "UPDATE financials SET ncfdiv='"+str(ncfdiv)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfdiv: "+str(ncfdiv)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfdiv: "+str(ncfdiv)+" to database: {e}")
    # ncff
        try:
            statement = "UPDATE financials SET ncff='"+str(ncff)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncff: "+str(ncff)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncff: "+str(ncff)+" to database: {e}")
    # ncfi
        try:
            statement = "UPDATE financials SET ncfi='"+str(ncfi)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfi: "+str(ncfi)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfi: "+str(ncfi)+" to database: {e}")
    # ncfinv
        try:
            statement = "UPDATE financials SET ncfinv='"+str(ncfinv)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfinv: "+str(ncfinv)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfinv: "+str(ncfinv)+" to database: {e}")
    # ncfo
        try:
            statement = "UPDATE financials SET ncfo='"+str(ncfo)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfo: "+str(ncfo)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfo: "+str(ncfo)+" to database: {e}")
    # ncfx
        try:
            statement = "UPDATE financials SET ncfx='"+str(ncfx)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ncfx: "+str(ncfx)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ncfx: "+str(ncfx)+" to database: {e}")
    # netinc
        try:
            statement = "UPDATE financials SET netinc='"+str(netinc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netinc: "+str(netinc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netinc: "+str(netinc)+" to database: {e}")
    # netinccmn
        try:
            statement = "UPDATE financials SET netinccmn='"+str(netinccmn)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netinccmn: "+str(netinccmn)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netinccmn: "+str(netinccmn)+" to database: {e}")
    # netinccmnusd
        try:
            statement = "UPDATE financials SET netinccmnusd='"+str(netinccmnusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netinccmnusd: "+str(netinccmnusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netinccmnusd: "+str(netinccmnusd)+" to database: {e}")
    # netincdis
        try:
            statement = "UPDATE financials SET netincdis='"+str(netincdis)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netincdis: "+str(netincdis)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netincdis: "+str(netincdis)+" to database: {e}")
    # netincnci
        try:
            statement = "UPDATE financials SET netincnci='"+str(netincnci)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netincnci: "+str(netincnci)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netincnci: "+str(netincnci)+" to database: {e}")
    # netmargin
        try:
            statement = "UPDATE financials SET netmargin='"+str(netmargin)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added netmargin: "+str(netmargin)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding netmargin: "+str(netmargin)+" to database: {e}")
    # opex
        try:
            statement = "UPDATE financials SET opex='"+str(opex)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added opex: "+str(opex)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding opex: "+str(opex)+" to database: {e}")
    # opinc
        try:
            statement = "UPDATE financials SET opinc='"+str(opinc)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added opinc: "+str(opinc)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding opinc: "+str(opinc)+" to database: {e}")
    # payables
        try:
            statement = "UPDATE financials SET payables='"+str(payables)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added payables: "+str(payables)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding payables: "+str(payables)+" to database: {e}")
    # payoutratio
        try:
            statement = "UPDATE financials SET payoutratio='"+str(payoutratio)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added payoutratio: "+str(payoutratio)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding payoutratio: "+str(payoutratio)+" to database: {e}")
    # pb
        try:
            statement = "UPDATE financials SET pb='"+str(pb)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added pb: "+str(pb)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding pb: "+str(pb)+" to database: {e}")
    # pe
        try:
            statement = "UPDATE financials SET pe='"+str(pe)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added pe: "+str(pe)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding pe: "+str(pe)+" to database: {e}")
    # pe1
        try:
            statement = "UPDATE financials SET pe1='"+str(pe1)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added pe1: "+str(pe1)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding pe1: "+str(pe1)+" to database: {e}")
    # ppnenet
        try:
            statement = "UPDATE financials SET ppnenet='"+str(ppnenet)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ppnenet: "+str(ppnenet)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ppnenet: "+str(ppnenet)+" to database: {e}")
    # prefdivis
        try:
            statement = "UPDATE financials SET prefdivis='"+str(prefdivis)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added prefdivis: "+str(prefdivis)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding prefdivis: "+str(prefdivis)+" to database: {e}")
    # price
        try:
            statement = "UPDATE financials SET price='"+str(price)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added price: "+str(price)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding price: "+str(price)+" to database: {e}")
    # ps
        try:
            statement = "UPDATE financials SET ps='"+str(ps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ps: "+str(ps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ps: "+str(ps)+" to database: {e}")
    # ps1
        try:
            statement = "UPDATE financials SET ps1='"+str(ps1)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ps1: "+str(ps1)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ps1: "+str(ps1)+" to database: {e}")
    # receivables
        try:
            statement = "UPDATE financials SET receivables='"+str(receivables)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added receivables: "+str(receivables)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding receivables: "+str(receivables)+" to database: {e}")
    # retearn
        try:
            statement = "UPDATE financials SET retearn='"+str(retearn)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added retearn: "+str(retearn)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding retearn: "+str(retearn)+" to database: {e}")
    # revenue
        try:
            statement = "UPDATE financials SET revenue='"+str(revenue)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added revenue: "+str(revenue)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding revenue: "+str(revenue)+" to database: {e}")
    # revenueusd
        try:
            statement = "UPDATE financials SET revenueusd='"+str(revenueusd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added revenueusd: "+str(revenueusd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding revenueusd: "+str(revenueusd)+" to database: {e}")
    # rnd
        try:
            statement = "UPDATE financials SET rnd='"+str(rnd)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added rnd: "+str(rnd)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding rnd: "+str(rnd)+" to database: {e}")
    # roa
        try:
            statement = "UPDATE financials SET roa='"+str(roa)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added roa: "+str(roa)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding roa: "+str(roa)+" to database: {e}")
    # roe
        try:
            statement = "UPDATE financials SET roe='"+str(roe)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added roe: "+str(roe)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding roe: "+str(roe)+" to database: {e}")
    # roic
        try:
            statement = "UPDATE financials SET roic='"+str(roic)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added roic: "+str(roic)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding roic: "+str(roic)+" to database: {e}")
    # ros
        try:
            statement = "UPDATE financials SET ros='"+str(ros)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added ros: "+str(ros)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding ros: "+str(ros)+" to database: {e}")
    # sbcomp
        try:
            statement = "UPDATE financials SET sbcomp='"+str(sbcomp)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added sbcomp: "+str(sbcomp)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding sbcomp: "+str(sbcomp)+" to database: {e}")
    # sgna
        try:
            statement = "UPDATE financials SET sgna='"+str(sgna)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added sgna: "+str(sgna)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding sgna: "+str(sgna)+" to database: {e}")
    # sharefactor
        try:
            statement = "UPDATE financials SET sharefactor='"+str(sharefactor)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added sharefactor: "+str(sharefactor)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding sharefactor: "+str(sharefactor)+" to database: {e}")
    # sharesbas
        try:
            statement = "UPDATE financials SET sharesbas='"+str(sharesbas)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added sharesbas: "+str(sharesbas)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding sharesbas: "+str(sharesbas)+" to database: {e}")
    # shareswa
        try:
            statement = "UPDATE financials SET shareswa='"+str(shareswa)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added shareswa: "+str(shareswa)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding shareswa: "+str(shareswa)+" to database: {e}")
    # shareswadil
        try:
            statement = "UPDATE financials SET shareswadil='"+str(shareswadil)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added shareswadil: "+str(shareswadil)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding shareswadil: "+str(shareswadil)+" to database: {e}")
    # sps
        try:
            statement = "UPDATE financials SET sps='"+str(sps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added sps: "+str(sps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding sps: "+str(sps)+" to database: {e}")
    # tangibles
        try:
            statement = "UPDATE financials SET tangibles='"+str(tangibles)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added tangibles: "+str(tangibles)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding tangibles: "+str(tangibles)+" to database: {e}")
    # taxassets
        try:
            statement = "UPDATE financials SET taxassets='"+str(taxassets)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added taxassets: "+str(taxassets)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding taxassets: "+str(taxassets)+" to database: {e}")
    # taxexp
        try:
            statement = "UPDATE financials SET taxexp='"+str(taxexp)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added taxexp: "+str(taxexp)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding taxexp: "+str(taxexp)+" to database: {e}")
    # taxliabilities
        try:
            statement = "UPDATE financials SET taxliabilities='"+str(taxliabilities)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added taxliabilities: "+str(taxliabilities)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding taxliabilities: "+str(taxliabilities)+" to database: {e}")
    # tbvps
        try:
            statement = "UPDATE financials SET tbvps='"+str(tbvps)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added tbvps: "+str(tbvps)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding tbvps: "+str(tbvps)+" to database: {e}")
    # workingcapital
        try:
            statement = "UPDATE financials SET workingcapital='"+str(workingcapital)+"' where ticker='"+ticker+"'"
            cur.execute(statement)
            conn.commit()
            print("Successfully added workingcapital: "+str(workingcapital)+" to database.")
        except mariadb.Error as e:
            print(f"Error adding workingcapital: "+str(workingcapital)+" to database: {e}")
        print("\n\n\nSuccessfully added financials to the database.")
