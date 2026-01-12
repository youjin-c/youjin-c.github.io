import os
import requests
import time
import random
from urllib.parse import urlparse

# 프로젝트별 이미지 URL 목록
# Admin 페이지에서 Console로 추출한 원본 이미지 URL들
PROJECTS = {
    "Swipe": [
        "https://freight.cargo.site/t/original/i/007735158ba0e27edc2a81cc9dec3bc6bacc2bb3b3e7d90fafa079315fa320d1/ezgif.com-crop-1.gif",
        "https://freight.cargo.site/t/original/i/2df723435c8ae9f110fdcbc4a9e14fce7a6bb28de4ffcc632ab6e8558a409461/Screen-Shot-2019-08-08-at-12.01.22-AM.png",
        "https://freight.cargo.site/t/original/i/3f13b00c32beba1d33432ae9d38360390be20b33ca8f827e0034b60134e310d6/Screen-Shot-2019-08-08-at-12.01.50-AM.png",
    ],
    "Tweequency": [
        "https://freight.cargo.site/t/original/i/bc7be1b18c2bac1fb8dec5f188c6de72bd11171f02adc2a52c674396f76284b9/ScreenShot.png",
    ],
    "Dead-Wood": [
        "https://freight.cargo.site/t/original/i/766017f7a6b2308a3b1e472277cc1d8d97652c5a2a64e908d720735b1cc6ea6b/IMG_4459.JPG",
        "https://freight.cargo.site/t/original/i/5c1c839f8c319b2e57384b26b94228c9b6c817367e746fe23012da358968a775/IMG_4489.JPG",
        "https://freight.cargo.site/t/original/i/f42a83bafe23e0ee073b2bc6315e7b9eb6dc584ab6ed55e9b5b8c877157e4089/IMG_4558.JPG",
        "https://freight.cargo.site/t/original/i/1541afd81f2662f52f0d2aecdf6984cdd3fbc9fc17d545bda8adbba3bbd7b687/IMG_4634.JPG",
        "https://freight.cargo.site/t/original/i/920b7731dcc23dd7e07b12603c77450b89d666752e89e1a1ad603ba18b5dedf4/IMG_4641.JPG",
        "https://freight.cargo.site/t/original/i/2c9d26d5bf11c54c8ba41998a319174c9d2c808e2d9ffd640d70ac6be946fbfc/IMG_4643.JPG",
        "https://freight.cargo.site/t/original/i/3dd9d6d4515f5a3131139d314e81d7357ebfa5aab92dc9bbcfa4f3f034cf120a/youjin_img_1944.jpg",
        "https://freight.cargo.site/t/original/i/515ffc4f6b0aba253f7094148e449770505571f9bf37b33a371e11672caa61dc/youjin_img_1948.jpg",
        "https://freight.cargo.site/t/original/i/ba00d87eb1ff3fb7d022700ba4d73fa98143aa6c0caa477f4ec8a38e4a5eef5d/youjin_img_1960.jpg",
        "https://freight.cargo.site/t/original/i/3f470ab42bba41c448dd730d6d719058fb6527089737c403f1841185a2fe97c4/youjin_img_1968.jpg",
        "https://freight.cargo.site/t/original/i/24b21bab4f1a88b132e8b273a7acbcbdd74ab0fa2a4810d08d703c68bbbee3c1/youjin_img_1981.jpg",
        "https://freight.cargo.site/t/original/i/5bf0f6d832a83f2d23797d9903a424f5e9440563c143f7bf2deffe10e87d1330/youjin_img_1984.jpg",
        "https://freight.cargo.site/t/original/i/17873fe7bfed74826de242ce5a554b1d01ea0a34a7d456e70595161dd963e530/youjin_img_1986.jpg",
        "https://freight.cargo.site/t/original/i/7540605f9b8954c674001c561bc45ad407d5bb4a1b265e9b3e4279db6292f9a1/youjin_img_1992.jpg",
        "https://freight.cargo.site/t/original/i/2cda0c756951ed19f26c2a5961b22ccf9f827ee8c545283d0f3697339e57418c/youjin_img_1996.jpg",
        "https://freight.cargo.site/t/original/i/66a793264336d045f9c0710756f93faf11c518a4ac08e4e9a05764f77151d2e4/youjin_img_1999.jpg",
        "https://freight.cargo.site/t/original/i/ea90bac525de24daae28d03b74d197ae40f54334ccdee06c42ea8cd007cd2adb/youjin_img_2008.jpg",
        "https://freight.cargo.site/t/original/i/71bf59099db701a46c145e7b130afa528c99e18a302c52264b7da5b141a6ed87/IMG_4343.jpg",
        "https://freight.cargo.site/t/original/i/930081a21f31e517a54366466c75588d9ecd894ae71bc95d9c638f5aa7946601/IMG_4404.jpg",
        "https://freight.cargo.site/t/original/i/22234b9b6a444e88f4388fa2784d86eee694ac34514e0d5712d0117b00e2fc59/ezgif.com-crop.jpg",
    ],
    "DoodlAR": [
        "https://freight.cargo.site/t/original/i/fc27a778fa8d2d55d13925a52b59c89a6a3f2452a22a2cedd1c3b3faac7652ed/ezgif.com-video-to-gif.gif",
        "https://freight.cargo.site/t/original/i/d52767b60aa80a8ac4fc777f3199836b6e06bc749b3ca0e9b2299ce9d4cf40e9/ezgif.com-crop.gif",
        "https://freight.cargo.site/t/original/i/1d6a9065773904d276a4c8ac7472948a9a3040aae478ea3eb204688c50b6d4f0/doodleNet_345.gif",
        "https://freight.cargo.site/t/original/i/6d478b752a9811d3743845b571712b5a63b636afc80eced356e2ef774f118d0b/Screenshot-2023-03-07-at-1.32.40-PM.png",
    ],
    "Toonify": [
        "https://freight.cargo.site/t/original/i/2f98e5876704992bc7cca0081b406d661a5e0bd85ab2eddac7df0c621e18f7d9/toonify_original_ratio.gif",
        "https://freight.cargo.site/t/original/i/37e694093fea20f8a8837434065879245c33336acbb60913998c91fe836a95f8/toonify_thumgnail.gif",
        "https://freight.cargo.site/t/original/i/8bb180219b6143eccd8b534e8460c5c444d0a028d39ed5418ecf82cdac15f518/Screenshot-2023-03-03-at-10.50.44-PM.png",
        "https://freight.cargo.site/t/original/i/c82999d1efa2439b98fc5ac7d97e93d1d02882ced466430cb7ce14711a3afafc/Screenshot-2023-03-03-at-10.49.35-PM.png",
    ],
    "Project-Awkward": [
        "https://freight.cargo.site/t/original/i/6488cee4c93194d98192c4a159ca1a39c55417cf012bf4e1851091235c41f915/ezgif.com-gif-maker.gif",
    ],
    "Blow-A-Kiss": [
        "https://freight.cargo.site/t/original/i/5fed07e9e3f402241ee234140cdc36d67134ed4bc7f0b2207ece80106ba29732/IMG_4666.jpg",
        "https://freight.cargo.site/t/original/i/806d2d93bd1d55c046f0d98ee80ae810ed2ca2c1d1d0fe7fc316296a25364837/Untitled_Artwork.png",
        "https://freight.cargo.site/t/original/i/cbb4ecad8f7dbd79c9378004649e56e99939c40a5aa656332855cf5e0d9a45e2/BlowAKiss.png",
        "https://freight.cargo.site/t/original/i/905d613aad038be2ba201abb95f0ea9b086022fedb1fb28758b22090230b9459/ezgif.com-gif-maker-3.gif",
    ],
    "Object-Segmentation": [
        "https://freight.cargo.site/t/original/i/57b46567c0081819618381b79e906153e39590e9ffe858fb5bde2194c27ecad3/coco_cat.png",
        "https://freight.cargo.site/t/original/i/bd49979f015e47996433066aff01f0dcff94784a94eeea9714671c2b7a47f814/coco_ex.png",
        "https://freight.cargo.site/t/original/i/48c4fa393f9304dce22ef767c8fb7bc09e30d4e4f9994d1583a4e5c2940dafc9/img_seg.png",
        "https://freight.cargo.site/t/original/i/80eb6f3509cebca1667756ae1e94ce5f75de84b7d98ca397fea7a1e3076fd291/labeling.png",
        "https://freight.cargo.site/t/original/i/eeeb6b903a4166af8988f9c50c1788a438427f1e97dcde085f558334b1cabf08/labeling2.png",
        "https://freight.cargo.site/t/original/i/ccf15b44e007158288175c502d88a7bb0a052619db92fbc7fe5649bdac5801fc/lime.png",
        "https://freight.cargo.site/t/original/i/9f8822628eb02bbf1930a26d88428b639ae985d1ffd7f1bc7da7b6cd691e4c18/MAL.png",
        "https://freight.cargo.site/t/original/i/5c19425eed73f428712c4ddbdbd974eb2e260e3e1d58ea5074d43c9843149c28/thumbnail.gif",
    ],
    "DICE": [
        "https://freight.cargo.site/t/original/i/9ba670398b63036527f67e1690227085a1227db073d80e47f1caa7ea58a29597/dice0.jpg",
        "https://freight.cargo.site/t/original/i/92a4634f007501f1e2d988cd0416196b3e0ed49bb5cea39dfb7e3d646fc34094/dice1.jpg",
        "https://freight.cargo.site/t/original/i/4b092f016dab9f0a01b30be4ccb7b959b57190e56668297a1f1b55e751d0f4c9/dice2.jpg",
        "https://freight.cargo.site/t/original/i/03a2332b0f4fe8784cee384d308b3642716f1bed963fc2173e7839161dedcde4/dice3.jpg",
        "https://freight.cargo.site/t/original/i/7e308c243be469cf08edd55eda30cba2fafb69393e3a13f54a32111ed3db5e8a/dice4.jpg",
        "https://freight.cargo.site/t/original/i/469e930e6b0e8abb83244bb2f0cce2d7b889fde162b63601a537d962970b387d/dice5.jpg",
        "https://freight.cargo.site/t/original/i/4b189a380cd389c3c84a57f280dd95aeeb4c359511e528bffbef02214f587438/dice6.jpg",
        "https://freight.cargo.site/t/original/i/4ebcbfaa472356c37430eec35adb5837f1110e22c89b79dfb20c4b2febd2e768/dice7.jpg",
        "https://freight.cargo.site/t/original/i/fa365f288035d8bc9a407517dcf4c2a993b519f88a47058124e61fa80f136fe2/dice8.jpg",
        "https://freight.cargo.site/t/original/i/73dbf03ca44a3c4ad46423ba2e4ea8664709b1268b6f1783e8884dba04e8e133/dice9.jpg",
        "https://freight.cargo.site/t/original/i/904a248a67713d75f74d5d604920485b794b646731496a18f6eaa7dfa3d47adc/giphy.gif",
    ],
    "One-Zero": [
        "https://freight.cargo.site/t/original/i/4806c3c32e73ed7661794f50865d11164296067ede849c4b5fe808f2eb1fa817/onezero1.jpg",
        "https://freight.cargo.site/t/original/i/f9430212d6065164efbb75d795cdfb19ea9a23b5fc7e4270abc496d15f0778db/onezero2.jpg",
        "https://freight.cargo.site/t/original/i/6f0346a039322abd5397318be9b82283fe94f5ced997589c5e3c0eddcdf2a6de/onezero3.jpg",
        "https://freight.cargo.site/t/original/i/768a203661bc642473874d5ad46a81fefc59eaf8593f39c35bca15687dac596b/onezero4.jpg",
        "https://freight.cargo.site/t/original/i/df0faf34b5ba923d81d9e1a6ebc20008116310f4e5aaf66809a6185e6b0095af/diagram.png",
        "https://freight.cargo.site/t/original/i/f2a1238cffd9125256893d9cd81a42c88114cc299dfbade6dbc21c1cb6fc35e2/Youjin.gif",
        "https://freight.cargo.site/t/original/i/2c991a88e9f8d1a7ac2016c76c4b3ef13fe3add6a55fc6f1269602e1b5585bbf/audience.gif",
        "https://freight.cargo.site/t/original/i/c248d9a3248aba97eb18982814f2c0d4305c445708bbc6087c44a05025115dec/show.gif",
        "https://freight.cargo.site/t/original/i/ad04e1432856c3349e6d40a0d2ee0a1ed12ef325be051c486a1620fa3d96225d/one-zero5.jpg",
    ],
    "Snapchat-Lenses": [
        "https://freight.cargo.site/t/original/i/74c2e9004ccbd0c8bc978a65647ef33d104fb015d62ce01f4ffee63fe9a16f14/ezgif.com-resize.gif",
    ],
    "Face-Recognition-Games": [
        "https://freight.cargo.site/t/original/i/dcbf26f34719221f8411e86ff305bd881a608fb899aaadfaa227f65d85186491/-180807_BanksyInUs_UX-Flow.gif",
        "https://freight.cargo.site/t/original/i/13df06aba1473faed34933803cfaaf28746695b198081ad5c31eaa7260bef932/-180807_BanksyInUs_UX-Flow.jpg",
        "https://freight.cargo.site/t/original/i/7668c8aaa3e31169ac84e937245a6fa45760747b0e072d6d8b5c40dbca5190a0/ezgif.com-video-to-gif-1.gif",
        "https://freight.cargo.site/t/original/i/9953653b185ec238b1663871735961c312a0a1e566411de5577c0e361189d891/insta01.png",
        "https://freight.cargo.site/t/original/i/d5e7c27c6e335121ef3a8c9c12494d7a663008c4912d83997bf1dc0504ec259f/mainImage.jpg",
        "https://freight.cargo.site/t/original/i/178be0453192858d8be3635886f23986b0cd96e24ed5917470650075ce8b1618/printed-image.jpg",
        "https://freight.cargo.site/t/original/i/78604de074a9b0754cd9e0844f85067604e4832d243dc0abae693ff9149e8aa1/ezgif.com-gif-maker.gif",
        "https://freight.cargo.site/t/original/i/a6f45995dbf0de28e4cff95cedc8fc444624476e0f90a9e1ac1c5fc72b13310f/faceRecTable.png",
        "https://freight.cargo.site/t/original/i/ec6a4364a0ff988d65ebf97dfc97fe5a3a2932584826e87dfa9e6d8529dad630/iceleb_short.gif",
        "https://freight.cargo.site/t/original/i/0c8a0105208354ced7192064a91e43ad7785735356c5bc5a45e91c6ec41540c6/img_1328_edited.jpg",
        "https://freight.cargo.site/t/original/i/91a684864f22461670278a596ec6863e24fb34f64f97f436a2c454eef188ac86/p2280081.jpg",
        "https://freight.cargo.site/t/original/i/61d289eee1c24d49adb78c45caeaccd3d9219c04e6a7c53dee63d780849bc0c8/tuangkamol_thongborisute_img_8657.jpg",
        "https://freight.cargo.site/t/original/i/e302dfc439dde72e97ab8703c69d95c0af6b637761979abb9c0d83a66d068628/tuangkamol_thongborisute_img_8668.jpg",
        "https://freight.cargo.site/t/original/i/184ce083d49853dc58b7c86fd45a9c098bbf8d096b5c52888fd54e7c7f0a416a/tuangkamol_thongborisute_img_8674.jpg",
    ],
    "Go-Card": [
        "https://freight.cargo.site/t/original/i/74d09a3c462e3031b04d19401d8598f88633813a6829182547310080dddba739/3.jpeg",
        "https://freight.cargo.site/t/original/i/fe8e07355da032ab7bc364da9c52daf5f0240a1df644b7a5ed1b2f3c88cd0280/1.jpg",
        "https://freight.cargo.site/t/original/i/a7c218b78c701bc061b40adc6ac64a8ea19f50d8790399326d0eb97cefca3cca/2.jpg",
        "https://freight.cargo.site/t/original/i/215d2e37317e2b6c3759dae208de76f9f1dbb7d981fa07982cfe1f7bcb3638a3/gocard0.jpg",
        "https://freight.cargo.site/t/original/i/ab85a317310c0c59dcf85bfe118e808aee8edbe55afa0b96c6e67a598c82043d/gocard1.jpg",
        "https://freight.cargo.site/t/original/i/0e8927c009c9a330b58094752e2b2540ca7d7e19511db051bb09a73bcf27797b/gocard2.jpg",
    ],
    "Humanphobia": [
        "https://freight.cargo.site/t/original/i/87119b9e0afa9f881de048f2eae132ba8fd0c4af213f5b015f0e117640b12b19/humanphobia.gif",
        "https://freight.cargo.site/t/original/i/d73ff9f35b95b27f8de852d1cbfe7cbfd571458e6c45918562541e432c9c5cff/IMG_0537.JPG",
        "https://freight.cargo.site/t/original/i/c1a2cab26f16ac205a2219408b684000ebc54b4a29ee4a4f397d987f8e5e42aa/ScaredMask_bb.png",
        "https://freight.cargo.site/t/original/i/bd09ec20c50cbbb5e56116103d1cbd1449bb80b8312771e3caa66c4e36e45ffb/IMG_5307.JPG",
    ],
    "ColorPiece": [
        "https://freight.cargo.site/t/original/i/7aed92c570d1a7439e57e3d8792c0e14471db1eaa739738737a8e9263f3638d7/ColorPiece.png",
        "https://freight.cargo.site/t/original/i/224c66e6023ba515177ccb1f0b1d3ac697b20993591d1fa0296e5d11a8a10970/Screen-Shot-2021-04-12-at-3.18.32-AM.png",
        "https://freight.cargo.site/t/original/i/fb367adfa27effb6588e23ca2aa1b29970e60f5955ca044a5dd6c44d4962bbce/ezgif.com-gif-maker-2.gif",
        "https://freight.cargo.site/t/original/i/a3203a095f4ea6f604949998b69eafd657c140d4449f5ffb0611cfeb8467d77a/ezgif.com-gif-maker-3.gif",
        "https://freight.cargo.site/t/original/i/2d5f156b80acc3732601ea76d4bad7ad340c6788958e371c2b30ea6137d371bc/ezgif.com-gif-maker-4.gif",
        "https://freight.cargo.site/t/original/i/f5cb0cbcde932aa04839303cce2b7dd0edebd5591a51310b9972b9be3780e113/ezgif.com-gif-maker.gif",
        "https://freight.cargo.site/t/original/i/8758cf37a30050a31526c91eed04d50e5c610503c63810f20164ff438cfd9bf7/ezgif.com-gif-maker-1.gif",
        "https://freight.cargo.site/t/original/i/da16d4bfbdc550e809004a9da6293979db768d96f36ae054d144e3906ad92512/ColorPieceUXFlow.png",
        "https://freight.cargo.site/t/original/i/140481e635444b550af0a5b6fa0867da55da7c77425a06f592880c725066ec35/ezgif.com-gif-maker.gif",
        "https://freight.cargo.site/t/original/i/ad720612db2e6db20dc28e94bddb989ef9d1a462dfc6aa2c79c0a1ea0349616d/rgb-scatter2.png",
    ],
    "MOTION-RECOGNITION": [
        "https://freight.cargo.site/t/original/i/1533c39b8ecffee56329368eb17435238d9cf8d8df77b11163c7cbec6e48b723/ARCHIVEE23_o.jpg",
        "https://freight.cargo.site/t/original/i/654ec08b9e1dd704cc3ffb08f6e33ee0309d7d1674e5e5ad4d7d31012305965e/motionrecognition1.png",
        "https://freight.cargo.site/t/original/i/b8b5cfe42ce54360c91677af280651ebe792894f23a0d542c3383878fe48132c/w14_motionrecognition_finger.png",
        "https://freight.cargo.site/t/original/i/d944cd1395c4ef4133372c9234effe4f97aa0f412afca241a69547d0f5ebc409/web_finger_move.gif",
    ],
    "The-Tree-of-Babel": [
        "https://freight.cargo.site/t/original/i/92de6a9a4dd3f96562f3afefa796143d2b9b3598fd4ee5af47990f76030371b5/ezgif.com-optimize.gif",
        "https://freight.cargo.site/t/original/i/1f07f5b5862d141b702abc91117a21a5b41cd120eba873c48ea5d5e73792234e/graphCategories_length-1.png",
        "https://freight.cargo.site/t/original/i/85a65f43b4e4ce2803267f1c44cda7ac1feb5243902a6621bbf756c369dd6a01/graphCategories_basic-1.png",
        "https://freight.cargo.site/t/original/i/f2b1719f8fc981ce69c41936348eeed352c09e26592314440d1eee8782663c14/graphCategories_broad.png",
        "https://freight.cargo.site/t/original/i/e07587d9068d55e46e4b50fc607bef26b502114397f20a142326f10e1943e7a7/graphCategories_merged.png",
        "https://freight.cargo.site/t/original/i/61018235a410586f1126686005cffda50de19e4dfcd8b96646bc7f3e70f7718f/graphCategories_cluster-1.png",
        "https://freight.cargo.site/t/original/i/00f414ecd896ff91a8fb91a2cd819bc6f8515b985f17cd0962756d58604bab86/graphCategories_cycle-1.png",
    ],
    "POSTURE-EYE-CARE": [
        "https://freight.cargo.site/t/original/i/5bb19e502a3b2beb2330918a2ab3b5c654a28377ac1fbb8c432645955ee8b86d/ARCHIVEE22_o.jpg",
        "https://freight.cargo.site/t/original/i/b807ead6f449f603488ea001255e7836393b174a6ccb85ffaeef4d7b72816179/-2015-12-30--4.31.13.png",
        "https://freight.cargo.site/t/original/i/1680fcd7ed1a25d8d9c9269b12c85349336f06b49031964e161362e3bebd7692/-2015-12-30--4.40.48.png",
        "https://freight.cargo.site/t/original/i/ea0d6a2b6832e769d5f948368a71a6a89e8b4daffc4f558aebf093cbe2de1e56/-2015-12-30--4.41.20.png",
        "https://freight.cargo.site/t/original/i/f2d5cc490737457e1d88055b5b3172c3f6995b0c56de476fa18387ef98a072be/-2015-12-30--4.41.59.png",
        "https://freight.cargo.site/t/original/i/ef6498feefe5645fec42e1680326d448c1c26bf70d6729a919da3d4dbe1b2871/-2015-12-30--4.42.17.png",
        "https://freight.cargo.site/t/original/i/cc9ec8ba24b3a5e477a1ea0bf4b6f186aa963df01e5fc5f000f480b162035d2c/-2015-12-30--4.43.04.png",
        "https://freight.cargo.site/t/original/i/81faee45d4d94878b792b16457aa30ea5e091ccb26c3efaa2b0316f244c829c0/-2015-12-30--4.43.23.png",
        "https://freight.cargo.site/t/original/i/ee98f7aa0cf03ac24df6f7014571478bf628cc11ed42f32986b1a0db791b8b53/-2015-12-30--4.43.42.png",
    ],
    "SMILE-FACE-IN": [
        "https://freight.cargo.site/t/original/i/f473e938e3372f9b6fb4d9eab151dafe455dac406701442d07581f48e491ed74/ARCHIVEE24_o.jpg",
        "https://freight.cargo.site/t/original/i/daba6cd2588c8f5bfa7aba43e5405063dc0f52dce0d1976f9ff23a27d8dd39aa/lg_face_in_2_01.gif",
        "https://freight.cargo.site/t/original/i/c60bdf7727a3968810b57156231e4774b21103e65e7b9222b8b66ed93203c984/lg_face_in_2_02.gif",
        "https://freight.cargo.site/t/original/i/66e599f74e55f05e8c439bc7a94771ee5dddebfac94ee9be3f0c1d76527db66d/lg_face_in_2_03.gif",
        "https://freight.cargo.site/t/original/i/7b3357ff51997ac8da30ed51e10ff38e410918e8810e5593098a18db4aa6bd6d/lg_face_in_2_04.gif",
        "https://freight.cargo.site/t/original/i/3158d6078f985d0658d0b68140daa6db885e61c3eb3549edc63c0b981c661efe/lg_face_in_2_05.gif",
        "https://freight.cargo.site/t/original/i/e28e11f5691a66b45399313691add99e42e925805fdd66d184c3c2789dcf3136/lg_face_in_2_06.gif",
    ],
    "Sigh-Machine": [
        "https://freight.cargo.site/t/original/i/6a422a39020b80e390e5833868af119bc07c0ab3b7ce3cd0bebb68683e516f50/0.png",
        "https://freight.cargo.site/t/original/i/d7274752b72821ba75dc4347867d2aaf973fb1fd8dbeb0968cab05f250083cff/1.png",
        "https://freight.cargo.site/t/original/i/dd2cbd60edee665974d94d547ccd6199f6825e2c78c2d1bfbec1aef151db628f/3.png",
    ],
    "Sigh": [
        "https://freight.cargo.site/t/original/i/b18a49019a3796cf4e676a66a64c80403b2acac3be305b41fb01ac23259f7a33/IMG_5530.JPG",
        "https://freight.cargo.site/t/original/i/2c033734346baae0e57d8368dff64795c2044993139821e0fdebfffffba72c86/ezgif.com-video-to-gif.gif",
        "https://freight.cargo.site/t/original/i/42e9e832374428e08d5aecdd83acde6220d7b75db52de33832c641a16014f3df/sighmachine.png",
        "https://freight.cargo.site/t/original/i/29601491440e60a19703a0e3ab94e74a17765a9b7340d14063167c75681afb79/IMG_5588.jpg",
    ],
    "Glitch": [
        "https://freight.cargo.site/t/original/i/5aa2cc694fa76cd33249ea3d37b7fa8469e674f13155d8e446933baa2b72bb91/ezgif.com-resize.gif",
        "https://freight.cargo.site/t/original/i/0131923ddc1f1eb5cff952c93cf156382c6367d99dd4b5973fbdd3133f11c4fb/ezgif.com-crop.gif",
        "https://freight.cargo.site/t/original/i/c1f59b40fb7f3c704fa179d595db92990846a616c041de2ff0a2ab59a1858ed3/ezgif.com-resize-2.gif",
    ],
    "Fandamonium": [
        "https://freight.cargo.site/t/original/i/ac137fc5df6830446ac767ab0de5b460714136dc03f1d1ff3fda583407fe46ff/fandamonium.png",
    ],
    "Emotion-Detection": [
        "https://freight.cargo.site/t/original/i/91d02c57b8f7753ece618a3e3a13a6a4f38cc3de18c5b4ed5cc0105182a18c5c/FER2013-0000001434-01251bb8_415HDzL.jpg",
        "https://freight.cargo.site/t/original/i/6d8e7eaa887024c226c76bdf574170e38cfc076f96fc364a0247ae7f3e88a3eb/Screenshot-2023-02-23-at-12.39.14-AM.png",
        "https://freight.cargo.site/t/original/i/6886f38a77b6e8af63c6ec18cab871e2474f2328850b1f490dd4cf4e560add46/im16.png",
        "https://freight.cargo.site/t/original/i/c1a226f7f808404e99a11f852560d35f18fcdf40e52fb6be2eca5c37e5236ecd/28795.png",
        "https://freight.cargo.site/t/original/i/8b4df55c503972b1e42581e7db320087d72ff5f77b198b90b4540666d2946ccd/Screenshot-2023-02-23-at-1.34.47-AM.png",
        "https://freight.cargo.site/t/original/i/6574763c85b8c62e256fb9a9117d83473b562195d9a6e17b87170c9f851a87d8/Screenshot-2023-02-23-at-1.34.56-AM.png",
        "https://freight.cargo.site/t/original/i/06a8cc9ead42d1523753ceb788adf25391bd77a19289345800955b13898c5e8e/1_kmu_t1iNbOipwozjxCG6og.jpeg",
        "https://freight.cargo.site/t/original/i/ea351497f9a612de86ab595d2590b03476fb80a039b05fbb1383b20a54816db9/img_1.png",
        "https://freight.cargo.site/t/original/i/7a0da9542a279191d7846dab500e3fad22e923b2c21ca35962f96f1cf1aa11ed/Screenshot-2023-02-23-at-1.50.07-AM.png",
        "https://freight.cargo.site/t/original/i/5e6de61a28e6578f310bad5287a81ca17b8d2615d0c21117fa61e5b017d7a10c/Screenshot_2021-02-01_at_13.44.53.png",
        "https://freight.cargo.site/t/original/i/9dc90859a5dc1631f600b1bd0e0e6ed28dc9d96da965b6758fc732227222f4b3/Screenshot-2023-02-23-at-1.58.23-AM.png",
        "https://freight.cargo.site/t/original/i/728314c9122f22da1c4f504b57fd4a66838ed92f367dbb733bf3e8913a09fd8e/Screenshot-2023-02-23-at-1.58.27-AM.png",
        "https://freight.cargo.site/t/original/i/7136cda59e340ca6a67862285030cc9f0d74a5783cd0d8905a039f2d82f88694/Screenshot-2023-02-23-at-1.58.27-AM.png",
    ],
    "Smile-Filter": [
        "https://freight.cargo.site/t/original/i/ff3a4a12e3d2cb38547e9e5dfd5f1b5058c28209ed6e1ffd3dea7693a7e64392/thumbnail.png",
        "https://freight.cargo.site/t/original/i/eb2b7deee4f6d3de013345557cc4044fe81599379c77e9e56aaf83e90aebd802/two_image_side0.jpg",
        "https://freight.cargo.site/t/original/i/5138866f1988c40d63854fbaeb25a08ac651229450c94241e19237c4ea4fc94c/two_image_side1.jpg",
        "https://freight.cargo.site/t/original/i/15e62d1fcea93a582300118804f9fedd094ab5a69ca6983a3e4f394561512407/two_image_side2.jpg",
        "https://freight.cargo.site/t/original/i/f1674a851e1e7e245936e4c71eb8ac3bd4276d21930c45de8c3e4f39f32f4bdc/two_image_side3.jpg",
        "https://freight.cargo.site/t/original/i/748a473f3200dffc58f840fecbe40d38b576134a9b8b1bbf8dd64aee58ee7c05/two_image_side4.jpg",
        "https://freight.cargo.site/t/original/i/df9f864b5fb3c5a7fff4cfd015b2dc782a2e378add2ac73fa671055a26c8771c/two_image_side5.jpg",
        "https://freight.cargo.site/t/original/i/c096d89cae2e8303d33a8ccdb3149f20b627b5dfa6ca42b4dbd868736fe3f919/two_image_side6.jpg",
        "https://freight.cargo.site/t/original/i/f6cc33ec02ca4382f34d41a7cb434787b88d10c26089b3c4e5522607f536ea0e/ffhq-teaser.png",
        "https://freight.cargo.site/t/original/i/e76dc237d0281c3884132556a5c27d32581141662c4bd3f4b456bbddfe565f30/cycleGAN.gif",
        "https://freight.cargo.site/t/original/i/f5742c8ffb5999871c1a0c4cba49263a5fef2b0e0ef4ee7e66cdb8adcd8b171d/teaser.png",
    ],
    "Thesis": [
        "https://freight.cargo.site/t/original/i/33433f35f84032cad0cd5ed2969762b0652e0491795202f9531cad05f2c6a6ca/IMG_0518.PNG",
        "https://freight.cargo.site/t/original/i/a76c9409d1ac11062f16ad8641faeac0b43d9153cd3806fdf29beb036bf68c0b/IMG_0519.PNG",
        "https://freight.cargo.site/t/original/i/020ef92d8cf4bf472d8d411a695dfe59ff18cca44ea732ace3f5fa3589c458ce/IMG_0520.PNG",
        "https://freight.cargo.site/t/original/i/0b93060beff21d5a04f7ed4f8f8c0d36301da5e549b26e3df0c5362f065ab91a/IMG_0521.PNG",
        "https://freight.cargo.site/t/original/i/222d97ca30d0248ed05b5bd3d6d9532bf8b6fd52878398ca16d5ea76f1061793/IMG_36316D93889E-1.jpeg",
        "https://freight.cargo.site/t/original/i/b5da51640373e7b8ebb240683c1203352d4beb1afea519d6d95a1ff4b98bf868/onezero.gif",
        "https://freight.cargo.site/t/original/i/87e5a216abe5124a6e780b0a22c908eed182208c2025ce88b9aab8f684b79e5f/onezero1.gif",
        "https://freight.cargo.site/t/original/i/648f4a1294907200a5de3b3b451e3dc7f2aed7c6c98e781a811dd5d58f1ba10d/lady.0.png",
        "https://freight.cargo.site/t/original/i/2fa29a6a70b07c0d488d0be77034b04ac09f5926ba1bdddf895e5a2cb1b83a0b/stanleyparableline.png",
        "https://freight.cargo.site/t/original/i/63e53cf1bbf89da3ff7d29981c34a9a7b19d9319d344a49050b56d127e1b25a3/Youjin.gif",
        "https://freight.cargo.site/t/original/i/dccdd37381c340298a6e447e6ef7328526e7b4e9f8f151d8f7571b5a664f3d23/IMG_0660.JPG",
        "https://freight.cargo.site/t/original/i/0e6ce6ae3401c017efa668fc15352537173f1fa13502739e03927e667a52e190/IMG_0661.JPG",
        "https://freight.cargo.site/t/original/i/50816323f68c5c4d468a4857f2f03d7765018165fb4fab525733d37dbdf52ecb/IMG_0663.JPG",
        "https://freight.cargo.site/t/original/i/9d09293cb0ddd0c98ecfc72303c7b6043b9ef9b80dc52e3cc48c33386a59795b/IMG_0662.JPG",
        "https://freight.cargo.site/t/original/i/e6033ecb6eb8879234ac667961748791ac07c24e7a6d7878cd8132d56f6a429c/Screen-Shot-2019-04-08-at-6.24.36-PM.png",
        "https://freight.cargo.site/t/original/i/578e4de74385fbacee1aa5802ae12672080628edce1c58e2fed5a11badaa89b4/Screen-Shot-2019-04-08-at-6.37.12-PM.png",
        "https://freight.cargo.site/t/original/i/3e06b877f8b2fedf61ec22f0c89083c69cd65fef5c0e227aa9ecc2133fad8cf5/Screen-Shot-2019-04-08-at-6.47.17-PM.png",
        "https://freight.cargo.site/t/original/i/3c59f3cc7b7686a966346d16e1f235f16f63b97a1acbbb79c19a83ba8fdcea2c/poster11_14.png",
        "https://freight.cargo.site/t/original/i/b54995f1cc8a8c9b7ce47fc5de6563a6f6e2747174edc8382cce7f25f98fd697/poster11_14.png",
        "https://freight.cargo.site/t/original/i/c5f82170f72db33d78d38be605926f013397fed53ab71e21bb57e447f09ee22a/41-34-Costruire-i-Libri-Gioco----Chapter---il-labirinto-di-certa.txt.gv.png",
        "https://freight.cargo.site/t/original/i/e9e8e5e4f66ad81e0ea7f5d28539979966c0435ef2aafe6247c6fd585920fc63/39-40-Maps-The-Uncollected-John-Sladek---Alien-Territory.txt.gv.png",
        "https://freight.cargo.site/t/original/i/6d4c95f27192c956db4ae798595f60f02e885fe957637f98f51e40bea8f331df/22-2220Knightmare20--20Fortress20of20Assasins.txt.gv.png",
        "https://freight.cargo.site/t/original/i/02f07617f2f4bad65992bec3ccc79465c571012d76e67c394c6ea59b70d733c4/atkas_100.png",
        "https://freight.cargo.site/t/original/i/365cb8a49443b037e3a82fea8ce5a61275c7028d059cc14711cd9df7cf3796fe/atlas_10.png",
        "https://freight.cargo.site/t/original/i/a282005ac5235c3b295ad1806775f2a95375bcd716e38a4c2c3b85ad9eac16e1/atlas_g_10.png",
        "https://freight.cargo.site/t/original/i/e1bc7dadf26dbc004bba697c193d8b81db3f912a17588ac2422c314b3359eba6/complete_10.png",
        "https://freight.cargo.site/t/original/i/13b0f508621ac84d0d4d4a5fc68c8b65a8329085734cae612a3a5b60f194924d/path.png",
        "https://freight.cargo.site/t/original/i/ad058f512d77bb6d7dccb4215452894de22def176dd7a27e851402ec63c6e5fa/thumbnail.png",
        "https://freight.cargo.site/t/original/i/e725f774464a218fa75de01c31e9c0ae1402fcfeb70b32b3e9bf53b078ac8880/Screen-Shot-2019-04-23-at-5.47.15-PM.png",
        "https://freight.cargo.site/t/original/i/76dd31ccb46c767fd99a3a99aab6a53dfcda158554bb2e961c302b226aeaf807/Screen-Shot-2019-04-23-at-5.47.26-PM.png",
        "https://freight.cargo.site/t/original/i/2563fdae27971632b34d82644937ea7a4bf3bf3fd54a8d29ecf30eeff4566547/Screen-Shot-2019-04-23-at-5.47.38-PM.png",
        "https://freight.cargo.site/t/original/i/c24876012ff1a500e19fd5f85e4b89826c00be156c7148a35000b18a454e7b11/Screen-Shot-2019-04-23-at-5.55.34-PM.png",
        "https://freight.cargo.site/t/original/i/f98f8a7aebbad1344b15ffa07141d4d9a72a251c5e52311a177a9388137f1d1b/graphCategories_basic.png",
        "https://freight.cargo.site/t/original/i/46c909ce3be6bd74cdbd18c65eebbda0996dda3238c1a28ccc0421182494c7f7/graphCategories_cluster.png",
        "https://freight.cargo.site/t/original/i/e47b9d2604299996b822a2c95812238debece3c5a1cd7967980c8079a02b0f7c/graphCategories_cycle.png",
        "https://freight.cargo.site/t/original/i/d1f72daba9540b58a590e88359be930ccb64882d4d817d25b3eb8149540d0546/graphCategories_length.png",
        "https://freight.cargo.site/t/original/i/179ee940ccb0abefc0077e83d8dfec7f08cc429f1000520403ac10bfe892a7f9/graphCategories_merge.png",
        "https://freight.cargo.site/t/original/i/9a2fd1be19d398981a53a5777dc1e715213aa3bdd0a00bb8ed38f21077002869/width.png",
        "https://freight.cargo.site/t/original/i/0b76ae1c89e65cd1ce5b5d210f6f6e9094ec439492fdadc15b27ec28080f0fce/clustering.png",
    ],
    "Machine-Learning-for-the-Web": [
        "https://freight.cargo.site/t/original/i/26d24bdc37199fdd598ffc71022b0ab746aba547b136242026a6b500482aa75e/0.jpg",
        "https://freight.cargo.site/t/original/i/10c728c8652a2008752088560ce57bf76d95ebba16a8bd9277e9d07231603c9d/1.jpg",
    ],
    "Soft-Sensing": [
        "https://freight.cargo.site/t/original/i/890afd807a5ce212b74484205e678d477a42a8c9b47653a31b0f18a10c6baee4/0.jpeg",
        "https://freight.cargo.site/t/original/i/b246e282a894e08b23004738cf9f251d20d61873ace57fef0b0eb3f909021544/Screen-Shot-2019-02-14-at-2.18.35-PM.png",
        "https://freight.cargo.site/t/original/i/fe8e07355da032ab7bc364da9c52daf5f0240a1df644b7a5ed1b2f3c88cd0280/1.jpg",
        "https://freight.cargo.site/t/original/i/a7c218b78c701bc061b40adc6ac64a8ea19f50d8790399326d0eb97cefca3cca/2.jpg",
        "https://freight.cargo.site/t/original/i/74d09a3c462e3031b04d19401d8598f88633813a6829182547310080dddba739/3.jpeg",
        "https://freight.cargo.site/t/original/i/2891326b677a3ee9e07ea10e80c232fde7a28035d876f6d65937ead383ccee49/4.jpeg",
    ],
    "Haptics": [
        "https://freight.cargo.site/t/original/i/94afbe4b10f5b9d4fc041e5f738ac8a47491fbc9f3ce2f293e9af20ecc5ec309/exp0.gif",
        "https://freight.cargo.site/t/original/i/e2fcbe6192cd5102d0c567ae328fec4c0c418ada2f0ad36c17bb6313cdf99fd4/exp1.gif",
        "https://freight.cargo.site/t/original/i/64220d7aa32b858055d1ae3198b79b2fda3bb356653b12c056fee5c824711fdc/exp2.gif",
        "https://freight.cargo.site/t/original/i/4f1a34b1cf2eb71cba2fe083134dead4beda0e7ff186bdfe68f0401b10fabafc/IMG_0292.jpeg",
        "https://freight.cargo.site/t/original/i/768cf976a60540cb8d446d001d4fd6ac792a7dc0d3cf76957729fb8ea849d65b/rainmaker.gif",
        "https://freight.cargo.site/t/original/i/d9b37e748cc553e22507db440da0ec465b34f0097a1f594bb26244c4d84334a6/5c65c3d427b41893901160.gif",
        "https://freight.cargo.site/t/original/i/f4f28ff66ca6b43b6234730a87fbb18d62bf938fb9ed9c97f37f93e1ab778d84/5c65c45375685677846274.gif",
    ],
    "Detourning-the-Web": [
        "https://freight.cargo.site/t/original/i/a7dbae91aa1ce66e1aab0d0a40acd6cd30df25593153c2f853ba4f73b11a6d95/sigh.gif",
        "https://freight.cargo.site/t/original/i/128e0eb7cf693cf7e36c345f8c3047f99ddb0b9eaabd0848578e4cb34ff3d987/lunch.gif",
        "https://freight.cargo.site/t/original/i/82e7cbe945877bc057711a9a5a869c81202779798b1f658f951344f510c9e46e/dongdong2.gif",
        "https://freight.cargo.site/t/original/i/d8f3f39851d85a1c60886cfdd63770879296e636deeb4551518b77302e71e0fd/pineconej.gif",
        "https://freight.cargo.site/t/original/i/40bdbcf63bd5207b40bbffe97e612654350fca2aef7f35231881329ab6210567/manolocampion.gif",
        "https://freight.cargo.site/t/original/i/b61032ed8ca7928e4255cb895e16ccb755a41401aff35d47dbc43cb2ad2e8736/ssup.gif",
        "https://freight.cargo.site/t/original/i/34d80af7c4dfc9b7684325ef74226a7755594ff089a553b0f15b90fb9ea8a848/insta.gif",
    ],
    "Voice": [
        "https://freight.cargo.site/t/original/i/b65ea3341f08239d92792fdbf44ba8f0f1db37d4b48cf6a7023af231f8f830df/0.jpg",
        "https://freight.cargo.site/t/original/i/940d56d2fea79e224611f9e4d5ac6104082079772b9907e3642de13d7f6e78ba/1.jpeg",
        "https://freight.cargo.site/t/original/i/26e983a00094f5b90938d9889301154c06664742bb1a9967b698fcfb3ce64b75/0.gif",
        "https://freight.cargo.site/t/original/i/c0c2b577095eb06faa7a24db4a7ffcbeb62312901cecd837ffe624195569def1/1.png",
        "https://freight.cargo.site/t/original/i/b98e47932a7aa65432d0b38d6e1dd967711a34dcc2bb2a0e64da0803067fa37a/2.png",
        "https://freight.cargo.site/t/original/i/be7389a4bfb158951797f36a11c84f80b2c03ec2bd7e9a0113cbc4cc620a1d41/3.png",
    ],
    "The-rest-of-You": [
        "https://freight.cargo.site/t/original/i/3340c38bb6e129e16d0df8f1fdcabe583b4eeb78b539f0e4260f84f71563cd42/0.png",
        "https://freight.cargo.site/t/original/i/5f417ac630006f328eff6b1c89213a3f571490403cd6c05a0308b5b040f019e1/1.png",
        "https://freight.cargo.site/t/original/i/e1d88f52a8928aef1e0c8255294909d2ed50a938eedc2ef32ad959b53f6ab6ec/2.png",
        "https://freight.cargo.site/t/original/i/f7ecdbb37875ae23ce7449d7a88e6a766c74e02ce1ef2697f1f6a3621fd1d6e1/3.png",
        "https://freight.cargo.site/t/original/i/59f51d37a589bd3e7ea24c72df16fe7959881daafa5a8b7c8e5a969a4b9d7e47/Screen-Shot-2019-02-14-at-12.29.57-PM.png",
        "https://freight.cargo.site/t/original/i/e9b64f6e2361b7b53c9a5175f5ef19512c13a419bef9c060b0ab32c78f094eb8/Screen-Shot-2019-02-14-at-12.30.07-PM.png",
    ],
    "Metabolism": [
        "https://freight.cargo.site/t/original/i/8750f56bdb582c9270ad3e1fae9df80a4eece68eb7aff1f44825abe44ca7f56f/ARCHIVEE4_o.jpg",
        "https://freight.cargo.site/t/original/i/a1436503ccab473eaa66552440005cef79219ec35f0497d79165cbe0f1a45935/ARCHIVEE5_o.jpg",
    ],
    "Habitual-Energy": [
        "https://freight.cargo.site/t/original/i/8750f56bdb582c9270ad3e1fae9df80a4eece68eb7aff1f44825abe44ca7f56f/ARCHIVEE4_o.jpg",
        "https://freight.cargo.site/t/original/i/a1436503ccab473eaa66552440005cef79219ec35f0497d79165cbe0f1a45935/ARCHIVEE5_o.jpg",
    ],
    "Art-Toy-Design": [
        "https://freight.cargo.site/t/original/i/9f0b9f6c6d3c2db3e7805c755440257967cf6e6cff082cfd099783c6f15b01ef/0.jpeg",
        "https://freight.cargo.site/t/original/i/77fa763510cec1f1f3feb5e84abf265242318b9d885e6503fd3c6cb63e269f8f/.jpeg",
        "https://freight.cargo.site/t/original/i/043c0929fcb1190cb21051dcb44935bf225ddd3fdf39f0c10e24d58d60546ba0/2.jpeg",
        "https://freight.cargo.site/t/original/i/036f5e36efa19007fe9e3cb1fb9e6bc56305c024d0925ba006887a6e9b639825/3.jpg",
        "https://freight.cargo.site/t/original/i/b7ccc361183f9b5a85e1fe220768f130447f3ef8e5322909ee77089cb09a4030/0.jpeg",
        "https://freight.cargo.site/t/original/i/d55a6ce30fa82fa98cb736f9d500e70592476424bfeee80ae27273b9cdcadf93/1.jpeg",
        "https://freight.cargo.site/t/original/i/bbe5261270c8bb270a5a4a66b64019725712bd8278f861f2720be68350eb147e/2.jpeg",
        "https://freight.cargo.site/t/original/i/f8e575e59124da548b96b1bcc8bce72a6bab114313639a38171d427750d48fc4/3.jpeg",
        "https://freight.cargo.site/t/original/i/a988afda9b7668491ad239712cba8080ef4e46cc0228d5d4842800a6b65bb363/4.jpeg",
        "https://freight.cargo.site/t/original/i/3ad9c226135cef1680e337c58d5abfd45fb23215abe5be4f35b31b736721d347/5.jpeg",
        "https://freight.cargo.site/t/original/i/3d2871e212da9d0737a51b6c6aa6f1d1e43dfb79d057b54de603b5d672c65e3d/6.jpeg",
        "https://freight.cargo.site/t/original/i/c95a47c0a86c777c24221788acd38d9d1952a1f22429add28da4813ba6c4be41/7.jpeg",
        "https://freight.cargo.site/t/original/i/e78af93065120e153443d5e410320fbd175859b8ba74203730f8321afc4c6663/8.jpeg",
        "https://freight.cargo.site/t/original/i/b3d3bc3cfbea819833d3bf9541cadfa60925ad14d08599dfd2ad25cad55a4693/9.jpeg",
        "https://freight.cargo.site/t/original/i/da19c58086189dcf0fc4a7224c6a8f9943c7426b943343ad5dfed1c074f0af1a/10.jpeg",
        "https://freight.cargo.site/t/original/i/97aa2f7cc00472efde99a8bcf90782c5bff28df1684a87cd85ce83e16d9b13f3/11.jpeg",
        "https://freight.cargo.site/t/original/i/9dd1f46b7b6ff6053e3a91e9f5ffecabb6adcfed504ae95d4464d7c358cfb1c1/12.jpeg",
        "https://freight.cargo.site/t/original/i/ea6de2093d2f7f2eccf9aa79afe4aa6623154014ad3e6d772e462d334284db45/13.jpeg",
        "https://freight.cargo.site/t/original/i/c56664fc0762f932630cd6d4c0f0961fdc770b7ea82f743f09113a234976f698/14.jpeg",
        "https://freight.cargo.site/t/original/i/11316d6c7fe405d7b58d874515d3a87a80ac5f43ea5c5b7544bb344b3a3045bc/15.jpeg",
        "https://freight.cargo.site/t/original/i/db7e5b81e7f865e498a0205821d669f52d10aadfae4de575bae7854a52940196/16.jpeg",
        "https://freight.cargo.site/t/original/i/4b2af5e504d0376cbda9a63e40c65b20266fcb3a2138a06f91fbbe6cdf28b367/17.jpeg",
        "https://freight.cargo.site/t/original/i/ca95fb72bdb23adcd8069842f4efd913a789067b08f3dedcee48141c7a50f646/18.jpeg",
        "https://freight.cargo.site/t/original/i/bbd98f5608fb3141a71f48c97b16ddb8df1e2f5061aac2e67ec6fbab92df8524/19.jpeg",
        "https://freight.cargo.site/t/original/i/71e08acba73fda9cda608499c23a8bd9d830334568298122bcb3e55dc21553ca/20.jpeg",
        "https://freight.cargo.site/t/original/i/74309a8e9ab0208078abf7571a3518501334ca689aca62878616b305bab7049b/00.jpeg",
        "https://freight.cargo.site/t/original/i/7dc1d33302cf94e35e0dc76680c08dc73d603249c0bf29a4ae0fc72b88f1fd7c/11.png",
        "https://freight.cargo.site/t/original/i/d7f61e19d856ed7c0f497b6e33086961782bf5556e1317272879c2be74844322/22.png",
        "https://freight.cargo.site/t/original/i/3dcc2f09518e6128d58aaccbe9907225fd2443821d6f4f26550e059de8a443fe/33.jpg",
        "https://freight.cargo.site/t/original/i/5f6046952f134b1d9fc95836a19e5aef453dd235b963ba9e4fb96d7d5ea52755/44.jpeg",
        "https://freight.cargo.site/t/original/i/0b400e4e1c1c536ea446b328f6c20a423c2c159b0e5b909f0131f6531015ada7/55.jpeg",
        "https://freight.cargo.site/t/original/i/ff02007c193879083252940178e24aeea59bc7c6c4b030a0b7b4793b78f27741/66.png",
        "https://freight.cargo.site/t/original/i/bc22e9b675b316b953f1a888b12596367a04b2afe723f4b7748d32661b77474f/77.jpeg",
        "https://freight.cargo.site/t/original/i/28487301723dd73a3e96cc1dc37797dfa0b00f6226d2f3ec8fe3ef71cce258e1/88.jpeg",
        "https://freight.cargo.site/t/original/i/5c469995c49255edd5effeb977b8b378c8f256575f0b2a4ceca243eeb56d79d6/99.jpeg",
        "https://freight.cargo.site/t/original/i/482de56c5fd4852100471fb99c981a90ad10f7668a796f31c2c5e04200afd664/000.png",
        "https://freight.cargo.site/t/original/i/dbcab9498919981f97d51aea9c9367cfb9794a6fe28472d1a51a5b41fa64bb78/111.png",
        "https://freight.cargo.site/t/original/i/e952c5a7f0badb01ff6f2686ccc8b8639daf95703c393e3972d11bea0429a3b4/222.png",
        "https://freight.cargo.site/t/original/i/b27d6236958ac6476aca93e3628acd1525d53cbc765b2189447bf799211a3cb9/333.png",
        "https://freight.cargo.site/t/original/i/2a229d58eedaedcc103412e52fe15831ba2f5e6fbfa33e59601abbbbc3c0a82a/444.png",
        "https://freight.cargo.site/t/original/i/ae42b48770de7275b8789a30e9b44309b5481213b06a2c8f80514a777b181e1b/555.png",
        "https://freight.cargo.site/t/original/i/90cae5adbd36f4bf291a8d4468b5b4f9437fcadd67c6f08f0796ea5f5b1ad826/666.png",
        "https://freight.cargo.site/t/original/i/42ddc7b4f423086422f9826ef224eb536e627cfa9b2917468e2263793a6599aa/777.jpeg",
        "https://freight.cargo.site/t/original/i/2c411ebf546666780dbc54bd77b8e09586a51e0d83fe12d9b905f4df2f65ace0/888.jpeg",
        "https://freight.cargo.site/t/original/i/74642f1e4c3346175f0cd9cb588c3e6e3325639eab693615bab6291ecb7e5e4f/999.jpeg",
        "https://freight.cargo.site/t/original/i/74a9c8ee3c111ca3f97cd9c4c70f1568b0e2868a4b268e024c9c3156db99a9be/1010.jpeg",
        "https://freight.cargo.site/t/original/i/1f7d57ed1f7b6940a8bfe1becfbb7808989f405ce1d889f747e16d42f742e140/1111.jpeg",
        "https://freight.cargo.site/t/original/i/5b196e8e19c3ad33103ab16e136ca70624d2341aea4d6e37ac5284829e90760d/1212.jpeg",
        "https://freight.cargo.site/t/original/i/2cb67648c9fdb18b4340d543561d7767237f4eb651546922ae6c3e946ff1052d/1313.jpeg",
        "https://freight.cargo.site/t/original/i/c08fab7cdbdfa0576fa0a0fe20a89b5c5b2fc97bb5eeb1d4bd527fab18d76fc4/1414.jpeg",
        "https://freight.cargo.site/t/original/i/218c165c097e8a7ca7aa91cf1860f869523358b6208a5b8d85692c4338d45448/1515.jpeg",
        "https://freight.cargo.site/t/original/i/3f71516534e652863f24b95f31c62e28984e24227371c8a30ebe18422f0cfb8c/1616.jpeg",
        "https://freight.cargo.site/t/original/i/ca7430c1851a884f3607e58686933b13758c5c8c2d1edee411f082f4e96bd414/1717.jpeg",
        "https://freight.cargo.site/t/original/i/ccc9e6bb680076f32dea0076056e21dd9ceb5a8b18e45bb0e8ed9f7506b7f036/A.jpeg",
        "https://freight.cargo.site/t/original/i/fbe70f9546ee35b8ead735fd9fdac9e0eac66aa80962dbfb8df6f71759df1242/B.jpeg",
        "https://freight.cargo.site/t/original/i/8ccbc689ed1bd3d7ee0e395753f511f205270133c683fa7134045e1ab8d16a12/C.jpeg",
        "https://freight.cargo.site/t/original/i/8490296d7f46c1a5a709fcacc2c31c50a383fd4904096b1b1c25f4b34018f8fc/D.jpeg",
        "https://freight.cargo.site/t/original/i/b1136962f45aea54b1b79248bffc4933a3ccf3255182ec7b2481ccd0ea14676f/Screen-Shot-2019-02-14-at-1.14.17-PM.png",
        "https://freight.cargo.site/t/original/i/945b1c3e582c9ef7d5e1645f950e9db8c96c09649b608cc13e74d6600541669b/Screen-Shot-2019-02-14-at-1.14.25-PM.png",
        "https://freight.cargo.site/t/original/i/a8d4c22f78d6c81f4f962cefef04e39dd7d187b7509e69ea511259ba07c14fea/Screen-Shot-2019-02-14-at-1.15.04-PM.png",
        "https://freight.cargo.site/t/original/i/b588dd2f35c6f4ce0f3f3a948adcc19185d5469fb891d9f975481b89e2cbb627/Screen-Shot-2019-02-14-at-1.15.27-PM.png",
        "https://freight.cargo.site/t/original/i/b309fa8c8af50a36cc45a2dfa3460254ecd96627942cd262aac3aee4dde2c301/Screen-Shot-2019-02-14-at-1.18.13-PM.png",
        "https://freight.cargo.site/t/original/i/732ce696723420cc6f3c890f42ac3276ac7e42a19d64249952bed7824215e808/f.jpeg",
        "https://freight.cargo.site/t/original/i/98b17e7a9f33443c56ebf2dcf7326f5f51ad30627f2b4bdc04458db90ed457a3/g.jpeg",
        "https://freight.cargo.site/t/original/i/2ba0610c101f208efe6565fa5a7164ae300e9bb2099511471c96cfe66a56d4de/h.jpeg",
        "https://freight.cargo.site/t/original/i/8430a99499f9ed379d5c6766776c4c1ae57355b8b0fceacfb2e3e4cd237ee0bf/i.jpeg",
        "https://freight.cargo.site/t/original/i/bbeddbe39cadb33eddc3f4c8c6ce1e151bc57bca4ab781b0d41b168dfda532ca/j.jpeg",
        "https://freight.cargo.site/t/original/i/195f431081f371cc1e1955606ec85ddaf799d6f094bf8bb3576450128dc3b368/k.jpeg",
        "https://freight.cargo.site/t/original/i/8890b28c340beffb5da9f2d2ee91887f890cf47fd1b952a7901de05b199d58c8/l.jpeg",
        "https://freight.cargo.site/t/original/i/0086ba2d2138c554467b6df6804e8305afdb87c5a29cde49423172fdf96a6692/m.jpeg",
        "https://freight.cargo.site/t/original/i/ca90ab6a596e876f85d95407dcd30e67f99d6a2c4884b05c282a4e71f74ce131/o.jpeg",
        "https://freight.cargo.site/t/original/i/d996ccae5ec15e6cd2264acec49cfd4c9f407470c315e439c9d9567ee009fc99/output.gif",
        "https://freight.cargo.site/t/original/i/c07ad6a3f223e13c1d7685dd8696e63befd8604047b1fd110e1ebdf821448eeb/p.jpeg",
        "https://freight.cargo.site/t/original/i/21ccbeb33e3ff0436e2813f9b7d99ad363efc57e32a4dd84e05006bb34598cf9/aa.png",
        "https://freight.cargo.site/t/original/i/979d015beba492407eb38246c5c1a993dbbbea060da7c2226c8b9327dfce029b/bb.jpeg",
        "https://freight.cargo.site/t/original/i/ad6fa03d79a69caf930199a280cb1b0dbf13ff39f375099f3327532f6871832c/cc.jpeg",
    ],
    "Generative-Music": [
        "https://freight.cargo.site/t/original/i/ca0e3c5f009c0ae4531eb7c78f90f361d69c3b5e251e96d9193194a75ff8d949/0.png",
        "https://freight.cargo.site/t/original/i/630b0d622ff02722221f911849cbc20433b17b5ccbbc109b18c8929cc80d8673/1.png",
        "https://freight.cargo.site/t/original/i/34364c471a31950c0d9026c447b4e57f60abc17dfab8c4d244245abad22dafa4/2.png",
        "https://freight.cargo.site/t/original/i/6196fe4eca27aafa897672cad07a4d6d39c352bd840f7339cc5883884dbf15ed/3.png",
        "https://freight.cargo.site/t/original/i/761979321e1b0cd387b5396fb98a89ae4536bc6592a66e368024a1dd899015bf/4.jpg",
    ],
    "Design-for-Discomfort": [
        "https://freight.cargo.site/t/original/i/66440f9fe4043956aff74de6f2b262368793a9e2034f6e3d424f3ee07f6bc262/0.jpeg",
        "https://freight.cargo.site/t/original/i/0cdcf7e6e5baf4f49eb698979efa8ce9ade7af14c4556732040fc4dd57f6fbba/1.jpeg",
        "https://freight.cargo.site/t/original/i/2a7dc821951658805138e490162b4738106bf9042b4e79a8af1d58169b3a2513/2.jpeg",
        "https://freight.cargo.site/t/original/i/f73f47075bdd6298e0e9c7dfa7ce25f74bf6661c586f67b5921cddae8390fe95/3.jpeg",
        "https://freight.cargo.site/t/original/i/26e77db81321f7224a6cd0e9307d4290fe0a457ce152ad45f8affa59ff087a01/4.jpeg",
        "https://freight.cargo.site/t/original/i/23b343920491c4b29e668489ce4549d22c0cdd915e5408c30853b4bdfddf409a/5.jpeg",
        "https://freight.cargo.site/t/original/i/16ff0a530b67eb881ee863e817defe2e3fdedb6418f7d0e648ef0ba31126a46b/6.jpeg",
        "https://freight.cargo.site/t/original/i/0e9b9dc1b21b58538780d81e784aaea89ed061dffb4c4f2e543de730fd993590/7.jpeg",
        "https://freight.cargo.site/t/original/i/5ddabbdee09a484974e41a5fa53974c1fe0b276e54dc01b30a5425bf2e8d1742/8.jpeg",
        "https://freight.cargo.site/t/original/i/b5b9e11f28bb68c5bf67b4cdbf47e0e8195a16ff6925c59fa63a9facfc92b87d/9.jpeg",
        "https://freight.cargo.site/t/original/i/23c825100ed81a41a8e2a0711ff9b4ef4962cda10560d14d2d5525c1f0909038/10.jpeg",
        "https://freight.cargo.site/t/original/i/7ed7c82f9caf2343b057c231f2ee4bee2560a64d9bd3540dedb72bc97f238609/a.jpg",
        "https://freight.cargo.site/t/original/i/cbc1e347212d943fa440cf972e1ec24ce028e1e4e50d584d867c865d1f27874d/b.jpeg",
        "https://freight.cargo.site/t/original/i/3bb14f50165ba053b1209c0dad4450326c4d8bf137a395de36b5b5414ac72f67/c.png",
        "https://freight.cargo.site/t/original/i/ec0c2afc93c51097b480c0d2d47decb57a5a105ba9cfd0e144a1c7e0f0312dd5/d.jpg",
        "https://freight.cargo.site/t/original/i/a16a459323f7339f123609497c44d8696b3bc80a33d5dc7a33921380d193c8bb/e.jpg",
        "https://freight.cargo.site/t/original/i/c3782222048374c63faeeec3701fa7a23ab439a48137c00bbe362f3aa77d97ee/z.jpg",
        "https://freight.cargo.site/t/original/i/12bd90c030bd6aaef5f505cbe46042e4cb68a629b56e4c49aacf63e3d73e2c79/zz.jpg",
    ],
    "Game-Design-and-Psychology": [
        "https://freight.cargo.site/t/original/i/c392852aa0505d992d347680c51a9972c710524c14f6f66dfe97757e2e02de72/0.png",
        "https://freight.cargo.site/t/original/i/f8971e69f72aff211ae9161e8a53d91e99f6e607f2affab10af8b9060da612f7/3.png",
        "https://freight.cargo.site/t/original/i/d90aa0b65c8684ee786b0b6df54582409387b0665134b830702c30cfe1013b25/1.png",
        "https://freight.cargo.site/t/original/i/74d5c57620e999029972408b5f409b833856ef7d5d41dd4412e06a66afc15412/2.png",
        "https://freight.cargo.site/t/original/i/82fbeb0bdc6f6e95f0ec227f31c93bc8af654da5d850d63a49136a227b2d1ccb/3.png",
        "https://freight.cargo.site/t/original/i/50b531afb1e91965bff72cf32f6b2c4fb045db0e5470e8888bf58994ccb05636/4.png",
    ],
    "Tweet-Reader": [
        "https://freight.cargo.site/t/original/i/40663f4e56c54c84b96fa9ba944891d10c20247797ade384a050d048c6b88097/logo.png",
        "https://freight.cargo.site/t/original/i/04a0642f0c3f1df339c2b1d4916472f1fd443f964b2e8a5c9ca698c681fffa9d/thumbnail.png",
    ],
}

