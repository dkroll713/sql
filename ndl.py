import nasdaqdatalink
import pandas as pd
import mariadb
import time

nasdaqdatalink.read_key("C:/bin/api-keys/nasdaq-data-link")

# ticker = input("Which stock would you like Sharadar data for?\n>> ")

# data = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)

# df = data.iloc[1]
# name = df.loc['name']

def print_fin(ticker):

    null = 'NULL'

    nasdaq_info = nasdaqdatalink.get_table('SHARADAR/TICKERS',ticker=ticker)
    if not nasdaq_info.empty:
        company = nasdaq_info.iloc[1]
        name = company.loc['name']
        sicsector = company.loc['sicsector']
        sicindustry = company.loc['sicindustry']
        famaindustry = company.loc['famaindustry']
        sector = company.loc['sector']
        industry = company.loc['industry']
        scalemarketcap = company.loc['scalemarketcap']
        scalerevenue = company.loc['scalerevenue']
    else:
        company = null
        name = null
        sicsector = null
        sicindustry = null
        famaindustry = null
        sector = null
        industry = null
        scalemarketcap = null
        scalerevenue = null

    financials = nasdaqdatalink.get_table('SHARADAR/SF1',dimension='MRY',ticker=ticker)
    nasdaq_financials = financials.iloc[1]
