# Visual Design Mockup Description

## Medical-Grade Admin Interface - Allergy Form

### Overall Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ Django Administration              [User Menu] [Documentation]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🏥 Patient Information                                  │   │
│  │  ┌──────────────┬──────────────┬──────────────┬────────┐│   │
│  │  │ Patient Name │ Date of Birth│ Record ID    │ Blood  ││   │
│  │  │ John Doe     │ Jan 15, 1980 │ PT-2024-001  │ O+     ││   │
│  │  └──────────────┴──────────────┴──────────────┴────────┘│   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ⚠️  High Severity Alert                                  │   │
│  │     This allergy has been marked as severe or life-      │   │
│  │     threatening. Please ensure all details are accurate. │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  👤 Patient & Medical History                            │   │
│  │  ───────────────────────────────────────────────────────│   │
│  │                                                           │   │
│  │  MEDICAL HISTORY RECORD *                                │   │
│  │  [Search patient by name or ID...          ▼]           │   │
│  │                                                           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  🔬 Allergy Details                                       │   │
│  │  ───────────────────────────────────────────────────────│   │
│  │                                                           │   │
│  │  ALLERGEN *                                              │   │
│  │  [Penicillin                                ]           │   │
│  │  Common: Penicillin, Peanuts, Shellfish, Latex...       │   │
│  │                                                           │   │
│  │  REACTION *                                              │   │
│  │  ┌───────────────────────────────────────────────────┐  │   │
│  │  │ Severe hives across torso and arms within 30     │  │   │
│  │  │ minutes of administration. Patient experienced   │  │   │
│  │  │ difficulty breathing and required immediate      │  │   │
│  │  │ epinephrine injection. Resolved after 4 hours.   │  │   │
│  │  └───────────────────────────────────────────────────┘  │   │
│  │                                                           │   │
│  │  SEVERITY LEVEL *                                        │   │
│  │  ┌───────┐  ┌───────┐  ┌───────┐  ┌──────────────┐    │   │
│  │  │ ✓ Mild│  │⚠ Mod  │  │⚠ Sev  │  │🚨 Life Threat│    │   │
│  │  └───────┘  └───────┘  └───────┘  └──────────────┘    │   │
│  │   GREEN      ORANGE       RED         DARK RED          │   │
│  │                                                           │   │
│  │  DATE IDENTIFIED *                                       │   │
│  │  [2025-12-14                📅]                         │   │
│  │                                                           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  📋 Clinical Notes                                        │   │
│  │  ───────────────────────────────────────────────────────│   │
│  │                                                           │   │
│  │  ADDITIONAL NOTES                                        │   │
│  │  ┌───────────────────────────────────────────────────┐  │   │
│  │  │ Patient should avoid all penicillin-based        │  │   │
│  │  │ antibiotics. Consider using cephalosporins only  │  │   │
│  │  │ with caution. Medical alert bracelet recommended│  │   │
│  │  └───────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌────────────────────────────────────────────────┐            │
│  │ [Save Allergy Record] [Save and Add Another] [Cancel]    │
│  └────────────────────────────────────────────────┘            │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Color Scheme (Dark Mode)

#### Background Colors

- Main Background: `#1a1d2e` (very dark blue-gray)
- Card Background: `#2a2e3a` (dark slate)
- Input Fields: `#22262e` (slightly lighter dark)
- Borders: `#3d4451` (medium gray)

#### Text Colors

- Primary Text: `#e4e7eb` (light gray, high contrast)
- Secondary Text: `#9ba3b1` (muted gray for help text)
- Labels: `#e4e7eb` with uppercase styling

#### Accent Colors

- Primary Blue: `#4a90e2` (for buttons, links, focus states)
- Success/Mild: `#4caf50` (green)
- Warning/Moderate: `#ff9800` (orange)
- Danger/Severe: `#f44336` (red)
- Critical: `#d32f2f` (dark red)

### Component Descriptions

#### 1. Patient Summary Card (Top)

- **Background**: Blue gradient (`#4a90e2` to `#357abd`)
- **Border Left**: 5px solid green accent
- **Text Color**: White
- **Icons**: 🏥 hospital emoji
- **Layout**: 4-column grid (responsive to 1-column on mobile)
- **Shadow**: Large shadow for elevation

#### 2. Severity Warning Banner

