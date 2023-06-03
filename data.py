import gdown
import pandas as pd
import numpy

# import export_40
# gdown.download_folder('https://drive.google.com/drive/folders/15prWrulNe0HMDbF-27YSUPmpU-FIcS-N', quiet=False)
# import export_41
# gdown.download_folder('https://drive.google.com/drive/folders/1k88urhr6Rhfeavtn5nbfShlpCVu3lGDh', quiet=False)
# import export_42(summary)
# gdown.download('https://drive.google.com/uc?export=download&id=1GVjrNHBtBFkV5YUO1mMdDQvTwMe5WFBb', quiet=False)

# process event data (export_41)
event_1 = pd.read_csv('export_41/csv_results_41_255439_mp-01-naamsestraat-35-maxim.csv', sep=';')
event_2 = pd.read_csv('export_41/csv_results_41_255440_mp-02-naamsestraat-57-xior.csv', sep=';')
event_3 = pd.read_csv('export_41/csv_results_41_255441_mp-03-naamsestraat-62-taste.csv', sep=';')
event_4 = pd.read_csv('export_41/csv_results_41_255442_mp-05-calvariekapel-ku-leuven.csv', sep=';')
event_5 = pd.read_csv('export_41/csv_results_41_255443_mp-06-parkstraat-2-la-filosovia.csv', sep=';')
event_6 = pd.read_csv('export_41/csv_results_41_255444_mp-07-naamsestraat-81.csv', sep=';')
event_7 = pd.read_csv('export_41/csv_results_41_255445_mp-08-kiosk-stadspark.csv', sep=';')
event_8 = pd.read_csv('export_41/csv_results_41_280324_mp08bis---vrijthof.csv', sep=';')
event_9 = pd.read_csv('export_41/csv_results_41_303910_mp-04-his-hears.csv', sep=';')
event_1 = event_1.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_2 = event_2.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_3 = event_3.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_4 = event_4.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_5 = event_5.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_6 = event_6.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_7 = event_7.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_8 = event_8.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
event_9 = event_9.drop(columns=['description', 'noise_event_laeq_model_id', 'noise_event_laeq_model_id_unit',
                                'noise_event_laeq_primary_detected_certainty_unit',
                                'noise_event_laeq_primary_detected_class_unit'])
