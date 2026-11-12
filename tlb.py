
MEM = 100
TLB = 10

for h in (0.80, 0.90, 0.98):
    eat = h * (TLB + MEM) + (1 - h) * (TLB + 2 * MEM)
    print(f"hit = {h:.0%} EAT = {eat:.1f} нс")

print("Без TLB:", 2 * MEM, "нс")