# financial data variables
    ticker = ticker
    date = str(nasdaq_financials.loc['calendardate'])
    datekey = nasdaq_financials.loc['datekey']
    reportperiod = nasdaq_financials.loc['reportperiod']
    lastupdated = nasdaq_financials.loc['lastupdated']
    if nasdaq_financials.loc['accoci'] != None:
        accoci = float(nasdaq_financials.loc['accoci'])
    else:
        accoci = null
    if nasdaq_financials.loc['assets'] != None:
        assets = float(nasdaq_financials.loc['assets'])
    else:
        assets = null
    if nasdaq_financials.loc['assetsavg'] != None:
        assetsavg = float(nasdaq_financials.loc['assetsavg'])
    else:
        assetsavg = null
    if nasdaq_financials.loc['assetsc'] != None:
        assetsc = float(nasdaq_financials.loc['assetsc'])
    else:
        assetsc = 'Null'
    if nasdaq_financials.loc['assetsnc'] != None:
        assetsnc = float(nasdaq_financials.loc['assetsnc'])
    else:
        assetsnc = 'Null'
    if nasdaq_financials.loc['assetturnover'] != None:
        assetturnover = float(nasdaq_financials.loc['assetturnover'])
    else:
        assetturnover = null
    if nasdaq_financials.loc['bvps'] != None:
        bvps = float(nasdaq_financials.loc['bvps'])
    else:
        bvps = null
    if nasdaq_financials.loc['capex'] != None:
        capex = float(nasdaq_financials.loc['capex'])
    else:
        capex = null
    if nasdaq_financials.loc['cashneq'] != None:
        cashneq = float(nasdaq_financials.loc['cashneq'])
    else:
        cashneq = null
    if nasdaq_financials.loc['cashnequsd'] != None:
        cashnequsd = float(nasdaq_financials.loc['cashnequsd'])
    else:
        cashnequsd = null
    if nasdaq_financials.loc['cor'] != None:
        cor = float(nasdaq_financials.loc['cor'])
    else:
        cor = null
    if nasdaq_financials.loc['consolinc'] != None:
        consolinc = float(nasdaq_financials.loc['consolinc'])
    else:
        consolinc = null
    if nasdaq_financials.loc['currentratio'] != None:
        currentratio = float(nasdaq_financials.loc['currentratio'])
    else:
        currentratio = null
    if nasdaq_financials.loc['de'] != None:
        de = float(nasdaq_financials.loc['de'])
    else:
        de = null
    if nasdaq_financials.loc['debt'] != None:
        debt = float(nasdaq_financials.loc['debt'])
    else:
        debt = null
    if nasdaq_financials.loc['debtc'] != None:
        debtc = float(nasdaq_financials.loc['debtc'])
    else:
        debtc = null
    if nasdaq_financials.loc['debtnc'] != None:
        debtnc = float(nasdaq_financials.loc['debtnc'])
    else:
        debtnc = null
    if nasdaq_financials.loc['debtusd'] != None:
        debtusd = float(nasdaq_financials.loc['debtusd'])
    else:
        debtusd = null
    if nasdaq_financials.loc['deferredrev'] != None:
        deferredrev = float(nasdaq_financials.loc['deferredrev'])
    else:
        deferredrev = null
    if nasdaq_financials.loc['depamor'] != None:
        depamor = float(nasdaq_financials.loc['depamor'])
    else:
        depamor = null
    if nasdaq_financials.loc['deposits'] != None:
        deposits = float(nasdaq_financials.loc['deposits'])
    else:
        deposits = null
    if nasdaq_financials.loc['divyield'] != None:
        divyield = float(nasdaq_financials.loc['divyield'])
    else:
        divyield = null
    if nasdaq_financials.loc['dps'] != None:
        dps = float(nasdaq_financials.loc['dps'])
    else:
        dps = null
    if nasdaq_financials.loc['ebit'] != None:
        ebit = float(nasdaq_financials.loc['ebit'])
    else:
        ebit = null
    if nasdaq_financials.loc['ebitda'] != None:
        ebitda = float(nasdaq_financials.loc['ebitda'])
    else:
        ebitda = null
    if nasdaq_financials.loc['ebitdamargin'] != None:
        ebitdamargin = float(nasdaq_financials.loc['ebitdamargin'])
    else:
        ebitdamargin = null
    if nasdaq_financials.loc['ebitdausd'] != None:
        ebitdausd = float(nasdaq_financials.loc['ebitdausd'])
    else:
        ebitdausd = null
    if nasdaq_financials.loc['ebitusd'] != None:
        ebitusd = float(nasdaq_financials.loc['ebitusd'])
    else:
        ebitusd = null
    if nasdaq_financials.loc['ebt'] != None:
        ebt = float(nasdaq_financials.loc['ebt'])
    else:
        ebt = null
    if nasdaq_financials.loc['eps'] != None:
        eps = float(nasdaq_financials.loc['eps'])
    else:
        eps = null
    if nasdaq_financials.loc['epsdil'] != None:
        epsdil = float(nasdaq_financials.loc['epsdil'])
    else:
        epsdil = null
    if nasdaq_financials.loc['epsusd'] != None:
        epsusd = float(nasdaq_financials.loc['epsusd'])
    else:
        epsusd = null
    if nasdaq_financials.loc['equity'] != None:
        equity = float(nasdaq_financials.loc['equity'])
    else:
        equity = null
    if nasdaq_financials.loc['equityavg'] != None:
        equityavg = float(nasdaq_financials.loc['equityavg'])
    else:
        equityavg = null
    if nasdaq_financials.loc['equityusd'] != None:
        equityusd = float(nasdaq_financials.loc['equityusd'])
    else:
        equityusd = null
    if nasdaq_financials.loc['ev'] != None:
        ev = float(nasdaq_financials.loc['ev'])
    else:
        ev = null
    if nasdaq_financials.loc['evebit'] != None:
        evebit = float(nasdaq_financials.loc['evebit'])
    else:
        evebit = null
    if nasdaq_financials.loc['fcf'] != None:
        fcf = float(nasdaq_financials.loc['fcf'])
    else:
        fcf = null
    if nasdaq_financials.loc['fcfps'] != None:
        fcfps = float(nasdaq_financials.loc['fcfps'])
    else:
        fcfps = null
    if nasdaq_financials.loc['fxusd'] != None:
        fxusd = float(nasdaq_financials.loc['fxusd'])
    else:
        fxusd = null
    if nasdaq_financials.loc['gp'] != None:
        gp = float(nasdaq_financials.loc['gp'])
    else:
        gp = null
    if nasdaq_financials.loc['grossmargin'] != None:
        grossmargin = float(nasdaq_financials.loc['grossmargin'])
    else:
        grossmargin = null
    if nasdaq_financials.loc['intangibles'] != None:
        intangibles = float(nasdaq_financials.loc['intangibles'])
    else:
        intangibles = null
    if nasdaq_financials.loc['intexp'] != None:
        intexp = float(nasdaq_financials.loc['intexp'])
    else:
        intexp = null
    if nasdaq_financials.loc['invcap'] != None:
        invcap = float(nasdaq_financials.loc['invcap'])
    else:
        invcap = null
    if nasdaq_financials.loc['inventory'] != None:
        inventory = float(nasdaq_financials.loc['inventory'])
    else:
        inventory = null
    if nasdaq_financials.loc['investments'] != None:
        investments = float(nasdaq_financials.loc['investments'])
    else:
        investments = null
    if nasdaq_financials.loc['investmentsc'] != None:
        investmentsc = float(nasdaq_financials.loc['investmentsc'])
    else:
        investmentsc = null
    if nasdaq_financials.loc['investmentsnc'] != None:
        investmentsnc = float(nasdaq_financials.loc['investmentsnc'])
    else:
        investmentsnc = null
    if nasdaq_financials.loc['liabilities'] != None:
        liabilities = float(nasdaq_financials.loc['liabilities'])
    else:
        liabilities = null
    if nasdaq_financials.loc['liabilitiesc'] != None:
        liabilitiesc = float(nasdaq_financials.loc['liabilitiesc'])
    else:
        liabilitiesc = null
    if nasdaq_financials.loc['liabilitiesnc'] != None:
        liabilitiesnc = float(nasdaq_financials.loc['liabilitiesnc'])
    else:
        liabilitiesnc = null
    if nasdaq_financials.loc['marketcap'] != None:
        marketcap = float(nasdaq_financials.loc['marketcap'])
    else:
        marketcap = null
    if nasdaq_financials.loc['ncf'] != None:
        ncf = float(nasdaq_financials.loc['ncf'])
    else:
        ncf = null
    if nasdaq_financials.loc['ncfbus'] != None:
        ncfbus = float(nasdaq_financials.loc['ncfbus'])
    else:
        ncfbus = null
    if nasdaq_financials.loc['ncfcommon'] != None:
        ncfcommon = float(nasdaq_financials.loc['ncfcommon'])
    else:
        ncfcommon = null
    if nasdaq_financials.loc['ncfdebt'] != None:
        ncfdebt = float(nasdaq_financials.loc['ncfdebt'])
    else:
        ncfdebt = null
    if nasdaq_financials.loc['ncfdiv'] != None:
        ncfdiv = float(nasdaq_financials.loc['ncfdiv'])
    else:
        ncfdiv = null
    if nasdaq_financials.loc['ncff'] != None:
        ncff = float(nasdaq_financials.loc['ncff'])
    else:
        ncff = null
    if nasdaq_financials.loc['ncfi'] != None:
        ncfi = float(nasdaq_financials.loc['ncfi'])
    else:
        ncfi = null
    if nasdaq_financials.loc['ncfinv'] != None:
        ncfinv = float(nasdaq_financials.loc['ncfinv'])
    else:
        ncfinv = null
    if nasdaq_financials.loc['ncfo'] != None:
        ncfo = float(nasdaq_financials.loc['ncfo'])
    else:
        ncfo = null
    if nasdaq_financials.loc['ncfx'] != None:
        ncfx = float(nasdaq_financials.loc['ncfx'])
    else:
        ncfx = null
    if nasdaq_financials.loc['netinc'] != None:
        netinc = float(nasdaq_financials.loc['netinc'])
    else:
        netinc = null
    if nasdaq_financials.loc['netinccmn'] != None:
        netinccmn = float(nasdaq_financials.loc['netinccmn'])
    else:
        netinccmn = null
    if nasdaq_financials.loc['netinccmnusd'] != None:
        netinccmnusd = float(nasdaq_financials.loc['netinccmnusd'])
    else:
        netinccmnusd = null
    if nasdaq_financials.loc['netincdis'] != None:
        netincdis = float(nasdaq_financials.loc['netincdis'])
    else:
        netincdis = null
    if nasdaq_financials.loc['netincnci'] != None:
        netincnci = float(nasdaq_financials.loc['netincnci'])
    else:
        netincnci = null
    if nasdaq_financials.loc['netmargin'] != None:
        netmargin = float(nasdaq_financials.loc['netmargin'])
    else:
        netmargin = null
    if nasdaq_financials.loc['opex'] != None:
        opex = float(nasdaq_financials.loc['opex'])
    else:
        opex = null
    if nasdaq_financials.loc['opinc'] != None:
        opinc = float(nasdaq_financials.loc['opinc'])
    else:
        opinc = null
    if nasdaq_financials.loc['payables'] != None:
        payables = float(nasdaq_financials.loc['payables'])
    else:
        payables = null
    if nasdaq_financials.loc['payoutratio'] != None:
        payoutratio = float(nasdaq_financials.loc['payoutratio'])
    else:
        payoutratio = null
    if nasdaq_financials.loc['pb'] != None:
        pb = float(nasdaq_financials.loc['pb'])
    else:
        pb = null
    if nasdaq_financials.loc['pe'] != None:
        pe = float(nasdaq_financials.loc['pe'])
    else:
        pe = null
    if nasdaq_financials.loc['pe1'] != None:
        pe1 = float(nasdaq_financials.loc['pe1'])
    else:
        pe1 = null
    if nasdaq_financials.loc['ppnenet'] != None:
        ppnenet = float(nasdaq_financials.loc['ppnenet'])
    else:
        ppnenet = null
    if nasdaq_financials.loc['prefdivis'] != None:
        prefdivis = float(nasdaq_financials.loc['prefdivis'])
    else:
        prefdivis = null
    if nasdaq_financials.loc['price'] != None:
        price = float(nasdaq_financials.loc['price'])
    else:
        price = null
    if nasdaq_financials.loc['ps'] != None:
        ps = float(nasdaq_financials.loc['ps'])
    else:
        ps = null
    if nasdaq_financials.loc['ps1'] != None:
        ps1 = float(nasdaq_financials.loc['ps1'])
    else:
        ps1 = null
    if nasdaq_financials.loc['receivables'] != None:
        receivables = float(nasdaq_financials.loc['receivables'])
    else:
        receivables = null
    if nasdaq_financials.loc['retearn'] != None:
        retearn = float(nasdaq_financials.loc['retearn'])
    else:
        retearn = null
    if nasdaq_financials.loc['revenue'] != None:
        revenue = float(nasdaq_financials.loc['revenue'])
    else:
        revenue = null
    if nasdaq_financials.loc['revenueusd'] != None:
        revenueusd = float(nasdaq_financials.loc['revenueusd'])
    else:
        revenueusd = null
    if nasdaq_financials.loc['rnd'] != None:
        rnd = float(nasdaq_financials.loc['rnd'])
    else:
        rnd = null
    if nasdaq_financials.loc['roa'] != None:
        roa = float(nasdaq_financials.loc['roa'])
    else:
        roa = null
    if nasdaq_financials.loc['roe'] != None:
        roe = float(nasdaq_financials.loc['roe'])
    else:
        roe = null
    if nasdaq_financials.loc['roic'] != None:
        roic = float(nasdaq_financials.loc['roic'])
    else:
        roic = null
    if nasdaq_financials.loc['ros'] != None:
        ros = float(nasdaq_financials.loc['ros'])
    else:
        ros = null
    if nasdaq_financials.loc['sbcomp'] != None:
        sbcomp = float(nasdaq_financials.loc['sbcomp'])
    else:
        sbcomp = null
    if nasdaq_financials.loc['sgna'] != None:
        sgna = float(nasdaq_financials.loc['sgna'])
    else:
        sgna = null
    if nasdaq_financials.loc['sharefactor'] != None:
        sharefactor = float(nasdaq_financials.loc['sharefactor'])
    else:
        sharefactor = null
    if nasdaq_financials.loc['sharesbas'] != None:
        sharesbas = float(nasdaq_financials.loc['sharesbas'])
    else:
        sharesbas = null
    if nasdaq_financials.loc['shareswa'] != None:
        shareswa = float(nasdaq_financials.loc['shareswa'])
    else:
        shareswa = null
    if nasdaq_financials.loc['shareswadil'] != None:
        shareswadil = float(nasdaq_financials.loc['shareswadil'])
    else:
        shareswadil = null
    if nasdaq_financials.loc['sps'] != None:
        sps = float(nasdaq_financials.loc['sps'])
    else:
        sps = null
    if nasdaq_financials.loc['tangibles'] != None:
        tangibles = float(nasdaq_financials.loc['tangibles'])
    else:
        tangibles = null
    if nasdaq_financials.loc['taxassets'] != None:
        taxassets = float(nasdaq_financials.loc['taxassets'])
    else:
        taxassets = null
    if nasdaq_financials.loc['taxexp'] != None:
        taxexp = float(nasdaq_financials.loc['taxexp'])
    else:
        taxexp = null
    if nasdaq_financials.loc['taxliabilities'] != None:
        taxliabilities = float(nasdaq_financials.loc['taxliabilities'])
    else:
        taxliabilities = null
    if nasdaq_financials.loc['tbvps'] != None:
        tbvps = float(nasdaq_financials.loc['tbvps'])
    else:
        tbvps = null
    if nasdaq_financials.loc['workingcapital'] != None:
        workingcapital = float(nasdaq_financials.loc['workingcapital'])
    else:
        workingcapital = null

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
      print(ticker+" already included in database.")
    else:
        try:
            statement = "INSERT INTO financials (ticker, date) VALUES (%s, %s)"
            data = (ticker, date)
            cur.execute(statement,data)
            conn.commit()
            print("\n\nSuccessfully initiated "+ticker+" financials entry.")
            time.sleep(.1)
        except mariadb.Error as e:
            print(f"Error adding financials to database: {e}")
    # accoci
        if accoci:
            try:
                statement = "UPDATE financials SET accoci='"+str(accoci)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added accoci: "+str(accoci)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding accoci: "+str(accoci)+" to database: {e}")
    # assets
        if assets:
            try:
                statement = "UPDATE financials SET assets='"+str(assets)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added assets: "+str(assets)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding assets: "+str(assets)+" to database: {e}")
    # assetsavg
        if assetsavg:
            try:
                statement = "UPDATE financials SET assetsavg='"+str(assetsavg)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added assetsavg: "+str(assetsavg)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding assetsavg: "+str(assetsavg)+" to database: {e}")
    # assetsc
        if assetsc:
            try:
                statement = "UPDATE financials SET assetsc='"+str(assetsc)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added assetsc: "+str(assetsc)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding assetsc: "+str(assetsc)+" to database: {e}")
    # assetsnc
        if assetsnc:
            try:
                statement = "UPDATE financials SET assetsnc='"+str(assetsnc)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added assetsnc: "+str(assetsnc)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding assetsnc: "+str(assetsnc)+" to database: {e}")
    # assetturnover
        if assetturnover:
            try:
                statement = "UPDATE financials SET assetturnover='"+str(assetturnover)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added assetturnover: "+str(assetturnover)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding assetturnover: "+str(assetturnover)+" to database: {e}")
    # bvps
        if bvps:
            try:
                statement = "UPDATE financials SET bvps='"+str(bvps)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added bvps: "+str(bvps)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding bvps: "+str(bvps)+" to database: {e}")
    # capex
        if capex:
            try:
                statement = "UPDATE financials SET capex='"+str(capex)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added capex: "+str(capex)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding capex: "+str(capex)+" to database: {e}")
    # cashneq
        if cashneq:
            try:
                statement = "UPDATE financials SET cashneq='"+str(cashneq)+"' where ticker='"+ticker+"'"
                cur.execute(statement)
                conn.commit()
                print("Successfully added cashneq: "+str(cashneq)+" to database.")
            except mariadb.Error as e:
                print(f"Error adding cashneq: "+str(cashneq)+" to database: {e}")
    # cashnequsd
        if cashnequsd:
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
        print("\n\n\nSuccessfully completed "+ticker+" financials entry.")
        time.sleep(.3)
    conn.close()
