from audioop import add
import sqlite3
from tkinter.tix import COLUMN
database = 'techshop.db'
con = sqlite3.connect('techshop.db')
cur = con.cursor()

# cur.execute('''create table phones (company text , fullname text , memory text , color text , date text , size text , weight text , simcard text ,  screensize text , screenresolution text , operatingsystem text , chipset text , gpu text , ram text ,  additionalmemory text , maincamera text ,  video text , selfiecamera text , selfievideo text , bluthooth text , gps text , nfc text , fmradio text ,  port text ,sizemah text)''')
# cur.execute('''INSERT INTO phones (company , fullname              , memory            , color                                            , date             , size                , weight  , simcard      ,  screensize  , screenresolution , operatingsystem , chipset                   , gpu                           , ram    ,  additionalmemory , maincamera   ,  video                                                                                                                          , selfiecamera , selfievideo                                       , bluthooth       , gps                                            , nfc , fmradio   ,  port , sizemah ) 
#                           VALUES  ("Apple" , "Apple iPhone 13 pro" , "128/256/512/1TB" , "Graphite/Silver/Gold/Sierra Blue/Alphine Green" , "2021 September" , "146.7x71.5x7.7 mm" , "204 g" , "Single SIM" , "6.1 inches" , "1170 x 2532"    , "iOS 15"        , "Apple A15 Bionic (5 nm)" , "Apple GPU (5-core graphics)" , "6 GB" , "NO"              , "12+12+12MP" ,  "4K@24/30/60fps, 1080p@30/60/120/240fps, 10 bit HDR, Dolby Vision HDR (up to 60fps), ProRes, Cinematic mode, stereo sound rec" , "12 MP"      , "4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS" , "5.0, A2DP, LE" , "Yes, with A-GPS, GLONASS, GALILEO, BDS, QZSS" , "YES" , "NO"    , "NO"  , "Li-Ion 3095 mAh") ''')

# cur.execute('''INSERT INTO phones (company , fullname           , memory   , color                                     , date           , size                    , weight  , simcard      ,  screensize  , screenresolution , operatingsystem , chipset             , gpu                           , ram    ,  additionalmemory , maincamera   ,  video                                                                                            , selfiecamera , selfievideo                                       , bluthooth       , gps                                            , nfc   , fmradio ,  port , sizemah ) 
#                           VALUES  ("Apple" , "Apple iPhone 11"  , "64/128" , "Black/White/Purple/Yellow/Green/Red"     , "2020 October" , "146.7 x 71.5 x 7.4 mm" , "194 g" , "Single SIM" , "6.1 inches" , "828 x 1792 "    , "iOS 13"        , "Apple A13 Bionic"  , "Apple GPU (4-core graphics)" , "4 GB" , "NO"              , "12+12MP"    ,  "4K@24/30/60fps, 1080p@30/60/120/240fps, HDR, Dolby Vision HDR (up to 30fps), stereo sound rec"  , "12 MP"      , "4K@24/25/30/60fps, 1080p@30/60/120fps, gyro-EIS" , "5.0, A2DP, LE" , "Yes, with A-GPS, GLONASS, GALILEO, BDS, QZSS" , "YES" , "NO"    , "NO"  , "Li-Ion 3110 mAh") ''')

# cur.execute('''INSERT INTO phones (company , fullname           , memory    , color                 , date           , size                    , weight  , simcard      ,  screensize  , screenresolution , operatingsystem , chipset             , gpu                           , ram    ,  additionalmemory , maincamera   ,  video                                        , selfiecamera , selfievideo   , bluthooth       , gps                                            , nfc   , fmradio ,  port , sizemah ) 
#                           VALUES  ("Apple" , "Apple iPhone SE"  , "128/256" , "Black/Red/White"     , "2020 October" , "138.4 x 67.3 x 7.3 mm" , "148 g" , "Single SIM" , "4.7 inches" , "750 x 1334"    , "iOS 13"         , "Apple A13 Bionic"  , "Apple GPU (4-core graphics)" , "3 GB" , "NO"              , "12MP"       ,  "2160p@24/30/60fps, 1080p@30/60/120/240fps"  , "7 MP"       , "1080p@30fps" , "5.0, A2DP, LE" , "Yes, with A-GPS, GLONASS, GALILEO, BDS, QZSS" , "YES" , "NO"    , "NO"  , "Li-Ion 1821 mAh") ''')


data = cur.execute("select * from phones")
items  = cur.fetchall()
phone = items;



con.commit()
con.close()