import tkinter as tk
from tkinter import ttk, messagebox
import math

# ===================== DATASET =====================
DATASET = [
    {"nom":"Albert Einstein","type_vivant":1,"type_humain":1,"scientifique":1,"historique":1},
    {"nom":"Marie Curie","type_vivant":1,"type_humain":1,"scientifique":1,"historique":1,"femme":1},
    {"nom":"Elon Musk","type_vivant":1,"type_humain":1,"vivant_actuellement":1},
    {"nom":"Nelson Mandela","type_vivant":1,"type_humain":1,"historique":1,"politique":1},
    {"nom":"J.K. Rowling","type_vivant":1,"type_humain":1,"artiste":1,"ecrivain":1,"femme":1,"vivant_actuellement":1},
    {"nom":"Michael Jackson","type_vivant":1,"type_humain":1,"historique":1,"artiste":1,"musique":1},
    {"nom":"Cristiano Ronaldo","type_vivant":1,"type_humain":1,"sportif":1,"vivant_actuellement":1},
    {"nom":"Napoleon Bonaparte","type_vivant":1,"type_humain":1,"historique":1,"politique":1,"militaire":1},
    {"nom":"Isaac Newton","type_vivant":1,"type_humain":1,"scientifique":1,"historique":1,"religieux":1},
    {"nom":"chat","type_vivant":1,"type_animal":1,"mammifere":1,"domestique":1,"nocturne":1,"terrestre":1},
    {"nom":"aigle","type_vivant":1,"type_animal":1,"oiseau":1,"vole":1,"terrestre":1},
    {"nom":"requin","type_vivant":1,"type_animal":1,"poisson":1,"aquatique":1,"marin":1},
    {"nom":"ordinateur portable","type_vivant":0,"type_objet":1,"electronique":1,"portable":1,"connecte":1,"energie":1,"outil":1},
    {"nom":"smartphone","type_vivant":0,"type_objet":1,"electronique":1,"portable":1,"connecte":1,"energie":1},
    {"nom":"avion","type_vivant":0,"type_objet":1,"transport":1,"vole":1,"energie":1},
    {"nom":"Wall-E","type_vivant":0,"type_objet":1,"electronique":1,"robot":1},
    {"nom":"Superman","type_vivant":1,"imaginaire":1,"extraterrestre":1},
    {"nom":"dragon","type_vivant":0,"imaginaire":1,"mythique":1,"vole":1},
    {"nom":"sabre laser","type_vivant":0,"imaginaire":1,"arme":1,"energie":1},
]

QUESTIONS = {
    "type_vivant":"Est-ce vivant ?","type_humain":"Est-ce un humain ?",
    "type_animal":"Est-ce un animal ?","type_objet":"Est-ce un objet ?",
    "scientifique":"Est-il scientifique ?","historique":"Est-ce un personnage historique ?",
    "artiste":"Est-il artiste ?","sportif":"Est-il sportif ?",
    "politique":"Est-il politique ?","militaire":"Est-il militaire ?",
    "religieux":"Est-il religieux ?","musique":"Est-il musicien ?",
    "ecrivain":"Est-il ecrivain ?","femme":"Est-ce une femme ?",
    "mammifere":"Est-ce un mammifere ?","oiseau":"Est-ce un oiseau ?",
    "poisson":"Est-ce un poisson ?","aquatique":"Vit-il dans l eau ?",
    "marin":"Est-il marin ?","terrestre":"Vit-il sur terre ?",
    "nocturne":"Est-il nocturne ?","vole":"Peut-il voler ?",
    "domestique":"Peut-il etre domestique ?","electronique":"Est-ce electronique ?",
    "connecte":"Peut-il se connecter a Internet ?","energie":"Utilise-t-il de l energie ?",
    "transport":"Sert-il au transport ?","outil":"Est-ce un outil ?",
    "arme":"Est-ce une arme ?","robot":"Est-ce un robot ?",
    "imaginaire":"Est-ce imaginaire ?","mythique":"Est-ce mythique ?",
    "extraterrestre":"Est-ce extraterrestre ?","vivant_actuellement":"Est-il vivant actuellement ?"
}

