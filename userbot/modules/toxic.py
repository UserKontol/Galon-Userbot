from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import galoncmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@galoncmd(pattern='d(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NGENTOTTT!!BAPA LU SURUH RIBUT SAMA GUA**")


@galoncmd(pattern='e(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK USAH SOK KERAS GOBLOK!!KENCING MASIH BERDIRI AJA BELAGU**")


@galoncmd(pattern='f(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL HAHAHAHA!!**")


@galoncmd(pattern='i(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL MASIH BENGKOK AJA BANGGA LU HAHAHAHA!!**")


@galoncmd(pattern='r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL KONTOL APA YANG BESAR?KONTOL LU LAH HAHAHAHA!!**")


@galoncmd(pattern='t(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI!!KONTOL!!NGENTOT!!!**")


@galoncmd(pattern='u(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!GANTENGAN JUGA GUA HAHAHAHA**")


@galoncmd(pattern='w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA**")


@galoncmd(pattern='z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")


@galoncmd(pattern='k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI PERKENALKAN NAMA SAYA GAK TAU LUPA!!**")


@galoncmd(pattern='n(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIMANA KABAR KAMU SAYANG??APAKAH BAIK?**")


@galoncmd(pattern='b(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ELEEEHHHH SOK BANGET KEPINTERAN KAMU!!**")


@galoncmd(pattern='m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**INI GRUB APA KUBURAN SEPI BANGET ASTAGFIRULLAH!!**")


@galoncmd(pattern='c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA JANGAN NGEYEL!!**")


@galoncmd(pattern='s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH KAMU!!**")


@galoncmd(pattern='v(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU HMM!!**")


@galoncmd(pattern='j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAAF BUKAN JAGOAN HAHAHAHA!!**")


@galoncmd(pattern='a(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BISMILLAH SLEEP CALL!!😁**")


@galoncmd(pattern='g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GANTENG LU BEGITU???**")


@galoncmd(pattern='y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin,Keras di sosmed Bhakss...**")


@galoncmd(pattern='h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CANTIK LU BEGITU???**")


@galoncmd(pattern='o(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MENTANG MENTANG PUNYA BOT MAINNYA BOT!!PANTES MUKANYA KAYA BOT😁**")


@galoncmd(pattern='1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NORAK LU KONTOL!! MAKE USERBOT CUMAN BUAT WAR MALAH SOK KERAS**")


CMD_HELP.update({
    "toxic":
    f"{cmd}d\
\nUsage: Bacotin Orang.\
\n\n{cmd}e\
\nUsage: Buat Orang Yang Sok Keras.\
\n\n{cmd}f\
\nUsage: Ngatain Orang Wkwkkw.\
\n\n{cmd}i\
\nUsage: Kontol Orang Ngatain.\
\n\n{cmd}r\
\nUsage: Pantun Anjing.\
\n\n{cmd}t\
\nUsage: Nyebutin Binatang.\
\n\n{cmd}u\
\nUsage: Biar Dikata Ganteng.\
\n\n{cmd}w\
\nUsage: Biar Dikata Cantik.\
\n\n{cmd}z\
\nUsage: Tremor Kan Lu.\
\n\n{cmd}k\
\nUsage: Memperkenalkan Diri.\
\n\n{cmd}n\
\nUsage: Menanyakan Kabar.\
\n\n{cmd}b\
\nUsage: Sok Kepinteran.\
\n\n{cmd}m\
\nUsage: Gc Nya Kaya kuburan.\
\n\\{cmd}c\
\nUsage: Dia tuh Ngeyel banget.\
\n\n{cmd}s\
\nUsage: Haha sokap.\
\n\n{cmd}v\
\nUsage: Merendah.\
\n\n{cmd}a\
\nUsage: Nyari Sleep Call.\
\n\n{cmd}j\
\nUsage: Hujat yang gapunya muka.\
\n\n{cmd}g\
\nUsage: Kegantengan.\
\n\n{cmd}y\
\nUsage: teruntuk petarung.\
\n\n{cmd}h\
\nUsage: Kecantikan.\
\n\n{cmd}o\
\nUsage: Ngatain org norak.\
\n\n{cmd}1\
\nUsage: Ngatain Petarunx Tele."
})
