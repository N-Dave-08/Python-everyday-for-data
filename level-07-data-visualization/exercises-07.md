# Level 7 Exercises: Data Visualization

Complete these exercises to practice creating visualizations with matplotlib and seaborn.

## Exercise 1: Basic Line Plot
**Difficulty: Beginner**

Using `employees.csv`:
1. Create a line plot showing employee_id vs salary
2. Add proper labels and title
3. Add a grid
4. Save the plot as 'salary_line.png'

**Expected Output:**
A line plot showing salary progression across employees.

---

## Exercise 2: Bar Chart
**Difficulty: Beginner**

Using `employees.csv`:
1. Calculate average salary by department
2. Create a bar chart showing this
3. Add labels, title, and color the bars
4. Rotate x-axis labels if needed

**Expected Output:**
A bar chart showing average salary for each department.

---

## Exercise 3: Scatter Plot
**Difficulty: Beginner**

Using `employees.csv`:
1. Create a scatter plot of age vs salary
2. Color points by department_id
3. Add labels and title
4. Add a legend

**Expected Output:**
A scatter plot showing relationship between age and salary, colored by department.

---

## Exercise 4: Histogram
**Difficulty: Beginner**

Using `employees.csv`:
1. Create a histogram of salary distribution
2. Use 20 bins
3. Add labels and title
4. Add a vertical line for the mean salary

**Expected Output:**
A histogram showing salary distribution with mean line.

---

## Exercise 5: Multiple Subplots
**Difficulty: Intermediate**

Using `employees.csv`:
1. Create a 2x2 subplot grid
2. Plot 1: Salary histogram
3. Plot 2: Age vs Salary scatter
4. Plot 3: Average salary by department (bar)
5. Plot 4: Salary box plot by department
6. Add titles to each subplot

**Expected Output:**
A figure with 4 different visualizations.

---

## Exercise 6: Seaborn Bar Plot
**Difficulty: Intermediate**

Using `employees.csv`:
1. Use seaborn to create a bar plot of average salary by department
2. Add error bars
3. Customize colors
4. Add proper labels and title

**Expected Output:**
A seaborn bar plot with error bars.

---

## Exercise 7: Box Plot
**Difficulty: Intermediate**

Using `employees.csv`:
1. Create a box plot showing salary distribution by department
2. Use seaborn for better styling
3. Add labels and title
4. Identify outliers if any

**Expected Output:**
A box plot showing salary distributions by department.

---

## Exercise 8: Heatmap
**Difficulty: Intermediate**

Using `employees.csv`:
1. Select numerical columns (age, salary, etc.)
2. Calculate correlation matrix
3. Create a heatmap of correlations
4. Add annotations showing correlation values
5. Use a color scheme (coolwarm)

**Expected Output:**
A correlation heatmap showing relationships between numerical variables.

---

## Exercise 9: Advanced Visualization
**Difficulty: Advanced**

Using merged data from employees and departments:
1. Create a grouped bar chart showing:
   - Average salary by department
   - Number of employees by department
2. Use different colors for each metric
3. Add a legend
4. Make it publication-ready

**Expected Output:**
A grouped bar chart with multiple metrics.

---

## Exercise 10: Comprehensive Dashboard
**Difficulty: Advanced**

Create a comprehensive visualization dashboard:
1. Read employees and sales data
2. Create a figure with multiple subplots:
   - Sales over time (line plot)
   - Top 5 products by sales (bar chart)
   - Sales by region (pie chart or bar)
   - Sales distribution (histogram)
3. Add overall title
4. Save as high-resolution image

**Expected Output:**
A comprehensive dashboard with multiple visualizations.

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use `plt.plot()`, `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.grid()`, `plt.savefig()`.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Group by department, calculate mean, use `plt.bar()`, customize colors.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use `plt.scatter()` with `c` parameter for colors, add `plt.colorbar()` or `plt.legend()`.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use `plt.hist()`, calculate mean with `df['salary'].mean()`, add vertical line with `plt.axvline()`.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `plt.subplots(2, 2)`, plot on each axis, use `plt.tight_layout()`.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Use `sns.barplot()`, it automatically adds error bars, customize with `palette` parameter.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Use `sns.boxplot()`, specify x and y parameters, identify outliers visually.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use `df.corr()` for correlation, `sns.heatmap()` with `annot=True`, choose colormap.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Prepare data with both metrics, use grouped bar chart technique, customize colors and legend.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Create large figure, use subplots, create different plot types, add overall title with `plt.suptitle()`.
</details>

---

**Good luck!** Visualization is both art and science. Experiment with colors, styles, and layouts to create clear, informative plots.