EMOJIS = {
    "type_vivant":"🌱","type_humain":"🧑","type_animal":"🐾","type_objet":"📦",
    "scientifique":"🔬","historique":"📜","artiste":"🎨","sportif":"⚽",
    "politique":"🏛","militaire":"🎖","religieux":"✝","musique":"🎵",
    "ecrivain":"✍","femme":"👩","mammifere":"🐶","oiseau":"🦅",
    "poisson":"🐟","aquatique":"🌊","marin":"🚢","terrestre":"🌍",
    "nocturne":"🌙","vole":"🕊","domestique":"🏠","electronique":"💻",
    "connecte":"🌐","energie":"⚡","transport":"🚗","outil":"🔧",
    "arme":"🔫","robot":"🤖","imaginaire":"📖","mythique":"🐉",
    "extraterrestre":"👽","vivant_actuellement":"💫"
}

# ===================== IA =====================
def entropie(p):
    if p in (0, 1): return 0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def gain_information(candidats, cle):
    total = len(candidats)
    if total <= 1: return 0
    oui = sum(1 for c in candidats if c.get(cle, 0) == 1)
    return entropie(oui / total)

def meilleure_question(candidats, posees):
    best, best_gain = None, -1
    for cle in QUESTIONS:
        if cle in posees: continue
        g = gain_information(candidats, cle)
        if g > best_gain:
            best, best_gain = cle, g
    return best

# ===================== COULEURS =====================
C = {
    # Fonds
    "bg":        "#07090F",
    "panel":     "#0C0F1A",
    "card":      "#101422",
    "card2":     "#141829",
    "input":     "#181D2E",
    # Accents
    "cyan":      "#00D4FF",
    "cyan_dim":  "#004E6A",
    "cyan_glow": "#00A8CC",
    "purple":    "#9D6FFF",
    "purple_dim":"#2E1870",
    "purple_glow":"#7B50CC",
    # Actions
    "green":     "#00F5A0",
    "green_dim": "#003D28",
    "green_glow":"#00C280",
    "red":       "#FF3D6E",
    "red_dim":   "#4A0820",
    "red_glow":  "#CC2255",
    "yellow":    "#FFD166",
    "amber":     "#FF9F1C",
    # Texte
    "white":     "#E8F4FF",
    "soft":      "#8BA8C8",
    "dim":       "#3A5068",
    "dim2":      "#1E3044",
    # Bordures
    "border":    "#1A2B40",
    "border2":   "#0D1A28",
    "sep":       "#0F1E30",
}

# ===================== ANIMATIONS =====================
class Anim:
    def __init__(self, root):
        self.root = root
        self._jobs = {}

    def cancel(self, key):
        if key in self._jobs:
            try: self.root.after_cancel(self._jobs[key])
            except: pass
            del self._jobs[key]

    def type_text(self, widget, text, speed=22):
        key = f"t{id(widget)}"
        self.cancel(key)
        self._t(widget, text, 0, key, speed)

    def _t(self, w, text, i, key, speed):
        if i <= len(text):
            w.config(text=text[:i] + ("▌" if i < len(text) else ""))
            self._jobs[key] = self.root.after(speed, self._t, w, text, i+1, key, speed)

    def smooth_bar(self, bar, target, ref, steps=22, delay=14):
        key = f"b{id(bar)}"
        self.cancel(key)
        self._bar(bar, target, ref[0], steps, steps, delay, key, ref)

    def _bar(self, bar, target, start, step, total, delay, key, ref):
        if total == 0:
            bar.place(relwidth=target)
            ref[0] = target
            return
        t = 1 - (step / total)
        ease = t * t * (3 - 2 * t)
        val = start + (target - start) * ease
        ref[0] = val
        bar.place(relwidth=max(0.0, min(1.0, val)))
        if step > 0:
            self._jobs[key] = self.root.after(delay, self._bar, bar, target, start, step-1, total, delay, key, ref)

    def blink_dot(self, widget, c1, c2, interval=600):
        key = f"blink{id(widget)}"
        self.cancel(key)
        self._blink(widget, c1, c2, True, interval, key)

    def _blink(self, w, c1, c2, state, interval, key):
        try:
            w.config(fg=c1 if state else c2)
            self._jobs[key] = self.root.after(interval, self._blink, w, c1, c2, not state, interval, key)
        except: pass

    def stop_blink(self, widget, final_color):
        key = f"blink{id(widget)}"
        self.cancel(key)
        try: widget.config(fg=final_color)
        except: pass

