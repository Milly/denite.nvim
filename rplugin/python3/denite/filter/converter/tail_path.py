# ============================================================================
# FILE: converter/tail_path.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from pathlib import Path

from denite.base.filter import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'converter/tail_path'
        self.description = 'convert candidate tail path to word'

    def filter(self, context):
        for candidate in context['candidates']:
            if 'abbr' not in candidate:
                candidate['abbr'] = candidate['word']
            candidate['word'] = Path(candidate.get(
                'action__path', candidate['word'])).name
        return context['candidates']
