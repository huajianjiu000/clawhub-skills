---
name: data-visualizer
description: AI-powered data visualization assistant that transforms raw data into compelling charts, graphs, and dashboards. Recommends optimal chart types, generates visualization code, and creates data stories. Use when presenting data, building dashboards, or explaining trends.
version: 1.0.0
author: muqing
tags: [data-analysis, visualization, charts, reporting]
---

# Data Visualizer

## Description

An AI-powered data visualization assistant that transforms raw data into compelling charts, graphs, and dashboards. Recommends optimal visualization types, generates visualization code, and creates data stories that communicate insights effectively.

## When to Use

- Creating charts from data
- Building dashboards
- Explaining data trends
- Presenting analytics
- Comparing datasets
- Showing distributions
- Visualizing relationships

## Chart Selection Guide

### Comparison
- **Bar Chart**: Compare categories (horizontal for many items)
- **Grouped Bar**: Compare multiple series per category
- **Radar Chart**: Compare multiple variables

### Distribution
- **Histogram**: Frequency distribution
- **Box Plot**: Statistical distribution with outliers
- **Violin Plot**: Distribution shape

### Trends Over Time
- **Line Chart**: Continuous time series
- **Area Chart**: Stacked trends
- **Candlestick**: Stock-like data

### Relationships
- **Scatter Plot**: Two variables correlation
- **Bubble Chart**: Three variables
- **Heatmap**: Correlation matrix

### Parts of Whole
- **Pie Chart**: Simple proportions (use sparingly)
- **Donut Chart**: Similar to pie with center info
- **Stacked Bar**: Proportions over time

### Workflow
1. Analyze data structure
2. Determine visualization goal
3. Select appropriate chart type
4. Generate code
5. Refine for clarity

## Output Formats

### Python (Matplotlib/Seaborn)
```python
import matplotlib.pyplot as plt
import seaborn as sns

# [Generated visualization code]
```

### Python (Plotly)
```python
import plotly.express as px

fig = px.bar(df, x='category', y='value', title='Title')
fig.show()
```

### JavaScript (Chart.js)
```javascript
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C'],
    datasets: [{
      label: 'Values',
      data: [10, 20, 30]
    }]
  }
});
```

### ECharts
```javascript
{
  title: { text: 'Chart Title' },
  xAxis: { type: 'category', data: ['A', 'B', 'C'] },
  yAxis: { type: 'value' },
  series: [{ type: 'bar', data: [10, 20, 30] }]
}
```

## Design Principles

1. **Simplicity**: Less is more
2. **Clarity**: Immediate comprehension
3. **Accuracy**: Don't distort data
4. **Context**: Include labels and scales
5. **Color**: Use accessible palettes
6. **Mobile**: Consider responsive design

## Example Output

```markdown
## Visualization Recommendation

### Data Summary
- Rows: 100
- Columns: ['Month', 'Revenue', 'Expenses']
- Key Insight: Revenue growing faster than expenses

### Recommended Chart Type
Line Chart with dual Y-axis

### Generated Code
```python
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.plot(df['Month'], df['Revenue'], 'b-', label='Revenue')
ax2 = ax1.twinx()
ax2.plot(df['Month'], df['Expenses'], 'r-', label='Expenses')
```

### Design Notes
- Blue for revenue (positive)
- Red for expenses (cost)
- Dual axis to show different scales
- Add legend for clarity
```