# ===================== APP =====================
class DevinetteIA:
    def __init__(self, root):
        self.root = root
        self.root.title("CSI  —  Moteur d'Inference Bayesien")
        self.root.geometry("1020x720")
        self.root.minsize(780, 580)
        self.root.resizable(True, True)
        self.root.configure(bg=C["bg"])

        self.anim = Anim(root)
        self.candidats = DATASET.copy()
        self.posees = set()
        self.q_actuelle = None
        self.q_count = 0
        self._prog_ref = [0.0]
        self._cand_ref = [1.0]
        self.hist_placeholder = None

        self._build()
        self.prochaine_question()

    # ── BUILD ────────────────────────────────────────────────────
    def _build(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self._header()
        self._body()
        self._footer()

    # ── HEADER ──────────────────────────────────────────────────
    def _header(self):
        # Ligne top cyan lumineuse
        top = tk.Canvas(self.root, height=3, bg=C["bg"], highlightthickness=0)
        top.grid(row=0, column=0, sticky="ew")
        top.create_rectangle(0, 0, 4000, 3, fill=C["cyan"], outline="")

        hdr = tk.Frame(self.root, bg=C["panel"])
        hdr.grid(row=0, column=0, sticky="ew", pady=(3, 0))
        hdr.columnconfigure(1, weight=1)

        # Icone hexagone
        icon_frame = tk.Frame(hdr, bg=C["cyan_dim"], padx=18, pady=18)
        icon_frame.grid(row=0, column=0, rowspan=2, sticky="ns")
        tk.Label(icon_frame, text="⬡", font=("Courier", 26, "bold"),
                 fg=C["cyan"], bg=C["cyan_dim"]).pack()

        # Textes titre
        txt_frame = tk.Frame(hdr, bg=C["panel"], padx=20, pady=14)
        txt_frame.grid(row=0, column=1, sticky="w")

        title_row = tk.Frame(txt_frame, bg=C["panel"])
        title_row.pack(anchor="w")
        tk.Label(title_row, text="CSI", font=("Courier", 20, "bold"),
                 fg=C["cyan"], bg=C["panel"]).pack(side="left")
        tk.Label(title_row, text="  DEVINETTE  IA",
                 font=("Courier", 20, "bold"),
                 fg=C["white"], bg=C["panel"]).pack(side="left")

        tk.Label(txt_frame,
                 text="MOTEUR  D'INFERENCE  BAYESIEN  ·  ENTROPIE  INFORMATIONNELLE",
                 font=("Courier", 7), fg=C["dim"], bg=C["panel"]).pack(anchor="w", pady=(2,0))

        # Stats droite
        stats = tk.Frame(hdr, bg=C["panel"], padx=28)
        stats.grid(row=0, column=2, rowspan=2, sticky="e")

        self.lbl_q = self._stat_badge(stats, "Q : 00", C["purple"])
        self.lbl_q.pack(anchor="e", pady=(12, 4))

        self.lbl_n = self._stat_badge(stats, f"{len(DATASET)} candidats", C["cyan"])
        self.lbl_n.pack(anchor="e", pady=(0, 12))

        # Séparateur
        tk.Frame(self.root, height=1, bg=C["border"]).grid(row=0, column=0, sticky="ew")

    # ── BODY ────────────────────────────────────────────────────
    def _body(self):
        body = tk.Frame(self.root, bg=C["bg"])
        body.grid(row=1, column=0, sticky="nsew", padx=24, pady=20)
        body.columnconfigure(0, weight=6)
        body.columnconfigure(1, weight=3)
        body.rowconfigure(0, weight=1)
        self._left(body)
        self._right(body)

    # ── COLONNE GAUCHE ──────────────────────────────────────────
    def _left(self, parent):
        col = tk.Frame(parent, bg=C["bg"])
        col.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        col.columnconfigure(0, weight=1)
        col.rowconfigure(0, weight=1)

        # ── Carte question ──────────────────────────────────────
        # Bordure lumineuse cyan (1px de chaque côté)
        outer = tk.Frame(col, bg=C["cyan"], padx=1, pady=1)
        outer.grid(row=0, column=0, sticky="nsew")

        card = tk.Frame(outer, bg=C["card"])
        card.pack(fill="both", expand=True)
        card.columnconfigure(0, weight=1)
        card.rowconfigure(2, weight=1)

        # Bande couleur haut
        top_band = tk.Frame(card, bg=C["cyan"], height=2)
        top_band.grid(row=0, column=0, sticky="ew")

        # Zone info (tag + entropie)
        info_row = tk.Frame(card, bg=C["card2"], pady=8, padx=20)
        info_row.grid(row=1, column=0, sticky="ew")

        left_info = tk.Frame(info_row, bg=C["card2"])
        left_info.pack(side="left")

        self.dot_status = tk.Label(left_info, text="●",
                                    font=("Courier", 9),
                                    fg=C["cyan"], bg=C["card2"])
        self.dot_status.pack(side="left", padx=(0, 6))
        self.anim.blink_dot(self.dot_status, C["cyan"], C["cyan_dim"])

        self.tag_lbl = tk.Label(left_info, text="SYSTEME PRET",
                                 font=("Courier", 8, "bold"),
                                 fg=C["cyan"], bg=C["card2"])
        self.tag_lbl.pack(side="left")

        self.ent_lbl = tk.Label(info_row, text="",
                                 font=("Courier", 8),
                                 fg=C["dim"], bg=C["card2"])
        self.ent_lbl.pack(side="right", padx=(0, 4))

        # Zone centrale : emoji + question
        center = tk.Frame(card, bg=C["card"], padx=30, pady=20)
        center.grid(row=2, column=0, sticky="nsew")
        center.columnconfigure(0, weight=1)

        self.emoji_lbl = tk.Label(center, text="🤖",
                                   font=("Segoe UI Emoji", 52),
                                   bg=C["card"])
        self.emoji_lbl.pack(pady=(10, 14))

        self.q_lbl = tk.Label(center,
                               text="Pense a quelque chose...",
                               font=("Courier", 18, "bold"),
                               fg=C["white"], bg=C["card"],
                               wraplength=500, justify="center")
        self.q_lbl.pack(pady=(0, 6))

        self.sub_lbl = tk.Label(center, text="",
                                 font=("Courier", 9),
                                 fg=C["dim"], bg=C["card"])
        self.sub_lbl.pack(pady=(0, 18))

        # Barre de progression dans la carte
        prog_area = tk.Frame(card, bg=C["card"], padx=20, pady=10)
        prog_area.grid(row=3, column=0, sticky="ew")

        prog_hdr = tk.Frame(prog_area, bg=C["card"])
        prog_hdr.pack(fill="x", pady=(0, 5))
        tk.Label(prog_hdr, text="PROGRESSION", font=("Courier", 7),
                 fg=C["dim"], bg=C["card"]).pack(side="left")
        self.prog_pct = tk.Label(prog_hdr, text="0%",
                                  font=("Courier", 7, "bold"),
                                  fg=C["purple"], bg=C["card"])
        self.prog_pct.pack(side="right")

        track = tk.Frame(prog_area, bg=C["border2"], height=6)
        track.pack(fill="x")
        self.prog_bar = tk.Frame(track, bg=C["cyan"], height=6)
        self.prog_bar.place(x=0, y=0, relheight=1, relwidth=0)

        # ── Boutons OUI / NON ───────────────────────────────────
        btn_row = tk.Frame(col, bg=C["bg"])
        btn_row.grid(row=1, column=0, sticky="ew", pady=(12, 0))
        btn_row.columnconfigure(0, weight=1)
        btn_row.columnconfigure(1, weight=1)

        self.btn_oui = self._glow_btn(btn_row, "✓   OUI",
                                       C["green"], C["green_dim"], C["green_glow"],
                                       lambda: self.repondre(1))
        self.btn_oui.grid(row=0, column=0, sticky="ew", padx=(0, 8), ipady=18)

        self.btn_non = self._glow_btn(btn_row, "✗   NON",
                                       C["red"], C["red_dim"], C["red_glow"],
                                       lambda: self.repondre(0))
        self.btn_non.grid(row=0, column=1, sticky="ew", padx=(8, 0), ipady=18)

        # ── Bouton reset ────────────────────────────────────────
        reset_wrap = tk.Frame(col, bg=C["dim2"],
                               highlightthickness=1,
                               highlightbackground=C["border"])
        reset_wrap.grid(row=2, column=0, sticky="ew", pady=(8, 0))
        self.btn_reset = tk.Button(
            reset_wrap, text="↺   NOUVELLE PARTIE",
            font=("Courier", 11),
            fg=C["soft"], bg=C["card2"],
            activeforeground=C["cyan"],
            activebackground=C["card"],
            relief="flat", bd=0, cursor="hand2",
            command=self.recommencer, pady=12)
        self.btn_reset.pack(fill="x")
        self.btn_reset.bind("<Enter>", lambda e: self.btn_reset.config(fg=C["cyan"], bg=C["card"]))
        self.btn_reset.bind("<Leave>", lambda e: self.btn_reset.config(fg=C["soft"], bg=C["card2"]))

    # ── COLONNE DROITE ──────────────────────────────────────────
    def _right(self, parent):
        col = tk.Frame(parent, bg=C["bg"])
        col.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        col.columnconfigure(0, weight=1)
        col.rowconfigure(1, weight=1)

        # ── Carte candidats ─────────────────────────────────────
        cand_outer = tk.Frame(col, bg=C["purple"], padx=1, pady=1)
        cand_outer.grid(row=0, column=0, sticky="ew")

        cand_card = tk.Frame(cand_outer, bg=C["card"], padx=18, pady=16)
        cand_card.pack(fill="both")

        # Header candidats
        c_hdr = tk.Frame(cand_card, bg=C["card"])
        c_hdr.pack(fill="x", pady=(0, 10))
        tk.Label(c_hdr, text="CANDIDATS EN MEMOIRE",
                 font=("Courier", 7, "bold"),
                 fg=C["soft"], bg=C["card"]).pack(side="left")

        # Nombre + label
        num_row = tk.Frame(cand_card, bg=C["card"])
        num_row.pack(fill="x", pady=(0, 4))

        self.badge_num = tk.Label(num_row, text=str(len(DATASET)),
                                   font=("Courier", 44, "bold"),
                                   fg=C["purple"], bg=C["card"])
        self.badge_num.pack(side="left")

        tk.Label(num_row, text=" restants",
                 font=("Courier", 10),
                 fg=C["dim"], bg=C["card"],
                 anchor="s").pack(side="left", pady=(28, 0))

        # Mini barre candidats
        c_track = tk.Frame(cand_card, bg=C["border2"], height=4)
        c_track.pack(fill="x", pady=(0, 12))
        self.cand_bar = tk.Frame(c_track, bg=C["purple"], height=4)
        self.cand_bar.place(x=0, y=0, relheight=1, relwidth=1.0)

        # Combobox
        style = ttk.Style()
        style.theme_use("default")
        style.configure("CSI.TCombobox",
            fieldbackground=C["input"],
            background=C["input"],
            foreground=C["white"],
            bordercolor=C["border"],
            arrowcolor=C["purple"],
            selectbackground=C["input"],
            selectforeground=C["purple"],
            padding=6)
        style.map("CSI.TCombobox",
            fieldbackground=[("readonly", C["input"])],
            foreground=[("readonly", C["white"])],
            background=[("readonly", C["input"])],
            bordercolor=[("focus", C["purple"])])

        self.combo_var = tk.StringVar()
        self.combo = ttk.Combobox(cand_card,
                                   textvariable=self.combo_var,
                                   state="readonly",
                                   style="CSI.TCombobox",
                                   font=("Courier", 10),
                                   height=20)
        self.combo.pack(fill="x", ipady=5)

        # ── Carte historique ─────────────────────────────────────
        hist_outer = tk.Frame(col, bg=C["border"], padx=1, pady=1)
        hist_outer.grid(row=1, column=0, sticky="nsew", pady=(12, 0))

        hist_card = tk.Frame(hist_outer, bg=C["card"])
        hist_card.pack(fill="both", expand=True)
        hist_card.columnconfigure(0, weight=1)
        hist_card.rowconfigure(1, weight=1)

        # Header historique
        h_hdr = tk.Frame(hist_card, bg=C["card2"], padx=14, pady=8)
        h_hdr.grid(row=0, column=0, sticky="ew")
        tk.Label(h_hdr, text="HISTORIQUE DES QUESTIONS",
                 font=("Courier", 7, "bold"),
                 fg=C["soft"], bg=C["card2"]).pack(side="left")

        # Canvas scrollable
        scroll_area = tk.Frame(hist_card, bg=C["card"])
        scroll_area.grid(row=1, column=0, sticky="nsew")
        scroll_area.columnconfigure(0, weight=1)
        scroll_area.rowconfigure(0, weight=1)

        self.hist_cv = tk.Canvas(scroll_area, bg=C["card"],
                                  highlightthickness=0, bd=0)
        sb = ttk.Scrollbar(scroll_area, orient="vertical",
                            command=self.hist_cv.yview)
        self.hist_inner = tk.Frame(self.hist_cv, bg=C["card"])
        self.hist_inner.bind("<Configure>", lambda e: self.hist_cv.configure(
            scrollregion=self.hist_cv.bbox("all")))
        win = self.hist_cv.create_window((0, 0), window=self.hist_inner, anchor="nw")
        self.hist_cv.bind("<Configure>", lambda e: self.hist_cv.itemconfig(win, width=e.width))
        self.hist_cv.configure(yscrollcommand=sb.set)
        self.hist_cv.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")

        self.hist_ph = tk.Label(self.hist_inner,
                                 text="Aucune question posee",
                                 font=("Courier", 8),
                                 fg=C["dim"], bg=C["card"])
        self.hist_ph.pack(pady=20)

    # ── FOOTER ──────────────────────────────────────────────────
    def _footer(self):
        tk.Frame(self.root, height=1, bg=C["border"]).grid(row=2, column=0, sticky="ew")
        footer = tk.Frame(self.root, bg=C["panel"], pady=10)
        footer.grid(row=2, column=0, sticky="ew")
        footer.columnconfigure(1, weight=1)

        self.foot_dot = tk.Label(footer, text="●",
                                  font=("Courier", 9),
                                  fg=C["green"], bg=C["panel"])
        self.foot_dot.grid(row=0, column=0, padx=(22, 6))

        self.foot_lbl = tk.Label(footer, text="SYSTEME PRET",
                                  font=("Courier", 8),
                                  fg=C["soft"], bg=C["panel"])
        self.foot_lbl.grid(row=0, column=1, sticky="w")

        tk.Label(footer,
                 text="CSI  v5.0  ·  ENTROPIE BAYESIENNE",
                 font=("Courier", 7),
                 fg=C["dim"], bg=C["panel"]).grid(row=0, column=2, padx=22)

    # ── HELPERS ─────────────────────────────────────────────────
    def _stat_badge(self, parent, text, color):
        f = tk.Frame(parent, bg=C["card2"],
                     highlightthickness=1,
                     highlightbackground=color)
        tk.Label(f, text=text,
                 font=("Courier", 9, "bold"),
                 fg=color, bg=C["card2"],
                 padx=12, pady=5).pack()
        return f

    def _glow_btn(self, parent, text, fg, bg_dim, bg_hover, cmd):
        btn = tk.Button(
            parent, text=text,
            font=("Courier", 13, "bold"),
            fg=fg, bg=C["card"],
            activeforeground=C["bg"],
            activebackground=fg,
            relief="flat", bd=0,
            cursor="hand2", command=cmd,
            highlightthickness=1,
            highlightbackground=fg,
            highlightcolor=fg)
        btn.bind("<Enter>", lambda e: btn.config(bg=bg_dim))
        btn.bind("<Leave>", lambda e: btn.config(bg=C["card"]))
        return btn

    # ── LOGIQUE ─────────────────────────────────────────────────
    def _update_combo(self):
        names = sorted([c["nom"] for c in self.candidats], key=str.lower)
        self.combo["values"] = names
        n = len(names)
        self.combo_var.set(f"  Voir les {n} candidats  ▾")
        self.badge_num.config(
            text=str(n),
            fg=C["green"] if n <= 2 else C["yellow"] if n <= 6 else C["purple"])
        self.lbl_n.winfo_children()[0].config(text=f"{n} candidats")
        ratio = n / len(DATASET)
        self.anim.smooth_bar(self.cand_bar, ratio, self._cand_ref)

    def _update_progress(self):
        asked = len(self.posees)
        total = len(QUESTIONS)
        ratio = asked / total
        pct = int(ratio * 100)
        self.anim.smooth_bar(self.prog_bar, ratio, self._prog_ref)
        self.prog_pct.config(text=f"{pct}%")

    def _add_hist(self, qkey, rep):
        if self.hist_ph:
            self.hist_ph.destroy()
            self.hist_ph = None

        n = len(self.hist_inner.winfo_children())
        bg = C["card2"] if n % 2 == 0 else C["card"]
        emoji = EMOJIS.get(qkey, "?")
        qtxt = QUESTIONS.get(qkey, qkey)
        is_oui = rep == 1
        dot_col = C["green"] if is_oui else C["red"]
        rep_txt = "OUI" if is_oui else "NON"

        row = tk.Frame(self.hist_inner, bg=bg, pady=6)
        row.pack(fill="x")
        row.columnconfigure(1, weight=1)

        tk.Label(row, text="●", font=("Courier", 7),
                 fg=dot_col, bg=bg, padx=8).grid(row=0, column=0)

        tk.Label(row, text=f"{emoji}  {qtxt}",
                 font=("Courier", 8),
                 fg=C["soft"], bg=bg,
                 anchor="w", wraplength=185,
                 justify="left").grid(row=0, column=1, sticky="w")

        r_lbl = tk.Label(row, text=rep_txt,
                          font=("Courier", 8, "bold"),
                          fg=dot_col, bg=bg, padx=10)
        r_lbl.grid(row=0, column=2, sticky="e")

        self.hist_cv.update_idletasks()
        self.hist_cv.yview_moveto(1.0)

    def prochaine_question(self):
        self._update_combo()
        self._update_progress()

        if len(self.candidats) == 1:
            nom = self.candidats[0]["nom"]
            self.emoji_lbl.config(text="🎯")
            self.anim.type_text(self.q_lbl, f"Tu pensais a  :  {nom}", speed=35)
            self.q_lbl.config(fg=C["green"])
            self.sub_lbl.config(text=f"Trouve en {self.q_count} questions !", fg=C["green"])
            self.tag_lbl.config(text="TROUVE !", fg=C["green"])
            self.anim.stop_blink(self.dot_status, C["green"])
            self.foot_dot.config(fg=C["green"])
            self.foot_lbl.config(text="TROUVE !")
            self.btn_oui.config(state="disabled", fg=C["dim"], highlightbackground=C["border"])
            self.btn_non.config(state="disabled", fg=C["dim"], highlightbackground=C["border"])
            self.anim.smooth_bar(self.prog_bar, 1.0, self._prog_ref)
            self.prog_pct.config(text="100%")
            self.root.after(600, lambda: messagebox.showinfo(
                "Resultat !",
                f"L'IA a trouve en {self.q_count} questions !\n\n>> {nom} <<",
                parent=self.root))
            return

        if len(self.candidats) == 0:
            self.q_lbl.config(text="Element inconnu...", fg=C["red"])
            self.tag_lbl.config(text="INCONNU", fg=C["red"])
            self.anim.stop_blink(self.dot_status, C["red"])
            return

        q = meilleure_question(self.candidats, self.posees)
        if not q:
            messagebox.showinfo("Resultat", f"Je dirais : {self.candidats[0]['nom']}")
            return

        self.posees.add(q)
        self.q_actuelle = q
        self.q_count += 1
        self.lbl_q.winfo_children()[0].config(text=f"Q : {self.q_count:02d}")

        total = len(self.candidats)
        oui = sum(1 for c in self.candidats if c.get(q, 0) == 1)
        h = entropie(oui / total) if total > 0 else 0

        self.emoji_lbl.config(text=EMOJIS.get(q, "?"))
        self.q_lbl.config(fg=C["white"])
        self.sub_lbl.config(text="", fg=C["dim"])
        self.tag_lbl.config(text="ANALYSE EN COURS", fg=C["cyan"])
        self.ent_lbl.config(text=f"H={h:.2f}  ·  {oui}/{total}")
        self.anim.blink_dot(self.dot_status, C["cyan"], C["cyan_dim"])
        self.foot_dot.config(fg=C["yellow"])
        self.foot_lbl.config(text="EN ATTENTE DE REPONSE")

        self.anim.type_text(self.q_lbl, QUESTIONS[q], speed=22)

    def repondre(self, val):
        if not self.q_actuelle: return
        self._add_hist(self.q_actuelle, val)
        self.candidats = [c for c in self.candidats
                          if c.get(self.q_actuelle, 0) == val]
        if not self.candidats:
            messagebox.showwarning("Inconnu", "Je ne connais pas cet element !", parent=self.root)
            self.recommencer()
            return
        self.prochaine_question()

    def recommencer(self):
        self.candidats = DATASET.copy()
        self.posees = set()
        self.q_actuelle = None
        self.q_count = 0
        self._prog_ref = [0.0]
        self._cand_ref = [1.0]

        self.lbl_q.winfo_children()[0].config(text="Q : 00")
        self.q_lbl.config(text="Pense a quelque chose...", fg=C["white"])
        self.sub_lbl.config(text="", fg=C["dim"])
        self.emoji_lbl.config(text="🤖")
        self.tag_lbl.config(text="SYSTEME PRET", fg=C["cyan"])
        self.ent_lbl.config(text="")
        self.prog_bar.place(relwidth=0)
        self.prog_pct.config(text="0%")
        self.cand_bar.place(relwidth=1.0)
        self.foot_dot.config(fg=C["green"])
        self.foot_lbl.config(text="SYSTEME PRET")
        self.btn_oui.config(state="normal", fg=C["green"],
                             highlightbackground=C["green"])
        self.btn_non.config(state="normal", fg=C["red"],
                             highlightbackground=C["red"])
        self.anim.blink_dot(self.dot_status, C["cyan"], C["cyan_dim"])

        for w in self.hist_inner.winfo_children():
            w.destroy()
        self.hist_ph = tk.Label(self.hist_inner,
                                 text="Aucune question posee",
                                 font=("Courier", 8),
                                 fg=C["dim"], bg=C["card"])
        self.hist_ph.pack(pady=20)

        self._update_combo()
        self.prochaine_question()

if __name__ == "__main__":
    root = tk.Tk()
    DevinetteIA(root)
    root.mainloop()