"""Save DOT source lines."""

import logging
import os
import typing

from . import base
from . import encoding
from . import tools

__all__ = ['File']

log = logging.getLogger(__name__)


class File(base.Base, encoding.Encoding):
    """Save DOT source lines to file."""

    directory = ''

    _default_extension = 'gv'

    def __init__(self, filename=None, directory=None, **kwargs):
        super().__init__(**kwargs)

        if filename is None:
            name = getattr(self, 'name', None) or self.__class__.__name__
            filename = f'{name}.{self._default_extension}'
        self.filename = filename

        if directory is not None:
            self.directory = directory

    def _kwargs(self):
        result = super()._kwargs()
        result['filename'] = self.filename
        if 'directory' in self.__dict__:
            result['directory'] = self.directory
        return result

    @property
    def filepath(self):
        return os.path.join(self.directory, self.filename)

    def save(self, filename=None, directory=None,
             *, skip_existing: typing.Optional[bool] = False):
        """Save the DOT source to file. Ensure the file ends with a newline.

        Args:
            filename: Filename for saving the source (defaults to ``name`` + ``'.gv'``)
            directory: (Sub)directory for source saving and rendering.
            skip_existing: Skip write if file exists (default: ``False``).

        Returns:
            The (possibly relative) path of the saved source file.
        """
        if filename is not None:
            self.filename = filename
        if directory is not None:
            self.directory = directory

        filepath = self.filepath
        if skip_existing and os.path.exists(filepath):
            return filepath

        tools.mkdirs(filepath)

        log.debug('write lines to %r', filepath)
        with open(filepath, 'w', encoding=self.encoding) as fd:
            for uline in self:
                fd.write(uline)

        return filepath
