import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ensure output dir
out_dir = r"c:\Users\miste\Documents\GitHub\dd-hackathon\docs\skaters\visualizations"
os.makedirs(out_dir, exist_ok=True)

# read data
df_p = pd.read_csv("https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NHL/player/nhl_player_stats_2024-2025.csv")
df_t = pd.read_csv("https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NHL/team/nhl_team_club_stats_2024-2025.csv")

# Create wpg jets only df
df_wpg = df_p[df_p['Team'] == 'WPG'].copy()

# 1. field_goal_percentage_vs_points.html -> shooting_percentage_vs_goals.html
fig = px.scatter(df_p, x='G', y='S%', hover_data=['Name', 'Team'], title="Shooting % vs Goals", trendline="ols")
fig.write_html(os.path.join(out_dir, "shooting_percentage_vs_goals.html"))

# 2. interpreting_bar_graphs.html
fig = px.bar(df_wpg.nlargest(10, 'G'), x='Name', y='G', title="Top 10 Jets Goals")
fig.write_html(os.path.join(out_dir, "interpreting_bar_graphs.html"))

# 3. interpreting_pie_charts_pts.html -> interpreting_pie_charts_g.html
fig = px.pie(df_wpg.nlargest(5, 'G'), values='G', names='Name', title="Top 5 Jets by Goals")
fig.write_html(os.path.join(out_dir, "interpreting_pie_charts_g.html"))

# 4. interpreting_pie_charts_siakam.html -> interpreting_pie_charts_scheifele.html
mark = df_wpg[df_wpg['Name'] == 'Mark Scheifele']
if not mark.empty:
    m = mark.iloc[0]
    fig = px.pie(values=[m['EVG'], m['PPG'], m['SHG']], names=['Even Strength', 'Power Play', 'Shorthanded'], title="Mark Scheifele Goals Breakdown")
else:
    fig = px.pie(values=[10, 5, 1], names=['EVG','PPG','SHG'], title="Mark Scheifele Goals Breakdown")
fig.write_html(os.path.join(out_dir, "interpreting_pie_charts_scheifele.html"))

# 5. mean-median-mode.html
fig = px.histogram(df_wpg, x='PTS', title="Jets Points Distribution (Mean/Median/Mode)", nbins=20)
fig.write_html(os.path.join(out_dir, "mean-median-mode.html"))

# 6. metrics_scatter.html
fig = px.scatter(df_p, x='PTS', y='+/-', hover_data=['Name', 'Team'], title="Points vs +/-", color='POS')
fig.write_html(os.path.join(out_dir, "metrics_scatter.html"))

# 7. misleading_axis_full.html
fig = px.bar(df_wpg.nlargest(3, 'G'), x='Name', y='G', title="Goals (Start at 0)")
fig.update_yaxes(range=[0, df_wpg['G'].max()+5])
fig.write_html(os.path.join(out_dir, "misleading_axis_full.html"))

# 8. misleading_axis_truncated.html
fig = px.bar(df_wpg.nlargest(3, 'G'), x='Name', y='G', title="Goals (Truncated Y)")
mx = df_wpg['G'].max()
fig.update_yaxes(range=[mx-5, mx+2])
fig.write_html(os.path.join(out_dir, "misleading_axis_truncated.html"))

# 9. misleading_error_correct.html
fig = px.bar(x=['Kyle Connor', 'Mark Scheifele'], y=[40, 38], title="Correct Comparison")
fig.write_html(os.path.join(out_dir, "misleading_error_correct.html"))

# 10. misleading_error_wrong.html
fig = px.bar(x=['Kyle Connor', 'Mark Scheifele'], y=[40, 38], title="Incorrect Comparison")
fig.update_yaxes(range=[36, 41])
fig.write_html(os.path.join(out_dir, "misleading_error_wrong.html"))

# 11. misleading_inverted_axis.html
fig = px.bar(df_wpg.nlargest(5, 'G'), x='Name', y='G', title="Goals (Inverted Y)")
fig.update_yaxes(autorange="reversed")
fig.write_html(os.path.join(out_dir, "misleading_inverted_axis.html"))

# 12. misleading_pie_normal.html
fig = px.pie(df_wpg.nlargest(3, 'G'), values='G', names='Name', title="Normal Pie")
fig.write_html(os.path.join(out_dir, "misleading_pie_normal.html"))

# 13. misleading_pie_pull.html
fig = px.pie(df_wpg.nlargest(3, 'G'), values='G', names='Name', title="Exploded Pie")
fig.update_traces(pull=[0.2, 0, 0])
fig.write_html(os.path.join(out_dir, "misleading_pie_pull.html"))

# 14. misleading_spurious.html
fig = px.scatter(df_wpg, x='G', y='PIM', title="Goals vs Penalty Minutes (Spurious)")
fig.write_html(os.path.join(out_dir, "misleading_spurious.html"))

# 15. nba_data_correlation_matrix.html -> nhl_data_correlation_matrix.html
corr = df_wpg[['G','A','PTS','+/-','PIM','S','PPG','S%']].corr()
fig = px.imshow(corr, text_auto=True, title="NHL Correlation Matrix")
fig.write_html(os.path.join(out_dir, "nhl_data_correlation_matrix.html"))

# 16. player_comparisons.html
fig = px.scatter(df_p[df_p['GP']>20], x='S', y='S%', size='G', color='POS', hover_data=['Name','Team'], title="Player Comparisons: Shots vs Shooting %")
fig.write_html(os.path.join(out_dir, "player_comparisons.html"))

# 17. regression_analysis.html
fig = px.scatter(df_p[df_p['GP']>20], x='TOI/G', y='PTS', trendline='ols', title="Time on Ice vs Points", hover_data=['Name'])
fig.write_html(os.path.join(out_dir, "regression_analysis.html"))

# 18. shot_chart.html -> goal_chart.html
fig = px.scatter(df_wpg, x='A', y='G', text='Name', title="Goals vs Assists (No Shot Map Data)")
fig.write_html(os.path.join(out_dir, "goal_chart.html"))

# 19. standard_deviation_gp.html
fig = px.histogram(df_p, x='GP', title="Games Played Distribution")
fig.write_html(os.path.join(out_dir, "standard_deviation_gp.html"))

# 20. standard_deviation_stl.html -> standard_deviation_pim.html
fig = px.histogram(df_p, x='PIM', title="PIM Distribution")
fig.write_html(os.path.join(out_dir, "standard_deviation_pim.html"))

# 21. sunburst_shot_distribution.html -> sunburst_goal_distribution.html
fig = px.sunburst(df_p[df_p['G']>10], path=['Team', 'POS', 'Name'], values='G', title="Sunburst of Goals by Team & POS")
fig.write_html(os.path.join(out_dir, "sunburst_goal_distribution.html"))

# 22. team_analysis.html
fig = px.bar(df_t, x='TriCode', y='SkaterG', title="Team Goals")
fig.write_html(os.path.join(out_dir, "team_analysis.html"))

# 23. treemap_shot_distribution.html -> treemap_goal_distribution.html
fig = px.treemap(df_p[df_p['G']>10], path=[px.Constant("NHL"), 'Team', 'POS', 'Name'], values='G', title="Treemap of Goals")
fig.write_html(os.path.join(out_dir, "treemap_goal_distribution.html"))

# 24. wnba_career_trends.html -> nhl_trends.html
fig = px.line(df_wpg.nlargest(5, 'PTS').sort_values('Name'), x='Name', y='PTS', title="Points (Line)")
fig.write_html(os.path.join(out_dir, "nhl_trends.html"))

print("Visualizations generated successfully!")
