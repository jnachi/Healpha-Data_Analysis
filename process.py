def process():
    import pandas as pd
    df = pd.read_csv("branch_Wise.csv", keep_default_na=False)
    df = df[df.generic_tempcolor != 'null']
    # den_red = (df['dentcolor'][df['dentcolor'] <= 9]).count()
    # den_amber = (df['dentcolor'][(df['dentcolor'] > 9) & (df['dentcolor'] <= 10.5)]).count()
    # vit_red = (df['vitcolor'][df['vitcolor'] <= 6]).count()
    # vit_amber = (df['vitcolor'][(df['vitcolor'] > 6) & (df['vitcolor'] <= 7)]).count()
    # eye_red = (df['eyecolor'][df['eyecolor'] <= 14]).count()
    # eye_green = (df['eyecolor'][df['eyecolor'] == 15]).count()
    df['entcolor'] = df['entcolor'] * (15 / 20)
    # ent_amber = (df['entcolor'][(df['entcolor'] > 9) & (df['entcolor'] <= 10.5)]).count()
    # ent_red = (df['entcolor'][df['entcolor'] <= 9]).count()
    df['phycolor'] = df['phycolor'] * 18 / 33
    df['phy_color_final'] = df['phycolor'] + df['ergcolor'] + df['hygcolor']
    # phy_red = (df['phy_color_final'][df['phy_color_final'] <= 23.125]).count()
    # phy_amber = (df['phy_color_final'][(df['phy_color_final'] > 23.125) & (df['phycolor'] <= 23.75)]).count()
    array = df['branch_id'].unique()
    dic = {}
    for i in array:
        df1 = df[df['branch_id'] == i]
        den_red = df1['dentcolor'][df1['dentcolor'] <= 9].count()
        den_amber = df1['dentcolor'][(df1['dentcolor'] > 9) & (df1['dentcolor'] <= 10.5)].count()
        vit_red = df1['vitcolor'][df1['vitcolor'] <= 6].count()
        vit_amber = df1['vitcolor'][(df1['vitcolor'] > 6) & (df1['vitcolor'] <= 7)].count()
        ent_red = df1['entcolor'][(df1['entcolor'] <= 9)].count()
        ent_amber = df1['entcolor'][(df1['entcolor'] > 9) & (df1['entcolor'] <= 10.5)].count()
        eye_red = df1['eyecolor'][df1['eyecolor'] <= 14].count()
        eye_green = df1['eyecolor'][df1['eyecolor'] > 14].count()
        phy_red = df1['phy_color_final'][df1['phy_color_final'] <= 23.125].count()
        phy_amber = df1['phy_color_final'][ (df1['phy_color_final'] > 23.125) & (df1['phy_color_final'] <= 23.75)].count()
        vit_cols = []
        for k in df1.columns:
            if (k.find("generic") == 0):
                vit_cols.append(k)
        vit_no = df1[vit_cols][(df1[vit_cols] == '0') | (df1[vit_cols] == '0.5')].count(axis=1)
        vit_atleast1 = vit_no[vit_no >= 1].count()
        phy_cols = []
        for k in df1.columns:
            if ((k.find("pickle") == 0) | (k.find("sysexam") == 0)):
                phy_cols.append(k)
        phy_no = df1[phy_cols][(df1[phy_cols] == '0') | (df1[phy_cols] == '0.5')].count(axis=1)
        # phy_atleast1 = phy_no[phy_no >= 1].count()
        erg_cols = []
        for k in df1.columns:
            if (k.find("ergonomics") == 0):
                erg_cols.append(k)
        erg_no = df1[erg_cols][(df1[erg_cols] == '0') | (df1[erg_cols] == '0.5')].count(axis=1)
        # erg_atleast1 = erg_no[erg_no >= 1].count()
        hyg_cols = []

        for k in df1.columns:
            if (k.find("hygiene") == 0):
                hyg_cols.append(k)
        hyg_no = df1[hyg_cols][(df1[hyg_cols] == '0') | (df1[hyg_cols] == '0.5')].count(axis=1)
        # hyg_atleast1 = erg_no[hyg_no >= 1].count()
        phy_atl = phy_no[phy_no >= 1].index
        erg_atl = erg_no[erg_no >= 1].index
        hyg_atl = hyg_no[hyg_no >= 1].index
        phy_final = list(set(phy_atl) | set(hyg_atl) | set(erg_atl))
        phy_final = set(phy_final)
        phy_atleast1=len(phy_final)
        dent_cols = []
        for k in df1.columns:
            if (k.find("dental") == 0):
                dent_cols.append(k)
        dent_no = df1[dent_cols][(df1[dent_cols] == '0') | (df1[dent_cols] == '0.5')].count(axis=1)
        dent_atleast1 = dent_no[dent_no >= 1].count()
        ent_cols = []
        for k in df1.columns:
            if (k.find("ent") == 0):
                ent_cols.append(k)
        ent_no = df1[ent_cols][(df1[ent_cols] == '0') | (df1[ent_cols] == '0.5')].count(axis=1)
        ent_atleast1 = ent_no[ent_no >= 1].count()
        eye_cols = []
        for k in df1.columns:
            if (k.find("eye") == 0):
                eye_cols.append(k)
        eye_no = df1[eye_cols][(df1[eye_cols] == '0') | (df1[eye_cols] == '0.5')].count(axis=1)
        eye_atleast1 = eye_no[eye_no >= 1].count()

        dic[i] = { 'dental':
                      {'red': int(den_red),
                       'amber': int(den_amber),
                       'atleast': int(dent_atleast1)
                      },
                  'ent':
                      {'red': int(ent_red),
                       'amber': int(ent_amber),
                       'atleast': int(ent_atleast1)
                      },
                  'vitals':
                      {'red': int(vit_red),
                       'amber': int(vit_amber),
                       'atleast': int(vit_atleast1)
                      },
                  'physical':
                      {'red': int(phy_red),
                       'amber': int(phy_amber),
                       'atlest': int( phy_atleast1)
                      },
                  'eye':
                      {'red': int(eye_red),
                       'amber': 0,
                       'atleast': int(eye_atleast1)
                      }
                }
    return (dic)
# print(process())

