# African Union Flag Emoji Font

Custom COLRv1 color webfont containing the African Union flag emoji mapped to Unicode Private Use Area codepoint **U+E001**.

## Files

| File | Size | Format | Description |
|------|------|--------|-------------|
| `AfricanUnionEmoji.woff2` | 10.7KB | COLRv1 + CPAL | **Color font** with green background, gold stars, white sunburst |

## Usage

### HTML

```html
<!-- Using the utility class -->
<span class="au-emoji">&#xE001;</span>

<!-- Or with inline style -->
<span style="font-family: 'AfricanUnionEmoji', sans-serif;">&#xE001;</span>
```

### CSS

```css
@font-face {
  font-family: 'AfricanUnionEmoji';
  src: url('/assets/fonts/au-flag-emoji/AfricanUnionEmoji.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
  unicode-range: U+E001;
}

.au-emoji {
  font-family: 'AfricanUnionEmoji', 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif;
}
```

## Unicode Mapping

| Codepoint | Glyph | Description |
|-----------|-------|-------------|
| U+E001 | 🇦🇺 | African Union flag (green, gold, white) |

## Browser Compatibility

- Chrome 90+
- Firefox 105+
- Edge 90+
- Safari 15.4+

Older browsers will fall back to system emoji fonts.

## Regeneration

### Using nanoemoji

```bash
# Install nanoemoji
pip install nanoemoji

# Generate COLRv1 color font
cp african-union.svg emoji_uE001.svg
nanoemoji --color_format glyf_colr_1 \
  --family AfricanUnionEmoji \
  --output_file AfricanUnionEmoji.ttf \
  emoji_uE001.svg

# Convert to WOFF2
python3 -c "
from fontTools.ttLib import TTFont
font = TTFont('build/AfricanUnionEmoji.ttf')
font.flavor = 'woff2'
font.save('AfricanUnionEmoji.woff2')
"

# Cleanup
rm -rf build emoji_uE001.svg
```

## Font Details

- **Format**: WOFF2 with COLRv1 color tables
- **Family Name**: AfricanUnionEmoji
- **Codepoint**: U+E001 (BMP Private Use Area)
- **Glyphs**: Single glyph (African Union flag)
- **Colors**: Green (#3f724a), Gold (#eec62d), White (#fff)
- **Source**: African Union flag SVG from Wikimedia Commons

## Color Font Technology

This font uses **COLRv1** (Color Layer Vector) table format:
- COLR table stores layered vector graphics with color information
- CPAL (Color Palette) table defines the color palette
- WOFF2 compression preserves color tables
- Vector-based colors scale infinitely without pixelation
