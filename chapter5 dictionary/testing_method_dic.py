marks={
    "shiv":75,
    "ram":85,
    "sita":90,
    "gita":95,
}
print(marks.items())


print(marks.keys())

marks.update({"s":65,"fd":54})
print(marks)

print(marks.get(("shiv")))

print(marks.values())

print(marks.pop("ram"))

print(marks.clear())

print(marks.setdefault ("shiv",75))