OUTPUT_ROOT = "/Users/youjin/Documents/youjin-c.github.io/cargo-collective/images"

def download_images(project_name, urls):
    """프로젝트의 이미지들을 다운로드"""

    output_dir = os.path.join(OUTPUT_ROOT, project_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"프로젝트: {project_name}")
    print(f"이미지 수: {len(urls)}")
    print(f"저장 경로: {output_dir}")
    print('='*50)

    success_count = 0

    for i, url in enumerate(urls):
        filename = os.path.basename(urlparse(url).path)
        filepath = os.path.join(output_dir, filename)

        # 이미 존재하면 스킵
        if os.path.exists(filepath):
            print(f"  [{i+1}/{len(urls)}] 이미 존재: {filename}")
            success_count += 1
            continue

        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"  [{i+1}/{len(urls)}] 다운로드 완료: {filename}")
                success_count += 1
            else:
                print(f"  [{i+1}/{len(urls)}] 실패 (HTTP {response.status_code}): {filename}")
        except Exception as e:
            print(f"  [{i+1}/{len(urls)}] 에러: {filename} - {e}")

        # 429 방지 딜레이
        if i < len(urls) - 1:
            delay = random.uniform(1, 3)
            time.sleep(delay)

    print(f"\n완료: {success_count}/{len(urls)} 이미지 다운로드")
    return success_count

def main():
    print("=" * 60)
    print("Admin 페이지에서 추출한 원본 이미지 다운로드")
    print("=" * 60)

    total_success = 0
    total_images = 0

    for project_name, urls in PROJECTS.items():
        total_images += len(urls)
        total_success += download_images(project_name, urls)

    print("\n" + "=" * 60)
    print(f"전체 완료: {total_success}/{total_images} 이미지")
    print("=" * 60)

if __name__ == "__main__":
    main()
