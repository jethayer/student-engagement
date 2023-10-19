#### SER594: Exploratory Data Munging and Visualization
#### Social Media and Attention Span
#### James Thayer
#### 10/18/2023

## Basic Questions
**Dataset Author(s):** 
Pedro Cardoso-Leite

**Dataset Construction Date:** 
6/15/2021 (has recieved updates in October)

**Dataset Record Count:** 
156

**Dataset Field Meanings:** 
—— ID and context variables ——
kid [string]
uniquely identifies a child in the dataset (e.g., “k001”).
teacher [string]
uniquely identifies a teacher in the dataset (e.g., “t01”).
school_year [string]
the child’s grade level at the time of testing. Possible values are: - 5P - 6P - 7P - 8P - special needs
age [float]
age of the child expressed in year (e.g., 11.9).
age_group [string]
age of the child expressed as one of three age range (in years): - [ 8.0,10.2) - [10.2,11.2) - [11.2,12.7]
gender [string]
the child’s gender. - male - female
grades [float]
values from 0 to 1, reflecting the child’s self-reported average grades (0 = lowest possible grade, 1 = highest
possible grade).
—— Media variables ——
read_h [float]
estimated number of daily hours the child spends reading.
video_h [float]
estimated number of daily hours the child spends watching videos.
music_h [float]
estimated number of daily hours the child spends listening to music.
write_h [float]
estimated number of daily hours the child spends writing.
create_h [float]
estimated number of daily hours the child spends creating content (e.g., images).
play_h [float]
estimated number of daily hours the child spends playing video games.
play_action_h [float]
estimated number of daily hours the child spends playing “action-like” video games. Note that some children
might have reported the time spent playing video games without however specifying which kinds of game
were played.
play_nonaction_h [float]
estimated number of daily hours the child spends playing video games that are not “action-like.” Note that
some children might have reported the time spent playing video games without however specifying which
kinds of game were played.
surf_h [float]
estimated number of daily hours the child spends searching information on the internet.
skype_h [float]
estimated number of daily hours the child spends talking to others using technology.
talk_h [float]
estimated number of daily hours the child spends talking to others without using technology.
total_hours_weekday [float]
estimated total number of daily hours the child spends on media during a week day (i.e., excluding weekend
days).
total_hours_weekendday [float]
estimated total number of daily hours the child spends on media during a weekend day (i.e., Saturday or
Sunday).
media_h [float]
estimated total number of daily hours the child spends on media; computed as:
media_h = read_h + video_h + music_h + create_h + write_h + play_h + surf_h + skype_h
mmi_score [float]
score on the media multitasking inventory which measures the average number of additional media used
simultaneously when using a medium; higher scores indicate a larger number of simultaneously used media.
Possible values range from 0 (media used only in single tasking mode) to 7 (using all possible media in
the list, all the time; the list of media included in the mmi score computation are “reading,” “watching
videos,” “listening to music,” “creating content,” “writing,” “playing video games,” “browsing the internet”
and “talking with others using technology”).
mmi_week [float]
mmi score based on week days media consumption.
mmi_weekend [float]
mmi score based on weekend days media consumption.
mm_frequency [float]
self-reported frequency of using multiple media at the same time. Possible values range from 0 (media used
only in single tasking mode) to 1 (always using more than one media at the same time, when using media).
—— Media variables ——
k6_score [float]
score on the K-6 distress scale which evaluates non-specific psychological distress with items relating to
anxiety and depression; a higher score reflects higher levels of emotional distress.
sdq_score [float]
score on the Strength and Difficulties questionnaire; a higher score reflects more greater socio-emotional
difficulties.
ct_score [float]
score reflects how teachers rate their pupils on specific dimensions; a higher score reflects overall more
ADHD-like behavior (i.e., teacher perceives the child as having more difficulties paying attention or engaging
more in impulsive behaviors).
cp_score [float]
score reflects how parents rate their child on specific dimensions; a higher score reflects overall more
ADHD-like behavior (i.e., parent perceives the child as having more difficulties paying attention or engaging
more in impulsive behaviors).
sleep_score [float]
estimate of the child’s sleep quality; a higher score indicates better sleep and less fatigue.
mw_score [float]
the child’s score on the mind wandering questionnaire; a higher score indicates the child has a higher
frequency to experience task unrelated thoughts (i.e., mind wandering).
grit_score [float]
the child’s score on the grit questionnaire; higher scores reflect perseverance and passion for long-term goals.
toi_score [float]
the child’s score on the theory of intelligence questionnaire (i.e., “mindset”); a higher score indicates a
“growth mindset” or a stronger belief that intelligence can be improved.
—— Cognitive test variables ——
d2_rt [float]
average response time per processed symbol in the d2 cancellation test expressed in seconds.
d2_fa_rate [float]
average rate ([0-1]) at which a child incorrectly cancelled a symbol in the d2 cancellation test.
d2_miss_rate [float]
average rate ([0-1]) at which a child incorrectly failed to cancel a symbol in the d2 cancellation test.
sart_rt [float]
sart is a go/no-go task. This variable refers to the average response time on correct “go” trials only, expressed
in seconds.
sart_fa_rate [float]
average rate ([0-1]) at which a child incorrectly responded (“go” response) in the sart test (a go/no-go test).
sart_miss_rate [float]
average rate ([0-1]) at which a child incorrectly failed to respond (i.e., “no-go” response) in the sart test (a
go/no-go test).
blast_rt [float]
average response on correct trials only of the BLAST test, expressed in seconds.
blast_fa_rate [float]
average rate ([0-1]) at which a child incorrectly reported a stimulus array to contain a probe symbol.
blast_miss_rate [float]
average rate ([0-1]) at which a child incorrectly failed to report the presence of a probe symbol in the stimulus
array.

