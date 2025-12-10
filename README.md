## LinkedIn bug:

## AIM :

To identify and correct incorrect experience duration displayed on LinkedIn when start and end dates are entered accurately, but LinkedIn auto-calculates the duration wrong by adding an extra month.



## 🚨 ISSUE DESCRIPTION

LinkedIn automatically calculates “total experience duration” based on start and end dates.

 



I noticed LinkedIn’s experience-duration auto-calculation was adding an extra month to some of my work experiences. I manually verified the correct duration based on start and end dates, identified the calculation mismatch, and updated the entries. After re-saving the exact same dates, LinkedIn recalculated the durations correctly.

This fixed the incorrect “+1 month” error across affected job entries.

## 🐞 BUG EXPLANATION (Easy to Understand)

LinkedIn calculates experience based on month-to-month difference, not real calendar months.

LinkedIn logic:

If you select Nov → Oct, LinkedIn treats it as if one full month more is completed.

Therefore:

11 months becomes 12

35 months becomes 36

And LinkedIn displays +1 month extra

This is a known LinkedIn duration miscalculation bug.

<img width="937" height="199" alt="Screenshot 2025-12-02 201949" src="https://github.com/user-attachments/assets/da5a3edb-48d7-4d1c-89d9-1c69dcb3bc78" />
<img width="943" height="292" alt="Screenshot 2025-12-10 162320" src="https://github.com/user-attachments/assets/83d6e057-22d0-4506-bfe1-7c0e132992f6" />
