import csv

# Import data manipulation modules
import pandas as pd
import numpy as np

# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt

data = pd.read_csv('nfc_s_qb_total_2021.csv')

# Select stat categories
categories = ['Cmp', 'Att', 'Yds', 'Cmp%', 'TD', 'Int', 'Rate']

# Create data subset for radar chart
data_radar = data[['Player', 'Tm'] + categories]

# Remove ornamental characters for achievements
data_radar['Player'] = data_radar['Player'].str.replace('*', '')
data_radar['Player'] = data_radar['Player'].str.replace('+', '')

# Create columns with percentile rank
for i in categories:
    data_radar[i + '_Rank'] = data_radar[i].rank(pct=True)

# Flip the rank for interceptions
data_radar['Int_Rank'] = 1 - data_radar['Int_Rank']

# General plot parameters
mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['font.size'] = 16
mpl.rcParams['axes.linewidth'] = 0
mpl.rcParams['xtick.major.pad'] = 15

team_colors = {'ARI':'#97233f', 'ATL':'#a71930', 'BAL':'#241773', 'BUF':'#00338d', 'CAR':'#0085ca', 'CHI':'#0b162a', 'CIN':'#fb4f14', 'CLE':'#311d00', 'DAL':'#041e42', 'DEN':'#002244', 'DET':'#0076b6', 'GNB':'#203731', 'HOU':'#03202f', 'IND':'#002c5f', 'JAX':'#006778', 'KAN':'#e31837', 'LAC':'#002a5e', 'LAR':'#003594', 'MIA':'#008e97', 'MIN':'#4f2683', 'NWE':'#002244', 'NOR':'#d3bc8d', 'NYG':'#0b2265', 'NYJ':'#125740', 'OAK':'#000000', 'PHI':'#004c54', 'PIT':'#ffb612', 'SFO':'#aa0000', 'SEA':'#002244', 'TAM':'#d50a0a', 'TEN':'#0c2340', 'WAS':'#773141'}

# Calculate angles for radar chart
offset = np.pi/6
angles = np.linspace(0, 2*np.pi, len(categories) + 1) + offset


def create_radar_chart(ax, angles, player_data, color='blue'):

    # Plot data and fill with team color
    ax.plot(angles, np.append(player_data[-(len(angles)-1):],
            player_data[-(len(angles)-1)]), color=color, linewidth=2)
    ax.fill(angles, np.append(player_data[-(len(angles)-1):],
            player_data[-(len(angles)-1)]), color=color, alpha=0.2)

    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # Remove radial labels
    ax.set_yticklabels([])

    # Add player name
    ax.text(np.pi/2, 1.7, player_data[0], ha='center', va='center',
            size=18, color=color)

    # Use white grid
    ax.grid(color='white', linewidth=1.5)

    # Set axis limits
    ax.set(xlim=(0, 2*np.pi), ylim=(0, 1)) 

    return ax

# function to get QB data
def get_qb_data(data, team):
    return np.asarray(data[data['Tm'] == team])[0]

# Create figure
fig = plt.figure(figsize=(8, 8), facecolor='white')
# Add subplots
ax1 = fig.add_subplot(221, projection='polar', facecolor='#ededed')
ax2 = fig.add_subplot(222, projection='polar', facecolor='#ededed')
ax3 = fig.add_subplot(223, projection='polar', facecolor='#ededed')
ax4 = fig.add_subplot(224, projection='polar', facecolor='#ededed')
# Adjust space between subplots
plt.subplots_adjust(hspace=0.8, wspace=0.5)
# Get QB data
tam_data = get_qb_data(data_radar, 'TAM')
atl_data = get_qb_data(data_radar, 'ATL') # Mariota season 2018
car_data = get_qb_data(data_radar, 'CAR')
nor_data = get_qb_data(data_radar, 'NOR') # Winston season 2019
# Plot QB data
ax1 = create_radar_chart(ax1, angles, tam_data, team_colors['TAM'])
ax2 = create_radar_chart(ax2, angles, atl_data, team_colors['ATL'])
ax3 = create_radar_chart(ax3, angles, car_data, team_colors['CAR'])
ax4 = create_radar_chart(ax4, angles, nor_data, team_colors['NOR'])

plt.show()