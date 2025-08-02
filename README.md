python form.py 'https://docs.google.com/forms/d/e/1FAIpQLSfDLX0kUUEL_SGEsaRi75IP-iOZIAQJz__iTH5ifgnCE7rQOA/formResponse' -o results.txt

python main.py 'https://docs.google.com/forms/d/e/1FAIpQLSfDLX0kUUEL_SGEsaRi75IP-iOZIAQJz__iTH5ifgnCE7rQOA/viewform' -r
python main.py 'https://docs.google.com/forms/d/1uOKF2UShXqvLUCWjmiToparFlplsU8CMH5LBOg99Ue4/viewform' -r



Based on our previous interactions, I'll help you create a Google Sheets formula to generate dispersed timestamps. Here's a solution that will work in Google Sheets:

In cell A1 (assuming that's where you want to start), enter your base timestamp: 8/2/2025 19:21:56

Then in cell A2, use this formula and drag down for 120 rows:

This formula will:

Start from your base timestamp
Add incremental days (approximately 6 hours intervals since we divide by 4)
Create a sequential dispersion of dates
Maintain time order without random jumps
Alternative formula for different time intervals:

For hourly intervals:
=A2+FLOOR(ROW()-1)/24
For daily intervals:
=A2+FLOOR(ROW()-1)
For weekly intervals:
=A2+FLOOR((ROW()-1)*7)
Make sure to format the cells as "Date Time" in Google Sheets to properly display the timestamps.

To apply:

Enter your base timestamp in A1
Enter the formula in A2
Click and drag the bottom-right corner of A2 down to row 120
Select all cells and format as Date Time

28 April - 3rd July 

6 villages

9 weeks 3 days

'Ajaawa':120-> "2 weeks",  28 April (4/28/2025 ) - 12 May
'Iresi':90->"1 week", 
'Ilora':45->"2 days",
'Olorunda':56->"1 week"
'Omoboriowo':30->"1 week", 
'Oke-Ogbo':14->"1 days", 
'Aka':100->"2 weeks", 
'Iragbiji':83->"2 weeks"
