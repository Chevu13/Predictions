import csv
import pandas as pd
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from nba_api.stats.endpoints.teamgamelog import TeamGameLog
from nba_api.stats.endpoints.boxscoretraditionalv2 import BoxScoreTraditionalV2
from nba_api.stats.endpoints.leaguegamelog import LeagueGameLog
from nba_api.stats.endpoints.boxscoreadvancedv2 import BoxScoreAdvancedV2
from nba_api.stats.endpoints.playergamelog import PlayerGameLog
from nba_api.stats.static import players
from matplotlib import pyplot as plt
import time 

def projekcija(igrac123,tim123)  :


    igrac=igrac123 # ovde zameniti LEBRONA sa promenljivom koja ce biti u pocetnoj funkciji
    team123=tim123
    
    
    def fetchPlayerData(pid):
        try:
            pgl = PlayerGameLog(player_id=pid).get_data_frames()[0]
            time.sleep(2)
            return pgl
        except:
            print("neuspelo1")
            return None
            
    def dodajboxadvance(game_id):
        try:
            pgl1 = BoxScoreAdvancedV2(game_id=game_id).get_data_frames()
            time.sleep(2)
            return pgl1
        except:
            print("neuspelo2")
            return None
        
    def dodajboxtradicional(game_id):
        try:
            pgl2 = BoxScoreTraditionalV2(game_id=game_id).get_data_frames()
            time.sleep(2)
            return pgl2
        except:
            print("neuspelo3")
            return None
            
            
    svi=players.get_players()
    igraci=[igracw for igracw in svi if igracw['is_active']]
    for igrac1 in igraci:
        if igrac1['full_name']==igrac:
            break
    zeljeni_igarc=igrac1  
    
    
    while True:
        new_data = fetchPlayerData(zeljeni_igarc['id'])
        if new_data is None:
            print('    ...sleeping at: %s'% time.ctime())
            time.sleep(10)
        else:
            njegove_utakmice=new_data
            break
    pp=0
    for red in range(len(njegove_utakmice)):
        pp+=njegove_utakmice['PTS'].values[red]
        pp/=len(njegove_utakmice)
    if pp<13:
        njegove_utakmice=njegove_utakmice[njegove_utakmice["MIN"]>=14]     
    else:
        njegove_utakmice=njegove_utakmice[njegove_utakmice["MIN"]>=20]
    skraceni=njegove_utakmice['MATCHUP']
    if 'vs.' in skraceni[0]:
        skr=skraceni[0].split(' vs. ')
    else:
        skr=skraceni[0].split(' @ ')
    if 'vs.' in skraceni[1]:
        skr1=skraceni[1].split(' vs. ')
    else:
        skr1=skraceni[1].split(' @ ')
    for skracenica in skr:
        if skracenica in skr1:
            break
            
    pts_avg=0
    fg_pct_avg=0
    ts_pct_avg=0
    off_rating_avg=0
    pace_avg=0
    usg_pct_avg=0
    
    team_off_rating_avg=0
    team_efg_pct_avg=0
    team_e_pace_avg=0
    team_poss_avg=0
    team_fg_avg=0
    team_pts_avg=0
    
    opponent_def_rating_avg=0
    opponent_pace_avg=0
    opponent_poss_avg=0
    
        
        
    ptslast5=[]
    fglast5=[]
    tslast5=[]
    offratinglast5=[]
    pacelast5=[]
    usglast5=[]
    toffrating5=[]
    tefglast5=[]
    tepacelast5=[]
    tposslast5=[]
    tfglast5=[]
    tpstlast5=[]
    
    pojmovi=['pts_avg','fg_pct_avg','ts_pct_avg','off_rating_avg','pace_avg','usg_pct_avg',\
             'team_off_rating_avg','team_efg_pct_avg','team_e_pace_avg','team_poss_avg','team_fg_avg','team_pts_avg',\
             'opponent_def_rating_avg','opponent_pace_avg','opponent_poss_avg',\
             'pts_last5','fg_pct_last5','ts_pct_last5','off_rating_last5','pace_last5','usg_pct_last5',\
             'team_off_rating_last5','team_efg_pct_last5','team_e_pace_last5','team_poss_last5','team_fg_last5','team_pts_last5',\
             'opponent_def_rating_last5','opponent_pace_last5','opponent_poss_last5','pts']
    
    
    sveutakmice=LeagueGameLog(counter=1,season='2019-20').get_data_frames()[0]
    njegove_utakmice=njegove_utakmice.sort_index(ascending=0)
    
    
    sveee=[]
    
    for i in range(len(njegove_utakmice)):
        kontis=[]
        
        pts_last5=0
        fg_pct_last5=0
        ts_pct_last5=0
        off_rating_last5=0
        pace_last5=0
        usg_pct_last5=0
        
        opponent_def_rating_last5=0
        opponent_pace_last5=0
        opponent_poss_last5=0
        
        team_off_rating_last5=0
        team_efg_pct_last5=0
        team_e_pace_last5=0
        team_poss_last5=0
        team_fg_last5=0
        team_pts_last5=0
    
        game_id=njegove_utakmice['Game_ID'].values[i]
    
        while True: 
            new_data1 = dodajboxtradicional(game_id)
            if new_data1 is None:
                print('    ...sleeping at: %s'% time.ctime())
                time.sleep(30)
            else:
                igractradicional=new_data1[0]
                igractradicional=igractradicional[igractradicional['PLAYER_ID']==zeljeni_igarc['id']]
                break
                    
        pts=igractradicional['PTS'].values[0]
        pts_avg+=pts
        fg_pct=igractradicional['FG_PCT'].values[0]
        fg_pct_avg+=fg_pct
        
        while True: 
            new_data3 = dodajboxadvance(game_id)
            if new_data3 is None:
                print('    ...sleeping at: %s'% time.ctime())
                time.sleep(30)
            else:
                igracadvance=new_data3[0]
                igracadvance=igracadvance[igracadvance['PLAYER_ID']==zeljeni_igarc['id']]
                tekma=new_data3[1]
                break
            
        ts_pct=igracadvance['TS_PCT'].values[0]
        ts_pct_avg+=ts_pct
        off_rating=igracadvance['OFF_RATING'].values[0]
        off_rating_avg+=off_rating
        pace=igracadvance['PACE'].values[0]
        pace_avg+=pace
        usg_pct=igracadvance['USG_PCT'].values[0]
        usg_pct_avg+=usg_pct
            
        while True: 
            new_data1 = dodajboxtradicional(game_id)
            if new_data1 is None:
                print('    ...sleeping at: %s'% time.ctime())
                time.sleep(20)
            else:
                tekma2=new_data1[1]
                tekma2=tekma2[tekma2['TEAM_ABBREVIATION']==skracenica]
                break
            
                
        team_fg=tekma2['FG_PCT'].values[0]
        team_fg_avg+=team_fg
        team_pts=tekma2['PTS'].values[0]
        team_pts_avg+=team_pts
        
        while True:
            print(game_id)
            new_data2 = dodajboxadvance(game_id)
            if new_data2 is None:
                print('    ...sleeping at: %s'% time.ctime())
                time.sleep(10)
            else:
                tekma=new_data2[1]
                tekma1=tekma[tekma['TEAM_ABBREVIATION']==skracenica]
                break
            
        team_off_rating=tekma1['OFF_RATING'].values[0]
        team_off_rating_avg+=team_off_rating
        team_efg_pct=tekma1['EFG_PCT'].values[0]
        team_efg_pct_avg+=team_efg_pct
        team_e_pace=tekma1['E_PACE'].values[0]
        team_e_pace_avg+=team_e_pace
        team_poss=tekma1['POSS'].values[0]
        team_poss_avg+=team_poss
            
        if i in range(5,10):
            ptslast5.append(pts)
            fglast5.append(fg_pct)
            tslast5.append(ts_pct)
            offratinglast5.append(off_rating)
            pacelast5.append(pace)
            usglast5.append(usg_pct)
                
            toffrating5.append(team_off_rating)
            tefglast5.append(team_efg_pct)
            tepacelast5.append(team_e_pace)
            tposslast5.append(team_poss)
            tfglast5.append(team_fg)
            tpstlast5.append(team_pts)  
        
        if (len(njegove_utakmice)-1)>i> 8:   
            gamee_id=njegove_utakmice['Game_ID'].values[i+1]
            while True:
                print(gamee_id)
                new_data33 =dodajboxadvance(gamee_id)
                if new_data33 is None:
                    print('    ...sleeping at: %s'% time.ctime())
                    time.sleep(10)
                else:
                    tekma=new_data33[1]
                    break
            
            opponent=tekma[tekma['TEAM_ABBREVIATION']!=skracenica]
            oponent=opponent['TEAM_ABBREVIATION'].values[0]
            oponent_game_id=opponent['GAME_ID'].values[0]
            opponent_id=sveutakmice[sveutakmice['TEAM_ABBREVIATION']==oponent]['TEAM_ID'].values[0]
            protivnik=TeamGameLog(team_id=opponent_id).get_data_frames()[0]
            lista_do_te_tekme=protivnik[protivnik["Game_ID"]<oponent_game_id]
            for j in range(len(lista_do_te_tekme)):
    
                while True:
                    game_idd=lista_do_te_tekme['Game_ID'].values[j]
                    new_data82 = dodajboxadvance(game_idd)
                    if new_data82 is None:
                        print('    ...sleeping at: %s'% time.ctime())
                        time.sleep(40)
                    else:
                        tekma=new_data82[1]
                        game1=tekma[tekma['TEAM_ABBREVIATION']==oponent]
                        break
                opponent_def_rating=game1['DEF_RATING'].values[0]
                opponent_def_rating_avg+=opponent_def_rating
                opponent_pace=game1['PACE'].values[0]
                opponent_pace_avg+=opponent_pace
                opponent_poss=game1['POSS'].values[0]
                opponent_poss_avg+=opponent_poss
                if j<4:
                    opponent_def_rating_last5+=opponent_def_rating
                    opponent_pace_last5+=opponent_pace
                    opponent_poss_last5+=opponent_poss
                if j==(len(lista_do_te_tekme)-1):
                    opponent_def_rating_avg/=j
                    opponent_pace_avg/=j
                    opponent_poss_avg/=j
                    
    
        if i>9:
            ptslast5=ptslast5[1:5]
            ptslast5.append(pts)
            fglast5=fglast5[1:5]
            fglast5.append(fg_pct)
            tslast5=tslast5[1:5]
            tslast5.append(ts_pct)
            offratinglast5=offratinglast5[1:5]
            offratinglast5.append(off_rating)
            pacelast5=pacelast5[1:5]
            pacelast5.append(pace)
            usglast5=usglast5[1:5]
            usglast5.append(usg_pct)
            toffrating5=toffrating5[1:5]
            toffrating5.append(team_off_rating)
            tefglast5=tefglast5[1:5]
            tefglast5.append(team_efg_pct)
            tepacelast5=tepacelast5[1:5]
            tepacelast5.append(team_e_pace)
            tposslast5=tposslast5[1:5]
            tposslast5.append(team_poss)
            tfglast5=tfglast5[1:5]
            tfglast5.append(team_fg)
            tpstlast5=tpstlast5[1:5]
            tpstlast5.append(team_pts)
        if i >= 9 :
        
            k=pts_avg/i                # OVO PROMENITIIIIIIIIIIIi
            kontis.append(k)
            k=fg_pct_avg/i
            kontis.append(k)
            k=ts_pct_avg/i
            kontis.append(k)
            k=off_rating_avg/i
            kontis.append(k)
            k=pace_avg/i
            kontis.append(k)
            k=usg_pct_avg/i
            kontis.append(k)
            
            k=team_off_rating_avg/i
            kontis.append(k)
            k=team_efg_pct_avg/i
            kontis.append(k)
            k=team_e_pace_avg/i
            kontis.append(k)
            k=team_poss_avg/i
            kontis.append(k)
            k=team_fg_avg/i
            kontis.append(k)
            k=team_pts_avg/i
            kontis.append(k)
                
            kontis.append(opponent_def_rating_avg)
            kontis.append(opponent_pace_avg)
            kontis.append(opponent_poss_avg)
    
            for a in ptslast5:
                pts_last5+=a
            for a in fglast5 :
                fg_pct_last5+=a
            for a in tslast5:
                ts_pct_last5+=a
            for a in offratinglast5:
                off_rating_last5+=a
            for a in pacelast5:
                pace_last5+=a
            for a in usglast5:
                usg_pct_last5+=a
                
            for a in toffrating5:
                team_off_rating_last5+=a
            for a in tefglast5:
                team_efg_pct_last5+=a
            for a in tepacelast5:
                team_e_pace_last5+=a
            for a in tposslast5:
                team_poss_last5+=a
            for a in tfglast5:
                team_fg_last5+=a
            for a in tpstlast5:
                team_pts_last5+=a
        
            pts_last5=pts_last5/5
            kontis.append(pts_last5)
            fg_pct_last5/=5
            kontis.append(fg_pct_last5)
            ts_pct_last5/=5
            kontis.append(ts_pct_last5)
            off_rating_last5/=5
            kontis.append(off_rating_last5)
            pace_last5/=5
            kontis.append(pace_last5)
            usg_pct_last5/=5
            kontis.append(usg_pct_last5)
            
            team_off_rating_last5/=5
            kontis.append(team_off_rating_last5)
            team_efg_pct_last5/=5
            kontis.append(team_efg_pct_last5)
            team_e_pace_last5/=5
            kontis.append(team_e_pace_last5)
            team_poss_last5/=5
            kontis.append(team_poss_last5)
            team_fg_last5/=5
            kontis.append(team_fg_last5)
            team_pts_last5/=5
            kontis.append(team_pts_last5)
            
            opponent_def_rating_last5/=5
            kontis.append(opponent_def_rating_last5)
            opponent_pace_last5/=5
            kontis.append(opponent_pace_last5)
            opponent_poss_last5/=5
            kontis.append(opponent_poss_last5)
            
        if i==(len(njegove_utakmice)-1):
                    
            protiv=sveutakmice[sveutakmice['TEAM_ABBREVIATION']==team123]
            protiv=protiv['Game_ID']
            for j in protiv:
                while True:
                    new_data123 = dodajboxadvance(j)
                    if new_data123 is None:
                        print('    ...sleeping at: %s'% time.ctime())
                        time.sleep(40)
                    else:
                        tekma=new_data82[1]
                        game1=tekma[tekma['TEAM_ABBREVIATION']==oponent]
                        break
            opponent_def_rating=game1['DEF_RATING'].values[0]
            opponent_def_rating_avg+=opponent_def_rating
            opponent_pace=game1['PACE'].values[0]
            opponent_pace_avg+=opponent_pace
            opponent_poss=game1['POSS'].values[0]
            opponent_poss_avg+=opponent_poss
            if j<4:
                opponent_def_rating_last5+=opponent_def_rating
                opponent_pace_last5+=opponent_pace
                opponent_poss_last5+=opponent_poss
            if j==(len(protiv)-1):
                opponent_def_rating_avg/=j
                opponent_pace_avg/=j
                opponent_poss_avg/=j
                
                
                opponent_def_rating_last5/=5
                kontis.append(opponent_def_rating_last5)
                opponent_pace_last5/=5
                kontis.append(opponent_pace_last5)
                opponent_poss_last5/=5
                kontis.append(opponent_poss_last5)
                
                kontis.append('?????????')
                
            dictionary = dict(zip(pojmovi, kontis))
            sveee.append(dictionary)
            print(i)
            
            
    print(len(kontis))
    print(len(pojmovi))
    dsds=sveee[0:len(sveee)-1]
        #print(sveee[-1])
        #print(dsds)
        
    with open('mycsv.csv','w',newline='') as f :
        fieldnames=pojmovi=['pts_avg','fg_pct_avg','ts_pct_avg','off_rating_avg','pace_avg','usg_pct_avg',\
             'team_off_rating_avg','team_efg_pct_avg','team_e_pace_avg','team_poss_avg','team_fg_avg','team_pts_avg',\
             'opponent_def_rating_avg','opponent_pace_avg','opponent_poss_avg',\
             'pts_last5','fg_pct_last5','ts_pct_last5','off_rating_last5','pace_last5','usg_pct_last5',\
             'team_off_rating_last5','team_efg_pct_last5','team_e_pace_last5','team_poss_last5','team_fg_last5','team_pts_last5',\
             'opponent_def_rating_last5','opponent_pace_last5','opponent_poss_last5','pts']
        thewriter=csv.DictWriter(f,fieldnames=fieldnames)    
        thewriter.writeheader()
        for i in range(1,len(dsds)):
            thewriter.writerow(dsds[i])       
        
    with open('mycsv1.csv','w',newline='') as f :
        fieldnames=pojmovi=['pts_avg','fg_pct_avg','ts_pct_avg','off_rating_avg','pace_avg','usg_pct_avg',\
             'team_off_rating_avg','team_efg_pct_avg','team_e_pace_avg','team_poss_avg','team_fg_avg','team_pts_avg',\
             'opponent_def_rating_avg','opponent_pace_avg','opponent_poss_avg',\
             'pts_last5','fg_pct_last5','ts_pct_last5','off_rating_last5','pace_last5','usg_pct_last5',\
             'team_off_rating_last5','team_efg_pct_last5','team_e_pace_last5','team_poss_last5','team_fg_last5','team_pts_last5',\
             'opponent_def_rating_last5','opponent_pace_last5','opponent_poss_last5','pts']
        thewriter=csv.DictWriter(f,fieldnames=fieldnames)    
        thewriter.writeheader()
        thewriter.writerow(sveee[-1]) 
        
    df=pd.read_csv('mycsv.csv')
    poeeni=df.pts
    df.drop('pts',axis=1,inplace=True)
        
    dff=pd.read_csv('mycsv1.csv')
    dff.drop('pts',axis=1,inplace=True)
        
        
    df_train,df_test,poeeni_train,poeeni_test=train_test_split(df,poeeni,test_size=0.15,random_state=0)
    '''
        model=LogisticRegression(random_state=0,max_iter=100000000)
        model.fit(df, poeeni)
        model.fit(df_train,poeeni_train)
        model.score(df_test,poeeni_test)
        model.predict(df_test)
        print(poeeni_test)
        model.predict(dff)
        
    '''
    df.drop('pts_avg',axis=1,inplace=True)
    df.drop('fg_pct_avg',axis=1,inplace=True)
    df.drop('pace_avg',axis=1,inplace=True)
    df.drop('ts_pct_avg',axis=1,inplace=True)
    df.drop('off_rating_avg',axis=1,inplace=True)
    df.drop('usg_pct_avg',axis=1,inplace=True)
    df.drop('opponent_def_rating_avg',axis=1,inplace=True)
    df.drop('team_off_rating_avg',axis=1,inplace=True)
    df.drop('team_e_pace_avg',axis=1,inplace=True)
    df.drop('team_poss_avg',axis=1,inplace=True)
    df.drop('team_fg_avg',axis=1,inplace=True)
    df.drop('team_pts_avg',axis=1,inplace=True)
    df.drop('opponent_pace_avg',axis=1,inplace=True)
    df.drop('opponent_poss_avg',axis=1,inplace=True)
    
        
    dff.drop('pts_avg',axis=1,inplace=True)
    dff.drop('fg_pct_avg',axis=1,inplace=True)
    dff.drop('pace_avg',axis=1,inplace=True)
    dff.drop('ts_pct_avg',axis=1,inplace=True)
    dff.drop('off_rating_avg',axis=1,inplace=True)
    dff.drop('usg_pct_avg',axis=1,inplace=True)
    dff.drop('opponent_def_rating_avg',axis=1,inplace=True)
    dff.drop('team_off_rating_avg',axis=1,inplace=True)
    dff.drop('team_e_pace_avg',axis=1,inplace=True)
    dff.drop('team_poss_avg',axis=1,inplace=True)
    dff.drop('team_fg_avg',axis=1,inplace=True)
    dff.drop('team_pts_avg',axis=1,inplace=True)
    dff.drop('opponent_pace_avg',axis=1,inplace=True)
    dff.drop('opponent_poss_avg',axis=1,inplace=True)
    
        
    clf=svm.SVC(gamma=0.001, C=100)
        
        
    clf.fit(df,poeeni)
    l=clf.predict(dff)
    clf.fit(df_train,poeeni_train)
    clf.score(df_test,poeeni_test)
        
    print(sveee[len(dsds)]['pts_avg'])
    if l[0]<sveee[len(dsds)]['pts_avg']:
        print('Postici ce manji broj poena nego u proseku')
    else:
        print('Postici ce veci broj poena nego u proseku')    
            