**Dataset File Hash(es):** 
6140E33D460A68C87CF28D32134FFC2B
this hash is for mmi_kids_gva_v2021.2.csv
https://osf.io/8wzbc

## Interpretable Records
### Record 1
**Raw Data:**
k010	t04	5P	8.9	[ 8.0,10.2)	male	0.8	3.357	0.786	0	3.357	1.5	0.357	0.08925	0.26775	0	0.5	4.5	12	4.5	9.857	0.125	0.555555556	0.181191032	0	7	10	34	0.066666667	1	0.25	37	31	1.103448276	0.031547619	0.010869565	0.372	0.015	0.88	1.6555	0.034482759	0.066666667

**Interpretation:**
This record is for the 10th kid in the data set. It lists the relevant data for each of the fields desribed in the field meanings section.
Some ones of note are gender (male), media_h (9.857), and grades (0.7). This data makes sense as it falls within a reasonable range in comparsion
with the other fields. media_h is the hours of media spent in a week and grades is the self reported from from 0-1. 0.7 would be a C.

### Record 2
**Raw Data:**
k014	t02	7P	10.5	[10.2,11.2)	male	0.7	0.5	0.786	0.5	0.5	0.5	1.929	1.929	0	0.5	0.786	1.5	5	8.5	6.001	1.6	1.647058824	1.619063489	0.67	4	12	42	0.366666667	0.357142857	0.55	35	12	0.730593607	0.035714286	0.018403482	0.351	0.0425	0.84	1.228	0.138888889	0.075

**Interpretation:**
This record is for the 14th kid in the data set. All applicable fields for this record have been entered with some relevant examples being
school_year (7P), age(10.5), and mmi_score(1.619063489). Where mmi_score is the average number of additional media used
simultaneously from 0-7, seven being all modes of media listed. These results are reasonable as the age range fits the school year and the
multi media score is in a range that would be expected for the age and is comparable to other records of the field.

