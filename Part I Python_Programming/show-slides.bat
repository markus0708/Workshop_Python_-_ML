@echo off
jupyter nbconvert python-beginner.ipynb --to slides --SlidesExporter.reveal_theme=simple --SlidesExporter.reveal_transition=convex --post serve --ServePostProcessor.open_in_browser=True
