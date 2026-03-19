# Package Delivery Aggregation (Lab Task)

This project processes delivery stop records and aggregates results by:
- `geografine zona` (zone)
- `sustojimo savaites diena` (day of week)

For each `zone|day` key, the final result shows:
- total number of packages (`siuntu skaicius`)
- total number of customers (`Sustojimo klientu skaicius`)

## Main files

- [Task report](Heorhii%20Lytvynenko/report.pdf)
- [Pipeline runner](Heorhii%20Lytvynenko/main.py)
- [Mapper](Heorhii%20Lytvynenko/map.py)
- [Sorter](Heorhii%20Lytvynenko/sort.py)
- [Reducer](Heorhii%20Lytvynenko/red.py)
- [Output before](Heorhii%20Lytvynenko/redout_before.txt)
- [Output after](Heorhii%20Lytvynenko/redout_after.txt)
- [Current output](Heorhii%20Lytvynenko/redout.txt)

## What changed (before vs after)

`redout_after.txt` is higher than `redout_before.txt` for package totals in every group, while customer totals stayed the same.

Examples:
- `Z1|1`: packages `86464 -> 90560` (`+4096`), customers `41580 -> 41580` (`+0`)
- `Z2|3`: packages `30715 -> 32146` (`+1431`), customers `18545 -> 18545` (`+0`)
- `Z3|5`: packages `18423 -> 19214` (`+791`), customers `12304 -> 12304` (`+0`)

## Why results changed

The mapper logic was updated to keep records even when customer count is missing:
- packages are still counted
- missing customer value is treated as `0`

Because of that, additional valid package records are included in the final aggregation, but customer sums remain unchanged.