## Background Domain Knowledge
This project is directed in an effort to identify with strong correlation if frequent social media usage has a negative impact on attention span, specifically in the 
domain of youth. This dataset takes into account: age, school year, grade received, average social media usage per week, frequency of using multiple forms of media at 
the same time, and various cognitive tests. The data also takes into account outside contributing factors such as amount of sleep, and disabilities. The comparisons of 
various strata and the records as a whole will allow the findings of a statistical significance in the effects of social media, or lack thereof. It has been stated that 
the attention span has gone down by 4 seconds since 2000, according to a study done by Microsoft (Wolmark). The question that is being asked is how much of this is 
actually due to social media and not outside factors. Therefore, the null hypothesis should be that social media does not have a significant effect on attention span 
and the alternative hypothesis, if statistically significant data is found to reject the null, would be that there is an effect. As we look deeper into whether there 
really is an effect, the answer becomes much less clear. The statistic that attention span is shrinking is not a direct source from microsoft but another source called 
Statistic Brain. It may be a myth that attention span is shrinking and it really is all just task-dependent (Maybin). It may also be the case that attention span is 
getting shorter but in a different way. It could be the case that switching tasks makes it seem like it is shorter but really the focus of attention is changing. This 
however, can come at a cost (LaMotte). Switching tasks takes time to reorient yourself to what you are doing and to organize your thoughts. It may be better to be able 
to focus on one task at a time to not incur these costs.

References:
LaMotte, Sandee. “Your Attention Span Is Shrinking, Studies Say. Here’s How to Stay Focused.” CNN, Cable News Network, 30 May 2023, 
edition.cnn.com/2023/01/11/health/short-attention-span-wellness/index.html.

Maybin, Simon. “Busting the Attention Span Myth.” BBC News, BBC, 10 Mar. 2017, www.bbc.com/news/health-38896790.
 
Wolmark, Mark. “Average Human Attention Span (Statistics).” In-Home &amp; Center-Based ABA - Golden Steps ABATM, Golden Steps ABA, 30 Aug. 2023, www.goldenstepsaba.com/resources/average-attention-span#:~:text=Social%20Media%20on%20Attention%20Span,primary%20drivers%20of%20this%20trend.

## Data Transformation
### Transformation 1

**Description:** 
Floor ages to integers. The ages in the CSV were saved as floats with values such as 8.5. 
I would floor this vale and save it as the integer 8.

**Soundness Justification:** 
There is no need for the ages to be eight and half for the purpose of this analyzation. 
Also it does not change the integrity of the data as someone who is eight and a half is 
typically only referred to as eight.

### Transformation 2

**Description:** 
mmi_score truncation to four decimal places. I truncate any and all mmi scores with more than
four decimals to for decimal places maximum.

**Soundness Justification:** 
Some of the mmi scores are very long floating point numbers. This makes the data hard to read. 
There is only really a need to save to two or three decimal places but I decided on four to
ensure integrity and precision of the data.

## Visualization
### Visual 1: media_hours_vs_age
**Analysis:** In this visual it can be seen that the amount of media kids
are consuming in hours/week is relatively close for their age. The minimum 
amount does seem to slightly increase as their age increases. This is no 
surprise as kids will consume more media as they get older.

### Visual 2 media_hours_vs_grades:
**Analysis:** There is not a strong correlation or much of a correlation at 
all for a studnents grade in comparison to how many hours of media they 
consume. There is a wide range of media consumption in hours/week for those 
who recieved at least a 90%.

### Visual 3 media_hours_vs_mmi_score:
**Analysis:** There is a positive linear correlation between those who have 
a lot of media hours and those who use multiple types of media at the same 
time. This makes sense given that one would expect heavy media consumers to 
use many sources of media.

### Visual 4 mmi_score_vs_grades:
**Analysis:** Similarly to media hours vs grades, mmi score vs grades does 
not have a statisitcally significant correlation of those who use media 
multitask with the level of grade attained. Again those who received an A 
grade have a notable range in media multitasking.

### Visual 5 school_year_histogram:
**Analysis:** 
This graph shows frequency of the grade level of the kids(School Year).
The graph varies from 5P to 8P, which is the eqivalent of 3rd to 6th grade 
in the U.S. and  includes a special needs category.
The special needs category has the lowest frequency and 7P has the highest.