- **Display**: Hidden by default, shows via JavaScript
- **Background**: Red gradient (`#d32f2f` to `#b71c1c`)
- **Border Left**: 5px solid light red (`#ff5252`)
- **Animation**: Slide down from top
- **Icons**: ⚠️ warning emoji
- **Text**: White with opacity variations

#### 3. Section Cards

- **Background**: `#2a2e3a` (card background)
- **Border**: 1px solid `#3d4451`
- **Border Radius**: 12px
- **Padding**: 2rem
- **Shadow**: Medium shadow, enhanced on hover
- **Hover**: Border turns blue, shadow increases

#### 4. Section Headers

- **Icon Box**: 40x40px, blue background, rounded 10px
- **Icon**: Emoji (👤, 🔬, 📋)
- **Title**: 1.25rem, weight 600
- **Bottom Border**: 2px solid border color

#### 5. Form Inputs

- **Background**: Dark secondary (`#22262e`)
- **Border**: 2px solid border color
- **Border Radius**: 8px
- **Padding**: 0.75rem 1rem
- **Focus State**:
  - Border: Blue accent
  - Shadow: Blue glow (3px spread)
  - Background: Slightly lighter

#### 6. Severity Radio Buttons

- **Layout**: Grid, 4 columns (responsive)
- **Unselected**:
  - Background: Dark secondary
  - Border: 2px solid severity color
  - Text: Severity color
- **Selected**:
  - Background: Solid severity color
  - Text: White
  - Transform: Scale 1.05
  - Shadow: Elevated

#### 7. Action Buttons

- **Primary (Save)**:
  - Background: Blue gradient
  - Text: White
  - Shadow: Blue glow
  - Hover: Lift 2px, increase shadow
- **Secondary (Save & Add)**:
  - Background: Card background
  - Border: 2px solid border
  - Text: Light gray
- **Cancel**:
  - Background: Transparent
  - Border: 2px solid border
  - Text: Muted gray

### Typography

```css
Font Family: 'Segoe UI', system-ui, -apple-system, sans-serif

Sizes:
- Base: 16px (1rem)
- Small: 14px (0.875rem)
- Tiny: 12.8px (0.8rem)
- Large: 20px (1.25rem)
- XLarge: 24px (1.5rem)

Weights:
- Normal: 400
- Medium: 500
- Semibold: 600

Line Heights:
- Tight: 1.2
- Normal: 1.5
- Relaxed: 1.75

Letter Spacing:
- Labels: 0.5px
- Buttons: 0.5px
```

### Spacing System

```css
Base Unit: 8px

Scale:
- XXS: 4px (0.25rem)
- XS: 8px (0.5rem)
- SM: 12px (0.75rem)
- MD: 16px (1rem)
- LG: 24px (1.5rem)
- XL: 32px (2rem)
- XXL: 48px (3rem)

Usage:
- Form row margin: 1.5rem (24px)
- Card padding: 2rem (32px)
- Section header margin: 1.5rem (24px)
- Button padding: 0.875rem 2rem (14px 32px)
```

### Shadows

```css
Small:    0 2px 4px rgba(0, 0, 0, 0.1)
Medium:   0 4px 12px rgba(0, 0, 0, 0.2)
Large:    0 10px 25px rgba(0, 0, 0, 0.3)
Focus:    0 0 0 3px rgba(74, 144, 226, 0.4)
```

### Animations

```css
Transitions:
- Default: all 0.2s ease
- Cards: all 0.3s ease
- Warnings: slide-down 0.3s ease

Hover Effects:
- Buttons: Transform translateY(-2px)
- Cards: Border color + shadow change
- Inputs: Background + border change

Loading:
- Spinner: Rotate 360deg in 1s linear infinite
```

### Responsive Breakpoints

```css
Desktop:  > 768px
  - Full card layout
  - Multi-column grids
  - Side-by-side buttons

Tablet:   768px - 480px
  - Reduced padding
  - 2-column grids
  - Stacked buttons

Mobile:   < 480px
  - Single column
  - Full width elements
  - Vertical buttons
  - Reduced font sizes
```

### Accessibility Features

```css
Focus Indicators:
- 3px solid blue outline
- 2px offset from element
- High contrast

Touch Targets:
- Minimum 44x44px
- Large padding on buttons
- Spaced clickable areas

Keyboard Navigation:
- Logical tab order
- Visible focus states
- Skip links available

Screen Readers:
- Semantic HTML
- ARIA labels
- Alt text for icons
```

This visual design creates a professional, medical-grade interface optimized for healthcare data entry with emphasis on safety, accuracy, and usability.
