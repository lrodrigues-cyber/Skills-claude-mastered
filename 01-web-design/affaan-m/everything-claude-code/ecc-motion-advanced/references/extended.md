# ecc-motion-advanced — extended reference

## End-to-End Example

Drag-to-dismiss sheet with shimmer content, loading state, and reduced motion
support — combining `useMotionValue`, `useTransform`, `useSafeMotion`,
`AnimatePresence`, and tokens from `motion-foundations`:

```tsx
"use client"
import { useState } from "react"
import { motion, AnimatePresence, useMotionValue, useTransform } from "motion/react"
import { springs, motionTokens } from "@/lib/motion-tokens"
import { useSafeMotion } from "@/hooks/use-reduced-motion"
import { ShimmerSkeleton } from "./shimmer-skeleton"

export function DismissibleSheet({
  isOpen,
  onClose,
  loading,
  children,
}: {
  isOpen: boolean
  onClose: () => void
  loading: boolean
  children: React.ReactNode
}) {
  const safe = useSafeMotion(motionTokens.distance.xl)
  const y = useMotionValue(0)
  const opacity = useTransform(y, [0, 200], [1, 0])

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            key="backdrop"
            className="fixed inset-0 bg-black/40"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
          />

          {/* Sheet — drag-to-dismiss */}
          <motion.div
            key="sheet"
            className="fixed bottom-0 inset-x-0 rounded-t-2xl bg-white p-6"
            drag="y"
            dragConstraints={{ top: 0 }}
            style={{ y, opacity }}
            onDragEnd={(_, info) => {
              if (info.offset.y > 120 || info.velocity.y > 500) onClose()
            }}
            initial={safe.initial}
            animate={safe.animate}
            exit={safe.exit}
            transition={springs.gentle}
          >
            {loading ? (
              <div className="space-y-3">
                <ShimmerSkeleton className="h-4 w-3/4" />
                <ShimmerSkeleton className="h-4 w-1/2" />
                <ShimmerSkeleton className="h-20 w-full" />
              </div>
            ) : children}
          </motion.div>
        </>
      )}
    </AnimatePresence>
  )
}
```

## Constraints / Non-Goals

This skill does **not** cover:

- Token and spring definitions → see `motion-foundations`
- Standard UI patterns (button, modal, stagger, page transitions) → see `motion-patterns`
- CSS-only animations or Tailwind `animate-*` without `motion/react`
- Canvas or WebGL-based animation (Three.js, Pixi, etc.)
- Full drag-and-drop systems with external state managers (dnd-kit, react-beautiful-dnd)
- Game-loop or frame-by-frame animation

## Anti-Patterns

| Anti-pattern | Rule violated | Fix |
| ---------------------------------------------- | ------- | ------------------------------------------------ |
| `drag` tested only on desktop | Rule 1 | Test on touch emulator and real device |
| `animate={{ repeat: Infinity }}` with no pause | Rule 2 | Add `visibilitychange` listener |
| `onDragEnd` checking only offset, not velocity | Rule 3 | Check both `info.offset` and `info.velocity` |
| `animate(scope, ...)` before `useEffect` | Rule 4 | Call `animate()` only after mount |
| `const x = new MotionValue(0)` in render | Rule 5 | Use `const x = useMotionValue(0)` |
| `transition={{ duration: 1.2 }}` inline | Rule 6 | Use `motionTokens.duration.crawl` |
| `useEffect` without cleanup | Rule 7 | Return `removeEventListener` / `controls.stop` |
| SVG morph between paths with different commands | Rule 8 | Normalize path commands before animating |

## Related Skills

- **`motion-foundations`** — defines all tokens, springs, `useSafeMotion`, and SSR guards imported here. Must be set up before using this skill.
- **`motion-patterns`** — handles standard UI patterns (button, modal, stagger, page transitions, scroll reveals). Use it before reaching for the advanced patterns here.
