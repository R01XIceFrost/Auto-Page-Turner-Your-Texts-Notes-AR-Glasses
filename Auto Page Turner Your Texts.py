#Project I made long time ago in 11/24/2023 on Discord Brilliant Labs

#practical use to my everyday things (I don't mind sharing my notes). It has 1500 loops (until the device runs out of battery) and set to 5 seconds to auto turn next page

#Important Notes

#Don't set it to 1-3 seconds, the alignment text will go haywire around 20 minutes or more. Wait for the firm update to fix this issue.
#If you run same code again after the loops finishes it will give you error like this  MemoryError: memory allocation failed, allocating 1762 bytes
#To fix it, restart your device
#Max Characters is 26 (space included)
 
#Big shout to @p2pDev @josuah  for making this happen and helping out beginner like me! 


import display
import time

l = []
l.append([[display.Text('***TOOL NAMES***', 0, 11, display.RED, justify=display.TOP_LEFT),
display.Text('DIAL TEST INDICATOR', 0, 355, display.BLUE, justify=display.TOP_LEFT),
display.Text('V-ANVIL MICROMETER', 0, 306, display.BLUE, justify=display.TOP_LEFT),
display.Text('GAGE BLOCKS,HEIGHT GAGE', 0, 257, display.BLUE, justify=display.TOP_LEFT),
display.Text('INSIDE MICROMETER', 0, 208, display.BLUE, justify=display.TOP_LEFT),
display.Text('DEPTH GAGE,SINE BAR', 0, 158, display.BLUE, justify=display.TOP_LEFT),
display.Text('V-ANVIL MICROMETER', 0, 109, display.CYAN, justify=display.TOP_LEFT),
display.Text('MICROMETER,HEIGHT GAGE', 0, 60, display.CYAN, justify=display.TOP_LEFT)]
,
[display.Text('Indexing Head', 0, 11, display.CYAN, justify=display.TOP_LEFT),
display.Text('HACKSAW, SCRIBER', 0, 355, display.BLUE, justify=display.TOP_LEFT),
display.Text('ANGLE PLATE,EDGE FINDER', 0, 306, display.BLUE, justify=display.TOP_LEFT),
display.Text('HELICAL/SPUR GEAR', 0, 257, display.BLUE, justify=display.TOP_LEFT),
display.Text('SIDE/FACING TOOL', 0, 208, display.BLUE, justify=display.TOP_LEFT),
display.Text('VERNIER/DIAL CALIPER', 0, 158, display.BLUE, justify=display.TOP_LEFT),
display.Text('MAGNETIC BASE, BROACHING', 0, 109, display.CYAN, justify=display.TOP_LEFT),
display.Text('Dovetail Cutter, KNURLING', 0, 60, display.CYAN, justify=display.TOP_LEFT)]
,
[display.Text('TELESCOPIC GAGE', 0, 11, display.CYAN, justify=display.TOP_LEFT),
display.Text('SNAP GAGE,CUTTING Ext THD', 0, 355, display.BLUE, justify=display.TOP_LEFT),
display.Text('CYLINDRICAL/THREAD GAGE', 0, 306, display.BLUE, justify=display.TOP_LEFT),
display.Text('THREAD PITCH GAGE', 0, 257, display.BLUE, justify=display.TOP_LEFT),
display.Text('SHADOWGRAPH, COMPARATOR', 0, 208, display.BLUE, justify=display.TOP_LEFT),
display.Text('CENTRE DRIL, SQUARE TOOL', 0, 158, display.BLUE, justify=display.TOP_LEFT),
display.Text('RADIUS GAGE, FILE TOOL', 0, 109, display.CYAN, justify=display.TOP_LEFT),
display.Text('SMALL HOLE GAGE', 0, 60, display.CYAN, justify=display.TOP_LEFT)]
,
[display.Text('PRICK/CENTRE PUNCH', 0, 11, display.CYAN, justify=display.TOP_LEFT),
display.Text('BOTTOMING TAP, GEARCUTTING', 0, 355, display.BLUE, justify=display.TOP_LEFT),
display.Text('TAPER TAP, PLUG TAP', 0, 306, display.BLUE, justify=display.TOP_LEFT),
display.Text('BORING, DRILLING, SPOTFACE', 0, 257, display.BLUE, justify=display.TOP_LEFT),
display.Text('COUNTERSINK DRIL BIT', 0, 208, display.BLUE, justify=display.TOP_LEFT),
display.Text('REAMER, COUNTERBORING', 0, 158, display.BLUE, justify=display.TOP_LEFT),
display.Text('THREAD CUTTING', 0, 109, display.CYAN, justify=display.TOP_LEFT),
display.Text('GROOVING (FORM TOOLS)', 0, 60, display.CYAN, justify=display.TOP_LEFT)]
,

[display.Text('PLAIN RING GAUGES', 0, 11, display.CYAN, justify=display.TOP_LEFT),
display.Text('THREAD RING GAGES', 0, 60, display.BLUE, justify=display.TOP_LEFT)]
,

[display.Text('***MACHINE NAMES***', 0, 11, display.RED, justify=display.TOP_LEFT),
display.Text('IMPACT TESTING MACHINE', 0, 355, display.GRAY5, justify=display.TOP_LEFT),
display.Text('HARDNESS TESTER MACHINE', 0, 306, display.GRAY5, justify=display.TOP_LEFT),
display.Text('DRILL PRESS', 0, 257, display.GRAY5, justify=display.TOP_LEFT),
display.Text('BAND SAW MACHINE ROTATING H.', 0, 208, display.GRAY5, justify=display.TOP_LEFT),
display.Text('MILLING MACHINE', 0, 158, display.GRAY5, justify=display.TOP_LEFT),
display.Text('GRINDING MACHINE', 0, 109, display.GRAY5, justify=display.TOP_LEFT),
display.Text('LATHE MACHINE', 0, 60, display.GRAY5, justify=display.TOP_LEFT)]
,

[display.Text('***ABBREVIATIONS & TERMS***', 0, 11, display.BLUE, justify=display.TOP_LEFT)]
,

[display.Text('TPI = THREAD PER INCH', 0, 11, display.YELLOW, justify=display.TOP_LEFT),
display.Text('N = NATIONAL, UN = UNIFIED', 0, 355, display.RED, justify=display.TOP_LEFT),
display.Text('**LATHE = Z (HORIZONTAL)**', 0, 306, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('**LATHE = X (NOT RADIUS)**', 0, 257, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('RELATIVE SYSTEM(PT TO PT)', 0, 208, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('TDS = TAP DRIL SIZE', 0, 158, display.GREEN, justify=display.TOP_LEFT),
display.Text('C = COARSE, F = FINE', 0, 109, display.GREEN, justify=display.TOP_LEFT),
display.Text('**THREAD QUALITY**', 0, 60, display.YELLOW, justify=display.TOP_LEFT)]
,

[display.Text('U & W RELATIVE', 0, 11, display.YELLOW, justify=display.TOP_LEFT),
display.Text('CBORE = Counterbore', 0, 355, display.RED, justify=display.TOP_LEFT),
display.Text('Rc = Rockwell hardness test', 0, 306, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('TIR=TOTAL INDICATED RUNOUT', 0, 257, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('LCS = LOW CARBON STEEL', 0, 208, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('HSS = HIGH SPEED STEEL', 0, 158, display.GREEN, justify=display.TOP_LEFT),
display.Text('GDT=Geometric Dimension...', 0, 109, display.GREEN, justify=display.TOP_LEFT),
display.Text('ABSOLUTE COORDINATES(ZERO)', 0, 60, display.YELLOW, justify=display.TOP_LEFT)]
,

[display.Text('COMMON METHOD SURFACE USE', 0, 11, display.YELLOW, justify=display.TOP_LEFT),
display.Text('TYP. THR. EQL SP. LH RH', 0, 355, display.RED, justify=display.TOP_LEFT),
display.Text('CSK CB SF TAP BLIND HOLE', 0, 306, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('M16x1.5-5g6g (METRIC)', 0, 257, display.MAGENTA, justify=display.TOP_LEFT),           
display.Text('.750-10 UNC-2A (IMPERIUM)', 0, 208, display.MAGENTA, justify=display.TOP_LEFT),
display.Text('Unilateral & Bilateral', 0, 158, display.GREEN, justify=display.TOP_LEFT),
display.Text('TOLERANCE TYPES', 0, 109, display.GREEN, justify=display.TOP_LEFT),
display.Text('Milling, Drilling, Tuning', 0, 60, display.YELLOW, justify=display.TOP_LEFT)]
])

counter = 0
next_time = 0
 
while counter < 1500:
    start_time = time.time()  # find current time in seconds
    next_time = start_time + 10  # Use seconds 

    while time.time() < next_time:
        display.clear()
        #comparison between time to display text for next_time amount of seconds
        for i in range(len(l[0])):
            display.clear()
            for j in range(len(l)):
                display.show(l[j][i])
                time.sleep(5)  # Adjust the sleep duration as needed
              # Display a blank text to clear the display
            time.sleep(1)
                #clear what is on display
        display.clear()
    display.show()
    display.clear()
    counter += 1