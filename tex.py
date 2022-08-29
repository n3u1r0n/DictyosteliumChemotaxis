image_template = '''\\includegraphics[width=0.49\\textwidth]{{{}}}\\hfill
\\includegraphics[width=0.49\\textwidth]{{{}}}
\\\\[\\smallskipamount]
\\includegraphics[width=0.49\\textwidth]{{{}}}\\hfill
\\includegraphics[width=0.49\\textwidth]{{{}}}
\\\\[\\smallskipamount]
\\includegraphics[width=0.49\\textwidth]{{{}}}\\hfill
\\includegraphics[width=0.49\\textwidth]{{{}}}
\\\\[\\smallskipamount]
\\includegraphics[width=0.49\\textwidth]{{{}}}\\hfill
\\includegraphics[width=0.49\\textwidth]{{{}}}'''

minipage_template = '''
\\begin{{minipage}}{{0.55\\textwidth}}
\\begin{{align*}}
{}
\\end{{align*}}
\\end{{minipage}}
\\begin{{minipage}}{{0.45\\textwidth}}

\\end{{minipage}}
'''

# format the frames into a latex document snippet
def tex(frames):
  image = image_template.format(*frames)
  return minipage_template.format(image)