from chess_init import chess_initt, speed_games, pd, sns, plt, np

# opcao = str(input("Atualizar?"))
# if opcao=='1':
#     chess_initt()
# else:
#     print("nao atualizou")

# sns.set_style("whitegrid")
# plt.figure(figsize=(13, 7))

# sns.lineplot(y='my_elo', 
#              x=speed_games.index,
#              data=speed_games, 
#              color='darkslategray')

# sns.lineplot(y='my_elo_ma', 
#              x=speed_games.index,
#              data=speed_games, 
#              color='red')

# plt.xlabel('Number of Games', fontsize=13)
# plt.ylabel('My Elo', fontsize=13)
# plt.title('My Elo Over Time', fontsize=15)
# plt.xlim(-20)

# plt.legend(['elo', '30-day MA'])
# plt.savefig('elo_graph.png')

# plt.show()

country_average = speed_games.groupby(speed_games['opponent_country']).mean()
country_count = speed_games.groupby(speed_games['opponent_country']).count()
country_stats = pd.DataFrame(country_average['result']).join(pd.DataFrame(country_count['my_elo']), how='inner')
sns.set_style("whitegrid")
plt.figure(figsize=(13, 7))

sns.barplot(y='result',
            x=country_stats[country_stats.my_elo > 3].index,
            data=country_stats[country_stats.my_elo > 3],
            order=country_stats[country_stats.my_elo > 3].sort_values('result', ascending=False).index,
            palette="coolwarm"
           )

plt.xticks(rotation=90)
plt.ylim(.1,1)

plt.xlabel('Country (n > 3)', fontsize=13)
plt.ylabel('Win Percentage', fontsize=13)
plt.title('Win Percentage by Country', fontsize=15)

plt.savefig('country_win_percent.png')

plt.show()