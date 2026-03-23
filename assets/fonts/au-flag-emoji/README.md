# African Union Flag Emoji Font

Custom COLRv1 color webfont containing the African Union flag emoji mapped to **U+1F30D** (🌍 Earth Globe Europe-Africa emoji).

> **Fallback strategy**: When the custom font loads, displays the African Union flag. When the font fails, falls back to the standard 🌍 emoji.

## Files

| File | Size | Format | Description |
|------|------|--------|-------------|
| `AfricanUnionEmoji.woff2` | 10.7KB | COLRv1 + CPAL | **Color font** with green background, gold stars, white sunburst |

## Usage

### HTML

```html
<!-- Using the utility class -->
<span class="au-emoji">🌍</span>

<!-- Or with HTML entity -->
<span class="au-emoji">&#x1F30D;</span>

<!-- Or with inline style -->
<span style="font-family: 'AfricanUnionEmoji', 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif;">🌍</span>
```

### CSS

```css
@font-face {
  font-family: 'AfricanUnionEmoji';
  src: url('/assets/fonts/au-flag-emoji/AfricanUnionEmoji.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
  unicode-range: U+1F30D;
}

.au-emoji {
  font-family: 'AfricanUnionEmoji', 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif;
}
```

## Unicode Mapping

| Codepoint | Glyph | Description | Fallback |
|-----------|-------|-------------|----------|
| U+1F30D | 🇦🇺 | African Union flag (green, gold, white) | 🌍 Earth emoji |

## Browser Compatibility

- Chrome 90+
- Firefox 105+
- Edge 90+
- Safari 15.4+

Older browsers will fall back to system emoji fonts.

## Regeneration

This repository uses a two-step deterministic pipeline:

1. Build base COLRv1 font from `african-union.svg` using `nanoemoji`
2. Apply a fixed post-process pass to reproduce the final horizontal tuning

Run all commands from `assets/fonts/au-flag-emoji`.

### 1) Build base font from SVG

```bash
# Prerequisites
python3 -m pip install nanoemoji fonttools

# Clean and build
rm -rf build emoji_u1F30D.svg AfricanUnionEmoji.ttf AfricanUnionEmoji.woff2
cp african-union.svg emoji_u1F30D.svg

nanoemoji --color_format glyf_colr_1 \
  --family AfricanUnionEmoji \
  --output_file AfricanUnionEmoji.ttf \
  emoji_u1F30D.svg

python3 - <<'PY'
from fontTools.ttLib import TTFont

font = TTFont('build/AfricanUnionEmoji.ttf')
font.flavor = 'woff2'
font.save('AfricanUnionEmoji.woff2')
PY
```

### 2) Apply final alignment tuning (authoritative)

This pass reproduces the final, validated tuning exactly:

- keep glyph width at `1020`
- keep `LSB` baseline to `0`
- move COLRv1 painted layers by `x = -127.5`
- shift COLR ClipBox by the same amount to avoid left clipping

```bash
python3 - <<'PY'
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables

X_SHIFT = -127.5
TARGET_ADVANCE = 1020
TARGET_LSB = 0
GLYPH = 'u1F30D'
PATH = 'AfricanUnionEmoji.woff2'

font = TTFont(PATH)
colr = font['COLR'].table

# Move every layer in the base glyph paint stack by X_SHIFT.
# Existing PaintTransform (Format 12): add to dx.
# PaintGlyph (Format 10): wrap with identity PaintTransform carrying dx.
layers = colr.LayerList.Paint
for i, paint in enumerate(layers):
    if paint.Format == 12:
        paint.Transform.dx += X_SHIFT
    elif paint.Format == 10:
        wrapped = otTables.Paint()
        wrapped.Format = 12
        wrapped.Paint = paint

        t = otTables.Affine2x3()
        t.xx = 1.0
        t.xy = 0.0
        t.yx = 0.0
        t.yy = 1.0
        t.dx = X_SHIFT
        t.dy = 0.0
        wrapped.Transform = t

        layers[i] = wrapped
    else:
        raise RuntimeError(f'Unexpected paint format {paint.Format} at layer {i}')

# Keep clip bounds aligned with the moved artwork (prevents left-edge clipping).
clip = colr.ClipList.clips[GLYPH]
clip.xMin = int(round(clip.xMin + X_SHIFT))
clip.xMax = int(round(clip.xMax + X_SHIFT))

# Keep spacing intent: advance width fixed to 1020, LSB baseline restored to 0.
font['hmtx'].metrics[GLYPH] = (TARGET_ADVANCE, TARGET_LSB)
font['hhea'].advanceWidthMax = max(a for a, _ in font['hmtx'].metrics.values())

font.flavor = 'woff2'
font.save(PATH)
PY
```

### 3) Verify expected final values

```bash
python3 - <<'PY'
from collections import Counter
from fontTools.ttLib import TTFont

font = TTFont('AfricanUnionEmoji.woff2')
glyph = font.getBestCmap()[0x1F30D]

hmtx = font['hmtx'].metrics[glyph]
clip = font['COLR'].table.ClipList.clips[glyph]
formats = Counter(p.Format for p in font['COLR'].table.LayerList.Paint)
hhea = (font['hhea'].ascent, font['hhea'].descent, font['hhea'].lineGap)
os2 = (font['OS/2'].sTypoAscender, font['OS/2'].sTypoDescender, font['OS/2'].sTypoLineGap)

print('glyph:', glyph)
print('hmtx:', hmtx)
print('clip:', (clip.xMin, clip.xMax, clip.yMin, clip.yMax))
print('layer_formats:', dict(formats))
print('hhea:', hhea)
print('OS/2 typo:', os2)

assert hmtx == (1020, 0)
assert (clip.xMin, clip.xMax, clip.yMin, clip.yMax) == (52, 972, 40, 660)
assert formats == {12: 169}
assert hhea == (950, -250, 0)
assert os2 == (950, -250, 0)
PY
```

### Cleanup

```bash
rm -rf build emoji_u1F30D.svg AfricanUnionEmoji.ttf
```

## Font Details

- **Format**: WOFF2 with COLRv1 color tables
- **Family Name**: AfricanUnionEmoji
- **Codepoint**: U+1F30D (🌍 Earth Globe Europe-Africa)
- **Fallback**: 🌍 emoji when font unavailable
- **Glyphs**: Single glyph (African Union flag)
- **Colors**: Green (#3f724a), Gold (#eec62d), White (#fff)
- **Source**: African Union flag SVG from Wikimedia Commons

## Color Font Technology

This font uses **COLRv1** (Color Layer Vector) table format:
- COLR table stores layered vector graphics with color information
- CPAL (Color Palette) table defines the color palette
- WOFF2 compression preserves color tables
- Vector-based colors scale infinitely without pixelation