frames = [event_1, event_2, event_3, event_4, event_5, event_6, event_7, event_8, event_9]
event = pd.concat(frames)
event = event.dropna()
event = event[event["noise_event_laeq_primary_detected_certainty"] != 0]
event = event.reset_index(drop=True)
event['result_timestamp'] = pd.to_datetime(event['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')
event['time_of_day'] = pd.cut(event['result_timestamp'].dt.hour,
                              bins=[0, 6, 12, 18, 24],
                              labels=['0:00 - 5:59', '6:00 - 11:59', '12:00 - 17:59', '18:00 - 24:00'], ordered=False)
event['weekday'] = event['result_timestamp'].dt.dayofweek
event['month'] = event['result_timestamp'].dt.month


def event_data():
    return event



# process percentile data (export_40)
percentile_1 = pd.read_csv('export_40/csv_results_40_255439_mp-01-naamsestraat-35-maxim.csv', sep=';')
percentile_2 = pd.read_csv('export_40/csv_results_40_255440_mp-02-naamsestraat-57-xior.csv', sep=';')
percentile_3 = pd.read_csv('export_40/csv_results_40_255441_mp-03-naamsestraat-62-taste.csv', sep=';')
percentile_4 = pd.read_csv('export_40/csv_results_40_255442_mp-05-calvariekapel-ku-leuven.csv', sep=';')
percentile_5 = pd.read_csv('export_40/csv_results_40_255443_mp-06-parkstraat-2-la-filosovia.csv', sep=';')
percentile_6 = pd.read_csv('export_40/csv_results_40_255444_mp-07-naamsestraat-81.csv', sep=';')
percentile_7 = pd.read_csv('export_40/csv_results_40_255445_mp-08-kiosk-stadspark.csv', sep=';')
percentile_8 = pd.read_csv('export_40/csv_results_40_280324_mp08bis---vrijthof.csv', sep=';')
percentile_9 = pd.read_csv('export_40/csv_results_40_303910_mp-04-his-hears.csv', sep=';')
frames = [percentile_1, percentile_2, percentile_3, percentile_4, percentile_5, percentile_6, percentile_7,
          percentile_8, percentile_9]
percentile = pd.concat(frames)
percentile = percentile.drop(
    columns=['description', 'laf005_per_hour_unit', 'laf01_per_hour_unit', 'laf05_per_hour_unit',
             'laf10_per_hour_unit', 'laf25_per_hour_unit', 'laf50_per_hour_unit',
             'laf75_per_hour_unit', 'laf90_per_hour_unit', 'laf95_per_hour_unit',
             'laf98_per_hour_unit', 'laf99_per_hour_unit', 'laf995_per_hour_unit'])
percentile = percentile.reset_index(drop=True)
percentile['result_timestamp'] = pd.to_datetime(percentile['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')


def percentile_data():
    return percentile

"""
# noise level data (every second)
level_11 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_12 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_13 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_14 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_15 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_16 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255444_mp-07-naamsestraat-81.csv", sep=";")
level_17 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_18 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_280324_mp08bis---vrijthof.csv", sep=";")
level_19 = pd.read_csv("D:/MDA/noise_level/Jan/csv_results_42_303910_mp-04-his-hears.csv", sep=";")
frames = [level_11, level_12, level_13, level_14, level_15, level_16, level_17, level_18, level_19]
Jan = pd.concat(frames)
Jan = Jan.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Jan = Jan.reset_index(drop=True)
Jan['result_timestamp'] = pd.to_datetime(Jan['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_21 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_22 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_23 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_24 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_25 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_26 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255444_mp-07-naamsestraat-81.csv", sep=";")
level_27 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_28 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_280324_mp08bis---vrijthof.csv", sep=";")
level_29 = pd.read_csv("D:/MDA/noise_level/Feb/csv_results_42_303910_mp-04-his-hears.csv", sep=";")
frames = [level_21, level_22, level_23, level_24, level_25, level_26, level_27, level_28, level_29]
Feb = pd.concat(frames)
Feb = Feb.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Feb = Feb.reset_index(drop=True)
Feb['result_timestamp'] = pd.to_datetime(Feb['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_31 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_32 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_33 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_34 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_35 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_36 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255444_mp-07-naamsestraat-81.csv", sep=";")
level_37 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_38 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_280324_mp08bis---vrijthof.csv", sep=";")
level_39 = pd.read_csv("D:/MDA/noise_level/March/csv_results_44_303910_mp-04-his-hears.csv", sep=";")
frames = [level_31, level_32, level_33, level_34, level_35, level_36, level_37, level_38, level_39]
March = pd.concat(frames)
March = March.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
March = March.reset_index(drop=True)
March['result_timestamp'] = pd.to_datetime(March['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_41 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_42 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_43 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_44 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_45 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_46 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255444_mp-07-naamsestraat-81.csv", sep=";")
level_47 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_48 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_280324_mp08bis---vrijthof.csv", sep=";")
level_49 = pd.read_csv("D:/MDA/noise_level/April/csv_results_45_303910_mp-04-his-hears.csv", sep=";")
frames = [level_41, level_42, level_43, level_44, level_45, level_46, level_47, level_48, level_49]
April = pd.concat(frames)
April = April.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
April = April.reset_index(drop=True)
April['result_timestamp'] = pd.to_datetime(April['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_51 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_52 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_53 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_54 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_55 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_56 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255444_mp-07-naamsestraat-81.csv", sep=";")
level_57 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_58 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_280324_mp08bis---vrijthof.csv", sep=";")
level_59 = pd.read_csv("D:/MDA/noise_level/May/csv_results_46_303910_mp-04-his-hears.csv", sep=";")
frames = [level_51, level_52, level_53, level_54, level_55, level_56, level_57, level_58, level_59]
May = pd.concat(frames)
May = May.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
May = May.reset_index(drop=True)
May['result_timestamp'] = pd.to_datetime(May['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_61 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_62 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_63 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_64 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_65 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_66 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255444_mp-07-naamsestraat-81.csv", sep=";")
level_67 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_68 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_280324_mp08bis---vrijthof.csv", sep=";")
level_69 = pd.read_csv("D:/MDA/noise_level/June/csv_results_47_303910_mp-04-his-hears.csv", sep=";")
frames = [level_61, level_62, level_63, level_64, level_65, level_66, level_67, level_68, level_69]
June = pd.concat(frames)
June = June.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
June = June.reset_index(drop=True)
June['result_timestamp'] = pd.to_datetime(June['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_71 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_72 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_73 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_74 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_75 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_76 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255444_mp-07-naamsestraat-81.csv", sep=";")
level_77 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_78 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_280324_mp08bis---vrijthof.csv", sep=";")
level_79 = pd.read_csv("D:/MDA/noise_level/Jul/csv_results_48_303910_mp-04-his-hears.csv", sep=";")
frames = [level_71, level_72, level_73, level_74, level_75, level_76, level_77, level_78, level_79]
Jul = pd.concat(frames)
Jul = Jul.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Jul = Jul.reset_index(drop=True)
Jul['result_timestamp'] = pd.to_datetime(Jul['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_81 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_82 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_83 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_84 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_85 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_86 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255444_mp-07-naamsestraat-81.csv", sep=";")
level_87 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_88 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_280324_mp08bis---vrijthof.csv", sep=";")
level_89 = pd.read_csv("D:/MDA/noise_level/Aug/csv_results_49_303910_mp-04-his-hears.csv", sep=";")
frames = [level_81, level_82, level_83, level_84, level_85, level_86, level_87, level_88, level_89]
Aug = pd.concat(frames)
Aug = Aug.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Aug = Aug.reset_index(drop=True)
Aug['result_timestamp'] = pd.to_datetime(Aug['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_91 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_92 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_93 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_94 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_95 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_96 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255444_mp-07-naamsestraat-81.csv", sep=";")
level_97 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_98 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_280324_mp08bis---vrijthof.csv", sep=";")
level_99 = pd.read_csv("D:/MDA/noise_level/Sep/csv_results_50_303910_mp-04-his-hears.csv", sep=";")
frames = [level_91, level_92, level_93, level_94, level_95, level_96, level_97, level_98, level_99]
Sep = pd.concat(frames)
Sep = Sep.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Sep = Sep.reset_index(drop=True)
Sep['result_timestamp'] = pd.to_datetime(Sep['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_101 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_102 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_103 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_104 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_105 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_106 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255444_mp-07-naamsestraat-81.csv", sep=";")
level_107 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_108 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_280324_mp08bis---vrijthof.csv", sep=";")
level_109 = pd.read_csv("D:/MDA/noise_level/Oct/csv_results_51_303910_mp-04-his-hears.csv", sep=";")
frames = [level_101, level_102, level_103, level_104, level_105, level_106, level_107, level_108, level_109]
Oct = pd.concat(frames)
Oct = Oct.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Oct = Oct.reset_index(drop=True)
Oct['result_timestamp'] = pd.to_datetime(Oct['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_111 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_112 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_113 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_114 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_115 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_116 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255444_mp-07-naamsestraat-81.csv", sep=";")
level_117 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_118 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_280324_mp08bis---vrijthof.csv", sep=";")
level_119 = pd.read_csv("D:/MDA/noise_level/Nov/csv_results_52_303910_mp-04-his-hears.csv", sep=";")
frames = [level_111, level_112, level_113, level_114, level_115, level_116, level_117, level_118, level_119]
Nov = pd.concat(frames)
Nov = Nov.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Nov = Nov.reset_index(drop=True)
Nov['result_timestamp'] = pd.to_datetime(Nov['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

level_121 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255439_mp-01-naamsestraat-35-maxim.csv", sep=";")
level_122 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255440_mp-02-naamsestraat-57-xior.csv", sep=";")
level_123 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255441_mp-03-naamsestraat-62-taste.csv", sep=";")
level_124 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255442_mp-05-calvariekapel-ku-leuven.csv", sep=";")
level_125 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255443_mp-06-parkstraat-2-la-filosovia.csv", sep=";")
level_126 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255444_mp-07-naamsestraat-81.csv", sep=";")
level_127 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_255445_mp-08-kiosk-stadspark.csv", sep=";")
level_128 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_280324_mp08bis---vrijthof.csv", sep=";")
level_129 = pd.read_csv("D:/MDA/noise_level/Dec/csv_results_53_303910_mp-04-his-hears.csv", sep=";")
frames = [level_121, level_122, level_123, level_124, level_125, level_126, level_127, level_128, level_129]
Dec = pd.concat(frames)
Dec = Dec.drop(columns=['description', 'lamax_unit', 'laeq_unit', 'lceq_unit', 'lcpeak_unit'])
Dec = Dec.reset_index(drop=True)
Dec['result_timestamp'] = pd.to_datetime(Dec['result_timestamp'], format='%d/%m/%Y %H:%M:%S.%f')

frames = [Jan, Feb, March, April, May, June, Jul, Aug, Sep, Oct, Nov, Dec]
level = pd.concat(frames)
summary_level = level.groupby(pd.Grouper(freq='10Min')).aggregate(numpy.mean)
"""

summary_level = pd.read_csv('level.csv', sep=',')
summary_level['result_timestamp'] = pd.to_datetime(summary_level['result_timestamp'], format='%Y-%m-%d %H:%M:%S')


def level_data():
    return summary_level
