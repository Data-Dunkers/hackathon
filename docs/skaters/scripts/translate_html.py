import os
import glob
import re

src_dir = r"c:\Users\miste\Documents\GitHub\dd-hackathon\docs"
dst_dir = r"c:\Users\miste\Documents\GitHub\dd-hackathon\docs\skaters"

os.makedirs(dst_dir, exist_ok=True)

# Find all html files in src
html_files = glob.glob(os.path.join(src_dir, "*.html"))

replacements = {
    r"Data Dunkers": "Data Skaters",
    r"free throws": "saves",
    r"free throw": "save",
    r"basketball": "hockey",
    r"Raptors": "Jets",
    r"Toronto Jets": "Winnipeg Jets", # in case "Toronto Raptors" became "Toronto Jets" from earlier rule? No. Dictionary is not ordered.
    r"Toronto Raptors": "Winnipeg Jets",
    r"Indiana Pacers": "Winnipeg Jets",
    r"WNBA legends Diana Taurasi and DeWanna Bonner": "NHL stars Kyle Connor and Mark Scheifele",
    r"Points Per Game": "Points",
    r"Efficiency \(EFF\)": "Plus-Minus (+/-)",
    r"EFF": "+/-",
    r"True Shooting Percentage \(TS%\)": "Shooting Percentage (S%)",
    r"TS%": "S%",
    r"True Shooting %": "Shooting %",
    r"Points Volume": "Goals Volume",
    r"rebound": "assist",
    r"A center \(who mostly dunks\) and a guard \(who shoots 3s\)": "A defenseman (who takes long shots) and a forward (who gets tap-ins)",
    r"\(PTS \+ REB \+ AST \+ STL \+ BLK\) - \(Missed FG \+ Missed FT \+ TO\)": "(G + A) + +/- + PIM",
    r"takes 30 shots to do it": "takes 50 shots to do it",
    # Links inside the table and around the site
    r"basketball-metrics.html": "hockey-metrics.html",
    r"interpreting_pie_charts_pts.html": "interpreting_pie_charts_g.html",
    r"interpreting_pie_charts_siakam.html": "interpreting_pie_charts_scheifele.html",
    r"field_goal_percentage_vs_points.html": "shooting_percentage_vs_goals.html",
    r"standard_deviation_stl.html": "standard_deviation_pim.html",
    r"sunburst_shot_distribution.html": "sunburst_goal_distribution.html",
    r"treemap_shot_distribution.html": "treemap_goal_distribution.html",
    r"wnba_career_trends.html": "nhl_trends.html",
    r"Pascal Siakam": "Mark Scheifele",
    r"metrics_scatter.html": "metrics_scatter.html",
    # Specific translation for the shot charts renaming I did in python
    r"shot_chart.html": "goal_chart.html",
}

def translate_content(text):
    for k, v in replacements.items():
        # Use case-insensitive where safe, but these keys are somewhat specific. Some can be case insensitive.
        text = re.sub(k, v, text)
    # Special exact string replaces correctly handling casing
    text = text.replace("Basketball", "Hockey")
    text = text.replace("basketball", "hockey")
    text = text.replace("BASKETBALL", "HOCKEY")
    text = text.replace("Toronto Raptors", "Winnipeg Jets")
    text = text.replace("Indiana Pacers", "Winnipeg Jets")
    return text

for fp in html_files:
    fname = os.path.basename(fp)
    if fname == "basketball-metrics.html":
        fname = "hockey-metrics.html"
        
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
        
    content = translate_content(content)
        
    # Save
    out_fp = os.path.join(dst_dir, fname)
    with open(out_fp, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Translated {len(html_files)} files!")
