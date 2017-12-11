#!/usr/bin/env python3

"""
    query_processing.py - Matches the query against the saved indexed chunks and returns a list of dictionaries with docID
    author: Nayeem Aquib
    email: nayeemaquib@bennington.edu
    date: 12/1/2017

"""


sample_indexed_chunks_dict = {"strike": {"word_count": 5, "doc_ID": {"13-abc1": [2, 84, 116, 125, 148]}}, "gogh": {"word_count": 24, "doc_ID": {"14-abc1": [12, 21, 103, 129, 186, 211, 224, 268, 312, 343, 373, 430, 447, 485, 567, 624, 671, 747, 789, 815, 859, 896, 1033, 1079]}}, "island": {"word_count": 3, "doc_ID": {"11-abc1": [226, 231, 404]}}, "included": {"word_count": 3, "doc_ID": {"12-abc1": [142, 382, 780]}}, "earth": {"word_count": 3, "doc_ID": {"10-abc1": [75, 87, 348]}}, "accomplishments": {"word_count": 3, "doc_ID": {"11-abc1": [45, 108, 456]}}, "became": {"word_count": 6, "doc_ID": {"12-abc1": [612, 689, 711], "14-abc1": [212, 222], "11-abc1": [95]}}, "year": {"word_count": 3, "doc_ID": {"14-abc1": [155, 331], "13-abc1": [309]}}, "body": {"word_count": 6, "doc_ID": {"12-abc1": [130, 190, 372, 483, 576, 643]}}, "van": {"word_count": 21, "doc_ID": {"14-abc1": [11, 20, 102, 185, 210, 223, 267, 311, 342, 372, 429, 484, 623, 670, 746, 788, 814, 858, 895, 1032, 1078]}}, "flesh": {"word_count": 3, "doc_ID": {"12-abc1": [295, 505, 524]}}, "disappearance": {"word_count": 3, "doc_ID": {"11-abc1": [1, 126, 433]}}, "salt": {"word_count": 10, "doc_ID": {"10-abc1": [103, 127, 156, 207, 227, 273, 279, 290, 366, 478]}}, "known": {"word_count": 3, "doc_ID": {"12-abc1": [88, 803], "14-abc1": [627]}}, "one": {"word_count": 14, "doc_ID": {"14-abc1": [154, 330, 686, 725, 876], "12-abc1": [30, 212, 478, 654], "11-abc1": [10, 361, 435], "13-abc1": [106], "10-abc1": [46]}}, "artist": {"word_count": 3, "doc_ID": {"14-abc1": [122, 580, 979]}}, "life": {"word_count": 11, "doc_ID": {"14-abc1": [8, 62, 92, 112, 133, 181, 546, 745, 830], "11-abc1": [453], "10-abc1": [52]}}, "famous": {"word_count": 3, "doc_ID": {"13-abc1": [388], "12-abc1": [658], "10-abc1": [22]}}, "donner": {"word_count": 3, "doc_ID": {"12-abc1": [665, 676, 741]}}, "could": {"word_count": 4, "doc_ID": {"14-abc1": [46, 290], "10-abc1": [323, 331]}}, "also": {"word_count": 3, "doc_ID": {"12-abc1": [161, 312, 568]}}, "like": {"word_count": 4, "doc_ID": {"10-abc1": [119, 445], "13-abc1": [390], "12-abc1": [293]}}, "fly": {"word_count": 3, "doc_ID": {"11-abc1": [80, 101, 216]}}, "vincent": {"word_count": 4, "doc_ID": {"14-abc1": [10, 19, 916, 1077]}}, "found": {"word_count": 4, "doc_ID": {"14-abc1": [266, 401, 584, 910]}}, "first": {"word_count": 4, "doc_ID": {"14-abc1": [309], "12-abc1": [814], "11-abc1": [97], "10-abc1": [300]}}, "survival": {"word_count": 3, "doc_ID": {"12-abc1": [632, 661, 748]}}, "halley": {"word_count": 4, "doc_ID": {"10-abc1": [307, 310, 402, 452]}}, "left": {"word_count": 4, "doc_ID": {"14-abc1": [421, 492, 862], "12-abc1": [677]}}, "nothing": {"word_count": 3, "doc_ID": {"14-abc1": [135], "13-abc1": [261], "12-abc1": [13]}}, "though": {"word_count": 3, "doc_ID": {"14-abc1": [101], "12-abc1": [337], "10-abc1": [241]}}, "perhaps": {"word_count": 3, "doc_ID": {"12-abc1": [12, 195], "14-abc1": [285]}}, "nearly": {"word_count": 3, "doc_ID": {"14-abc1": [592], "13-abc1": [406], "12-abc1": [370]}}, "alone": {"word_count": 3, "doc_ID": {"11-abc1": [102, 109], "13-abc1": [295]}}, "brother": {"word_count": 5, "doc_ID": {"14-abc1": [149, 217, 295, 908, 921]}}, "salty": {"word_count": 3, "doc_ID": {"10-abc1": [4, 66], "12-abc1": [301]}}, "practice": {"word_count": 4, "doc_ID": {"12-abc1": [57, 99, 159, 610]}}, "tortured": {"word_count": 3, "doc_ID": {"14-abc1": [108, 760, 978]}}, "noonan": {"word_count": 5, "doc_ID": {"11-abc1": [155, 254, 295, 319, 400]}}, "happen": {"word_count": 3, "doc_ID": {"13-abc1": [46, 87, 230]}}, "plane": {"word_count": 3, "doc_ID": {"11-abc1": [177, 267], "12-abc1": [752]}}, "theory": {"word_count": 3, "doc_ID": {"11-abc1": [362, 395, 421]}}, "eventually": {"word_count": 5, "doc_ID": {"14-abc1": [221, 420], "12-abc1": [611, 704], "10-abc1": [239]}}, "incredibly": {"word_count": 3, "doc_ID": {"13-abc1": [201, 324], "11-abc1": [229]}}, "thunderstorm": {"word_count": 3, "doc_ID": {"13-abc1": [96, 257, 416]}}, "human": {"word_count": 10, "doc_ID": {"12-abc1": [21, 172, 294, 383, 398, 424, 449, 504, 523, 642]}}, "later": {"word_count": 6, "doc_ID": {"14-abc1": [384, 951], "13-abc1": [141], "12-abc1": [789], "11-abc1": [183], "10-abc1": [431]}}, "set": {"word_count": 3, "doc_ID": {"11-abc1": [89, 129, 160]}}, "theo": {"word_count": 6, "doc_ID": {"14-abc1": [218, 220, 264, 288, 909, 954]}}, "children": {"word_count": 3, "doc_ID": {"12-abc1": [553, 572], "14-abc1": [194]}}, "american": {"word_count": 3, "doc_ID": {"11-abc1": [281, 442], "12-abc1": [808]}}, "would": {"word_count": 4, "doc_ID": {"14-abc1": [182], "13-abc1": [361], "12-abc1": [475], "10-abc1": [372]}}, "eaten": {"word_count": 3, "doc_ID": {"12-abc1": [91, 316], "14-abc1": [765]}}, "sold": {"word_count": 3, "doc_ID": {"14-abc1": [684, 732], "12-abc1": [522]}}, "thought": {"word_count": 7, "doc_ID": {"12-abc1": [126, 217, 254, 313, 401], "14-abc1": [762, 984]}}, "painter": {"word_count": 3, "doc_ID": {"14-abc1": [59, 631, 657]}}, "died": {"word_count": 5, "doc_ID": {"14-abc1": [152, 277, 682, 947], "12-abc1": [490]}}, "met": {"word_count": 3, "doc_ID": {"14-abc1": [334, 391], "11-abc1": [64]}}, "sea": {"word_count": 4, "doc_ID": {"10-abc1": [54, 296, 477], "11-abc1": [278]}}, "time": {"word_count": 9, "doc_ID": {"14-abc1": [310, 360, 416, 576], "13-abc1": [240, 331, 414], "11-abc1": [53], "10-abc1": [405]}}, "art": {"word_count": 4, "doc_ID": {"14-abc1": [236, 570, 689, 1052]}}, "seawater": {"word_count": 3, "doc_ID": {"10-abc1": [63, 132, 322]}}, "bolt": {"word_count": 3, "doc_ID": {"13-abc1": [187, 265, 344]}}, "still": {"word_count": 5, "doc_ID": {"11-abc1": [338, 354, 460], "12-abc1": [347], "10-abc1": [220]}}, "reached": {"word_count": 4, "doc_ID": {"11-abc1": [185, 203, 222, 401]}}, "never": {"word_count": 3, "doc_ID": {"14-abc1": [73, 477], "13-abc1": [12]}}, "twice": {"word_count": 3, "doc_ID": {"13-abc1": [6, 17, 129]}}, "love": {"word_count": 3, "doc_ID": {"14-abc1": [315, 356], "12-abc1": [106]}}, "epilepsy": {"word_count": 3, "doc_ID": {"12-abc1": [404, 463], "14-abc1": [1007]}}, "leader": {"word_count": 3, "doc_ID": {"13-abc1": [182, 380], "12-abc1": [260]}}, "despite": {"word_count": 3, "doc_ID": {"11-abc1": [84, 261, 445]}}, "well": {"word_count": 3, "doc_ID": {"12-abc1": [74, 386, 712]}}, "fell": {"word_count": 3, "doc_ID": {"14-abc1": [313, 354, 821]}}, "gauguin": {"word_count": 3, "doc_ID": {"14-abc1": [659, 845, 870]}}, "u.s.": {"word_count": 3, "doc_ID": {"11-abc1": [313, 372], "13-abc1": [294]}}, "cannibalism": {"word_count": 14, "doc_ID": {"12-abc1": [0, 22, 71, 143, 168, 325, 352, 360, 607, 662, 707, 735, 749, 781]}}, "ocean": {"word_count": 9, "doc_ID": {"10-abc1": [3, 106, 150, 250, 340, 359, 371, 381], "11-abc1": [330]}}, "britannica.com": {"word_count": 5, "doc_ID": {"14-abc1": [14], "13-abc1": [9], "12-abc1": [11], "11-abc1": [6], "10-abc1": [7]}}, "even": {"word_count": 8, "doc_ID": {"13-abc1": [51, 139, 253, 276], "12-abc1": [67, 407], "14-abc1": [693], "11-abc1": [70]}}, "day": {"word_count": 3, "doc_ID": {"11-abc1": [144, 359], "14-abc1": [885]}}, "cases": {"word_count": 3, "doc_ID": {"12-abc1": [469, 570, 629]}}, "earhart": {"word_count": 13, "doc_ID": {"11-abc1": [4, 8, 37, 111, 152, 252, 293, 298, 317, 365, 398, 430, 450]}}, "struck": {"word_count": 4, "doc_ID": {"13-abc1": [273, 319, 363, 410]}}, "miles": {"word_count": 3, "doc_ID": {"11-abc1": [194, 219], "10-abc1": [140]}}, "long": {"word_count": 3, "doc_ID": {"14-abc1": [76], "13-abc1": [328], "10-abc1": [375]}}, "addition": {"word_count": 3, "doc_ID": {"12-abc1": [121, 203], "14-abc1": [810]}}, "place": {"word_count": 9, "doc_ID": {"13-abc1": [5, 16, 107, 128, 234, 270, 317, 347, 360]}}, "many": {"word_count": 6, "doc_ID": {"14-abc1": [83, 569, 971], "11-abc1": [66, 90], "12-abc1": [604]}}, "water": {"word_count": 10, "doc_ID": {"10-abc1": [9, 11, 58, 80, 99, 107, 147, 218, 267, 360]}}, "normality": {"word_count": 3, "doc_ID": {"14-abc1": [0, 16, 65]}}, "strikes": {"word_count": 6, "doc_ID": {"13-abc1": [13, 105, 215, 228, 307, 371]}}, "people": {"word_count": 3, "doc_ID": {"12-abc1": [335, 703], "11-abc1": [141]}}, "per": {"word_count": 3, "doc_ID": {"10-abc1": [111, 128], "13-abc1": [308]}}, "guinea": {"word_count": 3, "doc_ID": {"12-abc1": [82, 246], "11-abc1": [189]}}, "air": {"word_count": 3, "doc_ID": {"13-abc1": [176], "11-abc1": [276], "10-abc1": [175]}}, "history": {"word_count": 3, "doc_ID": {"11-abc1": [12, 282, 443]}}, "million": {"word_count": 4, "doc_ID": {"10-abc1": [124, 425], "14-abc1": [738], "13-abc1": [302]}}, "within": {"word_count": 3, "doc_ID": {"12-abc1": [248, 739], "14-abc1": [278]}}, "much": {"word_count": 4, "doc_ID": {"14-abc1": [742, 827], "13-abc1": [289], "12-abc1": [16]}}, "however": {"word_count": 6, "doc_ID": {"14-abc1": [521, 715, 780], "11-abc1": [82, 120], "12-abc1": [615]}}, "man": {"word_count": 4, "doc_ID": {"14-abc1": [81, 450, 1037], "12-abc1": [487]}}, "example": {"word_count": 3, "doc_ID": {"12-abc1": [85, 438, 746]}}, "world": {"word_count": 4, "doc_ID": {"12-abc1": [235, 367, 416], "14-abc1": [1053]}}, "lightning": {"word_count": 14, "doc_ID": {"13-abc1": [1, 11, 83, 104, 121, 147, 186, 214, 245, 264, 306, 321, 412, 427]}}, "six": {"word_count": 4, "doc_ID": {"14-abc1": [193, 279, 957, 1021]}}, "cubic": {"word_count": 3, "doc_ID": {"10-abc1": [129, 139, 143]}}, "new": {"word_count": 5, "doc_ID": {"12-abc1": [81, 245, 415], "13-abc1": [396], "11-abc1": [188]}}, "period": {"word_count": 3, "doc_ID": {"13-abc1": [238, 329], "12-abc1": [802]}}, "average": {"word_count": 3, "doc_ID": {"13-abc1": [299], "12-abc1": [641], "10-abc1": [102]}}, "another": {"word_count": 3, "doc_ID": {"13-abc1": [115], "12-abc1": [745], "11-abc1": [217]}}, "used": {"word_count": 6, "doc_ID": {"13-abc1": [31, 53], "12-abc1": [322, 459], "14-abc1": [700], "10-abc1": [333]}}}
N = 1000 #sample_total_number_of_documents

#from index_client import get_index_chunk_metadata