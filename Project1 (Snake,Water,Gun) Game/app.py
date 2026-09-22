import random
import streamlit as st


st.set_page_config(
    page_title="Wild Draw | Snake Water Gun",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CHOICES = {
    "Snake": {"emoji": "🐍", "key": 1, "color": "#b8f05a", "tag": "strikes water"},
    "Water": {"emoji": "🌊", "key": -1, "color": "#66d9ff", "tag": "douses gun"},
    "Gun": {"emoji": "🔫", "key": 0, "color": "#ff8a65", "tag": "beats snake"},
}


def winner(player, computer):
    if player == computer:
        return "tie"
    if (player, computer) in ((1, -1), (0, 1), (-1, 0)):
        return "win"
    return "lose"


def reset_game():
    st.session_state.score = {"win": 0, "lose": 0, "tie": 0}
    st.session_state.history = []
    st.session_state.last_round = None


if "score" not in st.session_state:
    reset_game()


def play_round(choice_name):
    player = CHOICES[choice_name]["key"]
    computer_name = random.choice(list(CHOICES))
    computer = CHOICES[computer_name]["key"]
    result = winner(player, computer)
    st.session_state.score[result] += 1
    st.session_state.history.insert(0, (choice_name, computer_name, result))
    st.session_state.history = st.session_state.history[:6]
    st.session_state.last_round = (choice_name, computer_name, result)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    :root { --ink:#f7f7f2; --muted:#9b9d9b; --line:rgba(255,255,255,.12); --panel:rgba(22,26,27,.72); }
    * { font-family:'Space Grotesk', sans-serif; }
    .stApp { color:var(--ink); background: radial-gradient(circle at 50% -10%, rgba(190,255,82,.16), transparent 28%), radial-gradient(circle at 8% 28%, rgba(0,216,255,.13), transparent 25%), #080b10; }
    .stApp:before { content:""; position:fixed; inset:0; pointer-events:none; opacity:.14; background-image:linear-gradient(rgba(142,255,69,.18) 1px, transparent 1px),linear-gradient(90deg,rgba(142,255,69,.18) 1px,transparent 1px); background-size:42px 42px; mask-image:linear-gradient(to bottom,black,transparent 70%); }
    .block-container { max-width:1240px; padding:28px 4% 60px; }
    [data-testid="stHeader"] { background:transparent; }
    .brand { display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid var(--line); padding-bottom:18px; margin-bottom:42px; }
    .brand-mark { color:#b8f05a; font:500 12px 'DM Mono', monospace; letter-spacing:.12em; text-transform:uppercase; text-shadow:0 0 16px rgba(184,240,90,.7); }
    .status { color:#a8aaa8; font-size:12px; letter-spacing:.08em; text-transform:uppercase; }
    .status b { color:#b8f05a; font-weight:500; }
    .hero-kicker { color:#b8f05a; font:500 12px 'DM Mono', monospace; letter-spacing:.14em; text-transform:uppercase; margin-bottom:14px; }
    h1 { font-size:clamp(42px, 5.5vw, 76px) !important; line-height:.94 !important; letter-spacing:-.055em !important; margin:0 !important; max-width:760px; text-shadow:0 0 34px rgba(184,240,90,.16); }
    .hero-copy { color:#a9acab; font-size:16px; margin:18px 0 30px; max-width:510px; }
    .scoreboard { display:flex; gap:10px; margin:0 0 35px; }
    .score { background:linear-gradient(145deg,rgba(34,45,45,.9),rgba(12,18,24,.9)); border:1px solid var(--line); padding:13px 20px; min-width:100px; box-shadow:inset 0 0 20px rgba(106,240,90,.04); }
    .score-value { font-size:27px; font-weight:600; line-height:1; }
    .score-label { color:#8c908d; font:11px 'DM Mono', monospace; margin-top:8px; text-transform:uppercase; }
    .choice-title { color:#f7f7f2; font-size:20px; font-weight:600; margin:0 0 6px; }
    .choice-subtitle { color:#7e8583; font:11px 'DM Mono',monospace; letter-spacing:.08em; text-transform:uppercase; margin:0 0 14px; }
    div.stButton > button { height:154px; width:100%; color:#f7f7f2; background:linear-gradient(145deg,rgba(23,31,39,.98),rgba(10,15,22,.98)); border:1px solid rgba(255,255,255,.14); border-radius:5px; box-shadow:0 12px 26px rgba(0,0,0,.25), inset 0 0 30px rgba(80,220,255,.035); transition:transform .25s ease, border-color .25s ease, box-shadow .25s ease; }
    div.stButton > button:hover { transform:translateY(-8px) scale(1.015); border-color:#b8f05a; box-shadow:0 0 30px rgba(184,240,90,.18),0 16px 30px rgba(0,0,0,.34); color:#fff; }
    div.stButton > button:active { transform:translateY(-2px) scale(.99); }
    div.stButton > button p { font-size:54px; text-shadow:0 0 18px rgba(255,255,255,.28); }
    .battle { position:relative; overflow:hidden; border:1px solid rgba(184,240,90,.35); background:linear-gradient(120deg,rgba(25,38,33,.96),rgba(9,17,25,.96)); padding:24px 30px 27px; margin:35px 0 25px; animation:rise .45s ease both; box-shadow:0 0 45px rgba(184,240,90,.08); }
    .battle:after { content:""; position:absolute; left:0; right:0; top:-100%; height:100%; background:linear-gradient(transparent,rgba(184,240,90,.12),transparent); animation:scan 2.6s linear infinite; pointer-events:none; }
    .battle-label { color:#888d8b; font:11px 'DM Mono', monospace; letter-spacing:.12em; text-transform:uppercase; }
    .battle-row { display:flex; justify-content:center; align-items:center; gap:clamp(22px,8vw,100px); margin-top:20px; }
    .fighter { min-width:140px; display:flex; flex-direction:column; align-items:center; gap:8px; font-size:17px; font-weight:600; text-transform:uppercase; letter-spacing:.04em; }
    .fighter span { display:grid; place-items:center; width:88px; height:88px; border-radius:50%; font-size:47px; background:radial-gradient(circle at 35% 28%,rgba(255,255,255,.22),rgba(40,55,58,.25) 42%,rgba(5,9,14,.95) 70%); border:1px solid rgba(184,240,90,.55); box-shadow:0 0 28px rgba(184,240,90,.22),inset 0 0 18px rgba(255,255,255,.08); animation:avatarpop .65s ease both; }
    .versus { color:#b8f05a; font:700 15px 'DM Mono', monospace; text-shadow:0 0 13px rgba(184,240,90,.8); }
    .result { color:#b8f05a; font-size:34px; letter-spacing:.05em; font-weight:700; text-align:center; margin-top:24px; text-shadow:0 0 22px rgba(184,240,90,.55); animation:winpulse 1.8s ease-in-out infinite; }
    .result.lose { color:#ff8a65; text-shadow:0 0 18px rgba(255,138,101,.42); animation:shake .42s ease both; } .result.tie { color:#66d9ff; text-shadow:0 0 18px rgba(102,217,255,.42); animation:rise .65s ease both; }
    .history-title { color:#888d8b; font:11px 'DM Mono', monospace; letter-spacing:.12em; text-transform:uppercase; margin:42px 0 13px; }
    .history-item { display:flex; justify-content:space-between; border-top:1px solid var(--line); padding:13px 0; color:#b9bdba; font-size:13px; }
    .history-result { font:11px 'DM Mono', monospace; color:#b8f05a; text-transform:uppercase; }.history-result.lose{color:#ff8a65}.history-result.tie{color:#66d9ff}
    .tip { color:#717673; font-size:12px; margin-top:18px; }
    .round-status { display:flex; align-items:center; justify-content:center; gap:8px; color:#7e8583; font:11px 'DM Mono',monospace; letter-spacing:.1em; text-transform:uppercase; margin:0 0 14px; }
    .round-status b { color:#b8f05a; }
    @keyframes rise { from { opacity:0; transform:translateY(16px) scale(.98); } to { opacity:1; transform:translateY(0) scale(1); } }
    @keyframes scan { to { top:120%; } }
    @keyframes winpulse { 0%,100% { transform:scale(1); } 50% { transform:scale(1.025); } }
    @keyframes avatarpop { from { opacity:0; transform:scale(.4) rotate(-8deg); } to { opacity:1; transform:scale(1) rotate(0); } }
    @keyframes shake { 0%,100% { transform:translateX(0); } 25% { transform:translateX(-6px); } 75% { transform:translateX(6px); } }
    @media (max-width:650px) { .brand { margin-bottom:38px; } .status { display:none; } .score { min-width:0; flex:1; padding:12px; } .score-value{font-size:23px} .battle-row{gap:10px}.fighter{font-size:15px}.fighter span{font-size:27px} }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="brand"><div class="brand-mark">WILD DRAW / 001</div><div class="status">Arena status &nbsp; <b>● LIVE</b></div></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-kicker">A quick game of instinct</div>', unsafe_allow_html=True)
st.title("Snake. Water. Gun.")
st.markdown('<div class="hero-copy">Read the matchup. Make your move. Outsmart the machine before it reads you.</div>', unsafe_allow_html=True)

score = st.session_state.score
st.markdown(
    f'<div class="scoreboard"><div class="score"><div class="score-value">{score["win"]}</div><div class="score-label">Wins</div></div><div class="score"><div class="score-value">{score["lose"]}</div><div class="score-label">Losses</div></div><div class="score"><div class="score-value">{score["tie"]}</div><div class="score-label">Draws</div></div></div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="choice-title">Choose your fighter</div><div class="choice-subtitle">Your move decides the arena</div>', unsafe_allow_html=True)
columns = st.columns(3, gap="medium")
for column, name in zip(columns, CHOICES):
    with column:
        data = CHOICES[name]
        if st.button(f'{data["emoji"]}\n{name}', key=name, use_container_width=True):
            play_round(name)
            st.rerun()

if st.session_state.last_round:
    player_name, computer_name, result = st.session_state.last_round
    result_text = {"win": "You take the round", "lose": "The machine takes it", "tie": "Perfectly matched"}[result]
    if result == "win":
        st.balloons()
    headline = {"win": "YOU WON", "lose": "COMPUTER WON", "tie": "DRAW ROUND"}[result]
    st.markdown(
        f'<div class="battle"><div class="round-status"><b>ROUND {len(st.session_state.history):02d}</b> &nbsp; / &nbsp; COMBAT REVEAL</div><div class="battle-row"><div class="fighter"><span>{CHOICES[player_name]["emoji"]}</span>{player_name}</div><div class="versus">VS</div><div class="fighter"><span>{CHOICES[computer_name]["emoji"]}</span>{computer_name}</div></div><div class="result {result}">{headline}</div><div style="color:#9b9d9b;font-size:13px;text-align:center;margin-top:5px">{result_text}</div></div>',
        unsafe_allow_html=True,
    )

if st.session_state.history:
    st.markdown('<div class="history-title">Recent rounds</div>', unsafe_allow_html=True)
    for player_name, computer_name, result in st.session_state.history:
        st.markdown(f'<div class="history-item"><span>{CHOICES[player_name]["emoji"]} {player_name} <span style="color:#5e6661">vs</span> {CHOICES[computer_name]["emoji"]} {computer_name}</span><span class="history-result {result}">{result}</span></div>', unsafe_allow_html=True)

left, right = st.columns([1, 1])
with left:
    st.markdown('<div class="tip">Snake beats Water · Water beats Gun · Gun beats Snake</div>', unsafe_allow_html=True)
with right:
    if st.button("Reset arena", use_container_width=True):
        reset_game()
        st.rerun()