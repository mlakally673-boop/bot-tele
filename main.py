import telebot
from telebot import types

TOKEN = "8690379442:AAHnQ2K_4x6yC0wVnzAR1UE2cF7s9JT1W-8"
bot = telebot.TeleBot(TOKEN)

# ==================== قاعدة البيانات الشاملة للمابات ====================
GAMES_DATA = {
    "blox_fruits": {
        "title": "👇🏻 جميع سكربتات بلوكس فروت",
        "keywords": ["بلوكس فروت", "بلوكس", "blox fruits", "blox fruit", "bloxfruits"],
        "scripts": {
            "bf_1": {"name": "📄 كوانتوم (Quantum Onyx)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Trustmenotcondom/QTONYX/refs/heads/main/QuantumOnyx.lua"))()'},
            "bf_2": {"name": "📄 امرل (Redz Emerald)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bloxfruitsnokey/Redz/refs/heads/main/Emerald/update.luau"))()'},
            "bf_3": {"name": "📄 LinkHive Hub", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/JustParadozCode/LinkHive---Scripts/refs/heads/main/script.lua"))()'},
            "bf_4": {"name": "📄 ريدز (Redz v2)", "code": 'Loadstring(game:HttpGet("https://raw.githubusercontent.com/UCT-hub/main/refs/heads/main/redz-v2"))()'},
            "bf_5": {"name": "📄 ايم بوت (Axl PvP)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/itzaxl/DEVAXL/refs/heads/main/axlpvpblox.lua"))()'},
            "bf_6": {"name": "📄 نايت (WhiteX BF Beta)", "code": 'script_key = "" -- default is FREEMIUM]\nloadstring(game:HttpGet("https://raw.githubusercontent.com/WhiteX1208/Scripts/refs/heads/main/BF-Beta.lua"))()'},
            "bf_7": {"name": "📄 ترايدنت (Banana Trident)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bloxfruitsnokey/Banana/refs/heads/main/Trident/script.luau"))()'},
            "bf_8": {"name": "📄 دراجون هوب (DragonX)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Tdk-Dragon/DragonX.lua/refs/heads/main/DragonX.lua.txt"))()'},
            "bf_9": {"name": "📄 PVP (CentuDox Hub)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/JustParadozCode/CentuDox-Hub/refs/heads/main/CentuDox-Pvp.xyz"))()'},
            "bf_10": {"name": "📄 زن هوب (Zen Hub)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Itz-Npg/Roblox-Script/main/zenhubbf.lua", true))()'},
            "bf_11": {"name": "📄 زي واري (Zware Hub)", "code": 'loadstring(game:HttpGet("https://api.luarmor.net/files/v4/loaders/53f54e99aa490d4741858889f586475a.lua"))()'}
        }
    },
    "egg": {
        "title": "👇🏻 جميع سكربتات سرقة البيض",
        "keywords": ["البيض", "سرقة البيض", "egg", "steal an egg"],
        "scripts": {
            "egg_1": {"name": "📄 AXL Hub Free", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bloxdevaxl/AXL-HUB-LUAU/refs/heads/main/AxlHubEggFree.luau"))()'},
            "egg_2": {"name": "📄 DIVINE HUB V27", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bloxdevaxl/AXL-HUB-LUAU/refs/heads/main/AxlHubEggFree.luau"))()'},
            "egg_3": {"name": "📄 باحث البيض القوي", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bloxdevaxl/AXL-HUB-LUAU/refs/heads/main/DIVINEFIN.luau"))()'},
            "egg_4": {"name": "📄 FlowAuth Egg", "code": 'loadstring(game:HttpGet("https://flowauth.net/v1/loaders/69d3463240384f3a73fbe32c178093a2.lua"))()'},
            "egg_5": {"name": "📄 Jnkie Egg Script", "code": 'loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/338ceeba573ee21d1ce80a020b7923d8bde36038de4511162b01f325b16b9c3f/download"))()'},
            "egg_6": {"name": "📄 لينون هوب (Lennon Hub)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/lennonxscripts/lennonhubv2/refs/heads/main/stealaneggv2"))()'},
            "egg_7": {"name": "📄 ميراندا هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/miirandahub/loader/main/stealaeggs"))()'},
            "egg_8": {"name": "📄 سايبوس (SaiOps)", "code": 'loadstring(game:HttpGet("https://api.saiops.cc/scripts/Steal-An-Egg-Script.lua"))()'},
            "egg_9": {"name": "📄 دورايمون (Doraemon)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Omgshit/Scripts/main/MainLoader.lua"))()'},
            "egg_10": {"name": "📄 انكنون هوب (Unknown)", "code": 'loadstring(game:HttpGet("https://unknownhub.win/api/projects/54474b4c5d5a4f459909c4cb70e7b4f3/loader"))()'},
            "egg_11": {"name": "📄 سكابي (ForgeHub)", "code": 'loadstring(game:HttpGet("https://cdn.forgehub.store/loader"))()'},
            "egg_12": {"name": "📄 زيرو بوينت", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/JaxRol/ZeroPoint/refs/heads/main/KeySystem"))()'},
            "egg_13": {"name": "📄 كامود (CaoMod)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/caomod2077/Script/refs/heads/main/Fn-stealanegg.lua"))()'}
        }
    },
    "keyboard": {
        "title": "👇🏻 جميع سكربتات الكيبورد",
        "keywords": ["الكيبورد", "كيبورد", "keyboard", "speed keyboard"],
        "scripts": {
            "kb_1": {"name": "📄 سوليكس (Solex Hub)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/meobeo8/a/a/a"))()'},
            "kb_2": {"name": "📄 كاتو (Kato Hub)", "code": 'loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/2466cae5b0e0aa7123b3215eae3fb0e8cf0ef4f78071a09a72a401e8b1031207/download"))()'},
            "kb_3": {"name": "📄 لوكسي هوب", "code": 'loadstring(game:HttpGet("https://www.luxyhub.space/api/loader/luxyhub"))()'},
            "kb_4": {"name": "📄 فويد هوب", "code": 'loadstring(game:HttpGet("https://voidon.top/api/loader/main"))()'},
            "kb_5": {"name": "📄 درايغ هوب", "code": 'loadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/fda9babd071d6b536a745774b6bc681c.lua"))()'},
            "kb_6": {"name": "📄 مون لايف", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/71df11b32534fe3b4e657a77dc424940/script/refs/heads/main/main.lua"))()'},
            "kb_7": {"name": "📄 كاكتوس (Cactus Pro)", "code": 'loadstring(game:HttpGet("https://rblxscripts.net/raw/no-key-cactus-hub-pro-1-speed-keyboard-escape-auto-farm-auto-70aa18aa"))()'},
            "kb_8": {"name": "📄 شيزا هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Gerreiro68/ShizaHub/refs/heads/main/loader.lua"))()'},
            "kb_9": {"name": "📄 سبيد (Speed Hub X)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/AhmadV99/Speed-Hub-X/main/Speed%20Hub%20X.lua", true))()'},
            "kb_10": {"name": "📄 اراسكا (Araska)", "code": 'loadstring(game:HttpGet("https://gist.githubusercontent.com/nex-no1/ce10c68544ec307586f36cf1e6d15e98/raw/"))()'},
            "kb_11": {"name": "📄 اورفا (Orva Hub)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/OrvaEvncp/Orva/refs/heads/main/Speed_Keyboard.lua"))()'},
            "kb_12": {"name": "📄 جلاكتك (Galactic)", "code": 'loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/4386aea55612ce01731b47a200b9279bdd9edb81f99334a11e874017e5810257/download"))()'}
        }
    },
    "garden": {
        "title": "👇🏻 جميع سكربتات المزرعة 2",
        "keywords": ["المزرعه 2", "المزرعة", "المزرعه", "grow a garden", "garden"],
        "scripts": {
            "gar_1": {"name": "📄 اديوت هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/IdiotHub/Scripts/main/Loader"))()'},
            "gar_2": {"name": "📄 زيلو هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/aqxius/ZiluHub-Official/refs/heads/main/loader.lua"))()'},
            "gar_3": {"name": "📄 مونديتي", "code": "loadstring(game:HttpGet('https://raw.githubusercontent.com/m00ndiety/Moondiety/refs/heads/main/Loader'))()"},
            "gar_4": {"name": "📄 اكرو هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/nismovxa/acro-hub/refs/heads/main/acro-main"))()'},
            "gar_5": {"name": "📄 لايمن (Lumin)", "code": 'loadstring(game:HttpGet("https://lumin-hub.lol/loader.lua",true))()'},
            "gar_6": {"name": "📄 سنوي هوب", "code": 'loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/4ad6a2d2335968486879c1b1a2dcefc6937ea63c8acb88e703a1ec95a4a146ea/download"))()'},
            "gar_7": {"name": "📄 نيوكس هوب", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/hassanxzayn-lua/NEOXHUBMAIN/refs/heads/main/loader", true))()'}
        }
    },
    "doors": {
        "title": "👇🏻 جميع سكربتات الأبواب (DOORS)",
        "keywords": ["doors", "دورز", "ابواب", "أبواب"],
        "scripts": {
            "doors_1": {"name": "📄 Abysall Doors Loader", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/bocaj111004/Abysall/refs/heads/main/Loader.luau"))()'},
            "doors_2": {"name": "📄 Twinkhook Doors", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/sillyleo67/Doors/refs/heads/main/Twinkhook.lua"))()'}
        }
    },
    "fake_robux": {
        "title": "👇🏻 جميع سكربتات روبوكس وهمي",
        "keywords": ["روبوكس", "روبكس", "وهمي", "robux"],
        "scripts": {
            "fr_1": {"name": "📄 بلوكس فروت روبوكس", "code": 'loadstring(game:HttpGet("https://api.luarmor.net/files/v4/loaders/edf8e1697953b50b341cfcbc21eef492.lua"))()'},
            "fr_2": {"name": "📄 ماب البيض روبوكس", "code": 'loadstring(game:HttpGet("https://pastefy.app/CkaV7ET8/raw"))()'},
            "fr_3": {"name": "📄 مستشفى الحيوانات", "code": 'loadstring(game:HttpGet("https://api.luarmor.net/files/v4/loaders/a56c4dea1088d8f4bf2746ff90060053.lua"))()'}
        }
    },
    "blade_ball": {
        "title": "👇🏻 جميع سكربتات بليد بول (Blade Ball)",
        "keywords": ["بليد بول", "بليد", "blade ball", "blade"],
        "scripts": {
            "bb_1": {"name": "📄 Auto Parry Blade Ball", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Doortthemort/676/refs/heads/main/Main.lua"))()'}
        }
    },
    "blox_strike": {
        "title": "👇🏻 جميع سكربتات بلوكس سترايك (Blox Strike)",
        "keywords": ["بلوكس سترايك", "blox strike", "strike"],
        "scripts": {
            "bs_1": {"name": "📄 BloxStrike Ultimate", "code": 'loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/263b72a117005ed8b7383e97f5d76f1e4aa760ad3d33690acb9b53af04fd2d06/download"))()'}
        }
    },
    "adopt_me": {
        "title": "👇🏻 جميع سكربتات ادوبت مي (Adopt Me)",
        "keywords": ["ادوبت مي", "adopt me", "adopt"],
        "scripts": {
            "am_1": {"name": "📄 ZeroPoint Adopt Me", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/JaxRol/ZeroPoint/refs/heads/main/KeySystem"))()'}
        }
    },
    "steal_brainrot": {
        "title": "👇🏻 جميع سكربتات برينروت (Steal Brainrot)",
        "keywords": ["برينروت", "brainrot", "steal brainrot"],
        "scripts": {
            "sb_1": {"name": "📄 تشيلي (Chilli Script)", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/tienkhanh1/spicy/main/Chilli.lua"))()'}
        }
    },
    "clicker": {
        "title": "👇🏻 جميع سكربتات كليكر سيمولاتور",
        "keywords": ["كليكر", "clicker", "clicker simulator"],
        "scripts": {
            "cs_1": {"name": "📄 Clicker Simulator Hub", "code": 'getgenv().Config = {["Webhook"] = "", ["CPU Saver"] = true}\nloadstring(game:HttpGet("https://api.luarmor.net/files/v4/loaders/5dfdf7ef7126ce180a176d24782d78ac.lua"))()'}
        }
    },
    "tower_of_hell": {
        "title": "👇🏻 جميع سكربتات برج الجحيم (Tower of Hell)",
        "keywords": ["برج الجحيم", "tower of hell", "tower"],
        "scripts": {
            "toh_1": {"name": "📄 Tower of Hell Auto Farm", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Bac0nHck/Scripts/refs/heads/main/toweroffarm.lua"))()'}
        }
    },
    "hole_fishing": {
        "title": "👇🏻 جميع سكربتات صيد الثقب (Hole Fishing)",
        "keywords": ["صيد", "fishing", "hole fishing"],
        "scripts": {
            "hf_1": {"name": "📄 Hole Fishing Hub", "code": 'loadstring(game:HttpGet("https://akkiwi.com/h"))()'}
        }
    },
    "piggy": {
        "title": "👇🏻 جميع سكربتات بيجي (Piggy)",
        "keywords": ["بيجي", "piggy"],
        "scripts": {
            "p_1": {"name": "📄 Piggy NPC Controller", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/BarkleyGerard/myearisrunning/refs/heads/main/2020piggy"))()'}
        }
    },
    "rivals": {
        "title": "👇🏻 جميع سكربتات رايفلز (Rivals)",
        "keywords": ["رايفلز", "rivals"],
        "scripts": {
            "rv_1": {"name": "📄 PulseZax Rivals", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/PulseZax/Loader/refs/heads/main/.lua"))()'}
        }
    },
    "knife_duels": {
        "title": "👇🏻 جميع سكربتات مبارزة السكاكين (Knife Duels)",
        "keywords": ["سكاكين", "knife", "knife duels"],
        "scripts": {
            "kd_1": {"name": "📄 Knife Duels Menu", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/imshrak/knifeduels/refs/heads/main/menu"))()'}
        }
    },
    "mm2": {
        "title": "👇🏻 جميع سكربتات مردر ميستري (MM2)",
        "keywords": ["مردر", "مردور", "mm2", "murder mystery"],
        "scripts": {
            "mm_1": {"name": "📄 Keyless MM2 Script", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Key-less2v/Main-Scriptmm2/refs/heads/main/Murder-Mystery2"))()'}
        }
    },
    "tsb": {
        "title": "👇🏻 جميع سكربتات أقوى ساحة (TSB)",
        "keywords": ["اقوى ساحة", "أقوى ساحة", "tsb", "strongest battlegrounds"],
        "scripts": {
            "tsb_1": {"name": "📄 OPSCRIPT TSB", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/lionun-lab/OPSCRIPT/refs/heads/main/BESTSCRIPTS"))()'}
        }
    },
    "driving_empire": {
        "title": "👇🏻 جميع سكربتات درايفنج امباير (Driving Empire)",
        "keywords": ["درايفنج", "سيارات", "driving empire", "driving"],
        "scripts": {
            "de_1": {"name": "📄 Driving Empire Madara", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/IsThisMe01/Project-Madara/refs/heads/main/drivingempire.lua"))()'}
        }
    },
    "tongue_escape": {
        "title": "👇🏻 جميع سكربتات +1 Tongue Escape",
        "keywords": ["tongue", "tongue escape"],
        "scripts": {
            "te_1": {"name": "📄 +1 Tongue Escape Script", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Bac0nHck/Scripts/refs/heads/main/TongueEscape.lua"))()'}
        }
    },
    "fbs_flick": {
        "title": "👇🏻 جميع سكربتات FBS Flick",
        "keywords": ["fbs", "flick", "fbs flick"],
        "scripts": {
            "ff_1": {"name": "📄 FBS Flick Script", "code": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Bac0nHck/Scripts/refs/heads/main/Flick.lua"))()'}
        }
    },
    "private_server": {
        "title": "👇🏻 سكربت السيرفرات الخاصة المجانية",
        "keywords": ["سيرفر خاص", "سيرفرات خاصة", "private server"],
        "scripts": {
            "ps_1": {"name": "📄 Free Private Server", "code": 'loadstring(game:HttpGet("https://pastefy.app/YoZocJ8O/raw"))()'}
        }
    }
}

# إنشاء الأزرار لكل ماب
def make_game_keyboard(game_key):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for s_id, s_data in GAMES_DATA[game_key]["scripts"].items():
        btn = types.InlineKeyboardButton(text=s_data["name"], callback_data=f"sc_{s_id}")
        markup.add(btn)
    return markup

# أمر البدء /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for g_key, g_data in GAMES_DATA.items():
        title_clean = g_data['title'].replace('👇🏻 جميع سكربتات ', '').replace('👇🏻 ', '')
        btn = types.InlineKeyboardButton(text=f"🎮 {title_clean}", callback_data=f"menu_{g_key}")
        markup.add(btn)
        
    bot.send_message(
        message.chat.id,
        "مرحباً بك! اختر الماب المطلوب من القائمة أو اكتب اسمه مباشرة للبحث:",
        parse_mode="Markdown",
        reply_markup=markup
    )

# البحث النصي
@bot.message_handler(func=lambda message: True)
def handle_text_search(message):
    user_text = message.text.strip().lower()
    found_game = None
    
    for g_key, g_data in GAMES_DATA.items():
        if any(kw in user_text for kw in g_data["keywords"]):
            found_game = g_key
            break
            
    if found_game:
        bot.send_message(
            message.chat.id,
            GAMES_DATA[found_game]["title"],
            reply_markup=make_game_keyboard(found_game)
        )
    else:
        bot.reply_to(message, "❌ لم يتم العثور على الماب، جرب كتابة اسم الماب بشكل مباشر.")

# التعامل مع ضغطات الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("menu_"):
        g_key = call.data.replace("menu_", "")
        if g_key in GAMES_DATA:
            bot.send_message(call.message.chat.id, GAMES_DATA[g_key]["title"], reply_markup=make_game_keyboard(g_key))
            
    elif call.data.startswith("sc_"):
        target_id = call.data.replace("sc_", "")
        for g_key, g_data in GAMES_DATA.items():
            if target_id in g_data["scripts"]:
                s = g_data["scripts"][target_id]
                res = f"📜 **{s['name']}**\n\n`{s['code']}`"
                bot.send_message(call.message.chat.id, res, parse_mode="Markdown")
                bot.answer_callback_query(call.id, text="تم إرسال السكربت!")
                break

print("✅ تم فصل جميع المابات بنجاح وتشغيل البوت...")
bot.infinity_polling()
