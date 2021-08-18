# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2021, James R. Barlow (https://github.com/jbarlow83/)

# pybind11 does not generate type annotations yet, and mypy doesn't understand
# the way we're augmenting C++ classes with Python methods as in
# pikepdf/_methods.py. Thus, we need to manually spell out the resulting types
# after augmenting.

import datetime
from abc import abstractmethod
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import (
    Any,
    BinaryIO,
    Callable,
    Collection,
    Dict,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    List,
    MutableMapping,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from pikepdf.models.encryption import Encryption, EncryptionInfo, Permissions
from pikepdf.models.image import PdfInlineImage
from pikepdf.models.metadata import PdfMetadata
from pikepdf.models.outlines import Outline
from pikepdf.objects import Array, Dictionary, Name, Stream

# This is the whole point of stub files, but apparently we have to do this...
# pylint: disable=no-method-argument,unused-argument,no-self-use,too-many-public-methods

T = TypeVar('T', bound='Object')
Numeric = TypeVar('Numeric', int, float, Decimal)

class Buffer: ...

# Exceptions

class DataDecodingError(Exception): ...
class PasswordError(Exception): ...
class PdfError(Exception): ...
class ForeignObjectError(Exception): ...

# Enums
class AccessMode(Enum):
    default: int = ...
    mmap: int = ...
    mmap_only: int = ...
    stream: int = ...

class EncryptionMethod(Enum):
    none: int = ...
    unknown: int = ...
    rc4: int = ...
    aes: int = ...
    aesv3: int = ...

class ObjectStreamMode(Enum):
    disable: int = ...
    generate: int = ...
    preserve: int = ...

class ObjectType(Enum):
    array: int = ...
    boolean: int = ...
    dictionary: int = ...
    inlineimage: int = ...
    integer: int = ...
    name_: int = ...
    null: int = ...
    operator: int = ...
    real: int = ...
    reserved: int = ...
    stream: int = ...
    string: int = ...
    uninitialized: int = ...

class StreamDecodeLevel(Enum):
    all: int = ...
    generalized: int = ...
    none: int = ...
    specialized: int = ...

class TokenType(Enum):
    array_close: int = ...
    array_open: int = ...
    bad: int = ...
    bool: int = ...
    brace_close: int = ...
    brace_open: int = ...
    comment: int = ...
    dict_close: int = ...
    dict_open: int = ...
    eof: int = ...
    inline_image: int = ...
    integer: int = ...
    name_: int = ...
    null: int = ...
    real: int = ...
    space: int = ...
    string: int = ...
    word: int = ...

# Object
class Object:
    def _ipython_key_completions_(self) -> Optional[KeysView]: ...
    def _inline_image_raw_bytes(self) -> bytes: ...
    def _parse_page_contents(self, callbacks: Callable) -> None: ...
    def _parse_page_contents_grouped(
        self, whitelist: str
    ) -> List[Tuple[Collection[Union[Object, PdfInlineImage]], 'Operator']]: ...
    def _parse_stream(self, *args, **kwargs) -> Any: ...
    def _parse_stream_grouped(self, *args, **kwargs) -> Any: ...
    def _repr_mimebundle_(self, include=None, exclude=None) -> Optional[Dict]: ...
    def _write(
        self,
        data: bytes,
        filter: Object,  # pylint: disable=redefined-builtin
        decode_parms: Object,
    ) -> None: ...
    def append(self, pyitem: Any) -> None: ...
    def as_dict(self) -> '_ObjectMapping': ...
    def as_list(self) -> '_ObjectList': ...
    def emplace(self, other: Object, retain: Iterable['Name'] = ...) -> None: ...
    def extend(self, arg0: Iterable[Object]) -> None: ...
    @overload
    def get(
        self, key: str, default: Optional[T] = ...
    ) -> Union[Optional[T], Object]: ...
    @overload
    def get(
        self, key: Name, default: Optional[T] = ...
    ) -> Union[Optional[T], Object]: ...
    def get_raw_stream_buffer(self) -> Buffer: ...
    def get_stream_buffer(self, decode_level: StreamDecodeLevel = ...) -> Buffer: ...
    def is_owned_by(self, possible_owner: 'Pdf') -> bool: ...
    def items(self) -> Iterable[Tuple[str, Object]]: ...
    def keys(self) -> Set[str]: ...
    @staticmethod
    def parse(stream: bytes, description: str = ...) -> Object: ...
    def read_bytes(self, decode_level: StreamDecodeLevel = ...) -> bytes: ...
    def read_raw_bytes(self) -> bytes: ...
    def same_owner_as(self, other: Object) -> bool: ...
    def to_json(self, dereference: bool = ...) -> bytes: ...
    def unparse(self, resolved: bool = ...) -> bytes: ...
    def with_same_owner_as(self, arg0: Object) -> Object: ...
    def wrap_in_array(self) -> Object: ...
    def write(
        self,
        data: bytes,
        *,
        filter: Union['Name', 'Array', None] = ...,  # pylint: disable=redefined-builtin
        decode_parms: Union['Dictionary', 'Array', None] = ...,
        type_check: bool = ...,
    ) -> None: ...
    def __bytes__(self) -> bytes: ...
    @overload
    def __contains__(self, arg0: Object) -> bool: ...
    @overload
    def __contains__(self, arg0: str) -> bool: ...
    def __copy__(self) -> Object: ...
    def __delattr__(self, arg0: str) -> None: ...
    @overload
    def __delitem__(self, arg0: str) -> None: ...
    @overload
    def __delitem__(self, arg0: Object) -> None: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    def __dir__(self) -> list: ...
    def __eq__(self, other: Any) -> bool: ...
    def __getattr__(self, arg0: str) -> Object: ...
    @overload
    def __getitem__(self, arg0: str) -> Object: ...
    @overload
    def __getitem__(self, arg0: Object) -> Object: ...
    @overload
    def __getitem__(self, arg0: int) -> Object: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterable[Object]: ...
    def __len__(self) -> int: ...
    def __setattr__(self, arg0: str, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: str, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: Object, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: str, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: Object, arg1: object) -> None: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: int, arg1: object) -> None: ...
    @property
    def _objgen(self) -> Tuple[int, int]: ...
    @property
    def _type_code(self) -> ObjectType: ...
    @property
    def _type_name(self) -> str: ...
    @property
    def images(self) -> '_ObjectMapping': ...
    @property
    def is_indirect(self) -> bool: ...
    @property
    def is_rectangle(self) -> bool: ...
    @property
    def objgen(self) -> Tuple[int, int]: ...
    @property
    def stream_dict(self) -> Object: ...
    @stream_dict.setter
    def stream_dict(self, val: Object) -> None: ...

class _ObjectList:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: _ObjectList) -> None: ...
    @overload
    def __init__(self, arg0: Iterable) -> None: ...
    @overload
    def __init__(*args, **kwargs) -> None: ...
    def append(self, x: Object) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: Object) -> int: ...
    @overload
    def extend(self, L: _ObjectList) -> None: ...
    @overload
    def extend(self, L: Iterable[Object]) -> None: ...
    def insert(self, i: int, x: Object) -> None: ...
    @overload
    def pop(self) -> Object: ...
    @overload
    def pop(self, i: int) -> Object: ...
    @overload
    def pop(*args, **kwargs) -> Any: ...
    def remove(self, x: Object) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, x: Object) -> bool: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    @overload
    def __delitem__(self, arg0: slice) -> None: ...
    @overload
    def __delitem__(*args, **kwargs) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    @overload
    def __getitem__(self, s: slice) -> _ObjectList: ...
    @overload
    def __getitem__(self, arg0: int) -> Object: ...
    @overload
    def __getitem__(*args, **kwargs) -> Any: ...
    def __iter__(self) -> Iterator[Object]: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: Any) -> bool: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Object) -> None: ...
    @overload
    def __setitem__(self, arg0: slice, arg1: _ObjectList) -> None: ...
    @overload
    def __setitem__(*args, **kwargs) -> Any: ...

class _ObjectMapping:
    get: Any = ...
    keys: Any = ...
    values: Any = ...
    __contains__: Any = ...
    def __init__(self) -> None: ...
    def items(self) -> Iterator: ...
    def __bool__(self) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> Object: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: Object) -> None: ...

class Operator(Object): ...

class Annotation:
    def __init__(self, arg0: Object) -> None: ...
    @overload
    def get_appearance_stream(self, which: Object) -> Object: ...
    @overload
    def get_appearance_stream(self, which: Object, state: Object) -> Object: ...
    def get_page_content_for_appearance(
        self,
        name: Object,
        rotate: int,
        required_flags: int = ...,
        forbidden_flags: int = ...,
    ) -> bytes: ...
    @property
    def appearance_dict(self) -> Object: ...
    @property
    def appearance_state(self) -> Object: ...
    @property
    def flags(self) -> int: ...
    @property
    def obj(self) -> Object: ...
    @property
    def subtype(self) -> str: ...

class AttachedFile:
    _creation_date: str
    _mod_date: str
    creation_date: Optional[datetime.datetime]
    mime_type: str
    mod_date: Optional[datetime.datetime]
    @property
    def md5(self) -> bytes: ...
    @property
    def obj(self) -> Object: ...
    def read_bytes(self) -> bytes: ...
    @property
    def size(self) -> int: ...

class AttachedFileSpec:
    description: str
    filename: str
    def __init__(
        self, stream: Union[Stream, BinaryIO, Path], description: str
    ) -> None: ...
    def get_all_filenames(self) -> dict: ...
    @overload
    def get_file(self) -> AttachedFile: ...
    @overload
    def get_file(self, name: Name) -> AttachedFile: ...
    @property
    def obj(self) -> Object: ...

class Attachments(MutableMapping[str, AttachedFileSpec]):
    def __contains__(self, k: object) -> bool: ...
    def __delitem__(self, k: str) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __getitem__(self, k: str) -> AttachedFileSpec: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, k: str, v: AttachedFileSpec): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _add_replace_filespec(self, arg0: str, arg1: AttachedFileSpec) -> None: ...
    def _get_all_filespecs(self) -> Dict[str, AttachedFileSpec]: ...
    def _get_filespec(self, arg0: str) -> AttachedFileSpec: ...
    def _remove_filespec(self, arg0: str) -> bool: ...
    @property
    def _has_embedded_files(self) -> bool: ...

class Token:
    def __init__(self, arg0: TokenType, arg1: bytes) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def error_msg(self) -> str: ...
    @property
    def raw_value(self) -> bytes: ...
    @property
    def type_(self) -> TokenType: ...
    @property
    def value(self) -> str: ...

class _QPDFTokenFilter: ...

class TokenFilter(_QPDFTokenFilter):
    def __init__(self) -> None: ...
    def handle_token(self, token: Token = ...) -> Union[None, List, Token]: ...

class StreamParser:
    def __init__(self) -> None: ...
    @abstractmethod
    def handle_eof(self) -> None: ...
    @abstractmethod
    def handle_object(self, obj: Object) -> None: ...

class Page:
    _repr_mimebundle_: Any = ...
    @overload
    def __init__(self, arg0: Object) -> None: ...
    @overload
    def __init__(self, arg0: Page) -> None: ...
    def __contains__(self, key: Any) -> bool: ...
    def __delattr__(self, name: Any) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __getattr__(self, name: Any) -> Object: ...
    def __getitem__(self, name: Any) -> Object: ...
    def __setattr__(self, name: Any, value: Any): ...
    def __setitem__(self, name: Any, value: Any): ...
    def _get_cropbox(self, arg0: bool) -> Object: ...
    def _get_mediabox(self, arg0: bool) -> Object: ...
    def _get_trimbox(self, arg0: bool) -> Object: ...
    def add_content_token_filter(self, tf: TokenFilter) -> None: ...
    def add_overlay(self, other: Union[Object, Page], rect: Optional['Rectangle']): ...
    def add_underlay(self, other: Union[Object, Page], rect: Optional['Rectangle']): ...
    def as_form_xobject(self, handle_transformations: bool = ...) -> Object: ...
    def calc_form_xobject_placement(
        self,
        formx: Object,
        name: Name,
        rec: 'Rectangle',
        *,
        invert_transformations: bool,
        allow_shrink: bool,
        allow_expand: bool,
    ) -> bytes: ...
    def contents_add(
        self, contents: Union['Stream', bytes], *, prepend: bool
    ) -> None: ...
    def contents_coalesce(self) -> None: ...
    def emplace(self, other: Page, retain: Iterable[Name]) -> None: ...
    def externalize_inline_images(self, min_size: int = ...) -> None: ...
    def get(
        self, key: Union[str, Name], default: Optional[T] = ...
    ) -> Union[Optional[T], Object]: ...
    def get_filtered_contents(self, tf: TokenFilter) -> bytes: ...
    def index(self) -> int: ...
    def label(self) -> str: ...
    def parse_contents(self, arg0: StreamParser) -> None: ...
    def remove_unreferenced_resources(self) -> None: ...
    def rotate(self, angle: int, relative: bool) -> None: ...
    @property
    def images(self) -> _ObjectMapping: ...
    @property
    def cropbox(self) -> 'Array': ...
    @cropbox.setter
    def cropbox(self, val: 'Array') -> None: ...
    @property
    def mediabox(self) -> 'Array': ...
    @mediabox.setter
    def mediabox(self, val: 'Array') -> None: ...
    @property
    def obj(self) -> Dictionary: ...
    @property
    def trimbox(self) -> 'Array': ...
    @trimbox.setter
    def trimbox(self, val: 'Array') -> None: ...
    @property
    def resources(self) -> Dictionary: ...
    def add_resource(
        self,
        res: Object,
        res_type: Name,
        name: Optional[Name] = None,
        *,
        prefix: str = '',
        replace_existing: bool = True,
    ) -> Name: ...

class PageList:
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, page: Page) -> None: ...
    @overload
    def extend(self, other: PageList) -> None: ...
    @overload
    def extend(self, iterable: Iterable[Page]) -> None: ...
    def insert(self, index: int, obj: Page) -> None: ...
    def p(self, pnum: int) -> Page: ...
    def remove(self, **kwargs) -> None: ...
    def reverse(self) -> None: ...
    @overload
    def __delitem__(self, arg0: int) -> None: ...
    @overload
    def __delitem__(self, arg0: slice) -> None: ...
    @overload
    def __getitem__(self, arg0: int) -> Page: ...
    @overload
    def __getitem__(self, arg0: slice) -> list: ...
    def __iter__(self) -> PageList: ...
    def __len__(self) -> int: ...
    def __next__(self) -> Page: ...
    @overload
    def __setitem__(self, arg0: int, arg1: Page) -> None: ...
    @overload
    def __setitem__(self, arg0: slice, arg1: Iterable[Page]) -> None: ...

class Pdf:
    _repr_mimebundle_: Any = ...
    def add_blank_page(self, *, page_size: Tuple[Numeric, Numeric] = ...) -> Page: ...
    def __enter__(self) -> 'Pdf': ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _add_page(self, page: Object, first: bool = ...) -> None: ...
    def _add_page_at(self, arg0: Object, arg1: bool, arg2: Object) -> None: ...
    def _decode_all_streams_and_discard(self) -> None: ...
    def _get_object_id(self, arg0: int, arg1: int) -> Object: ...
    def _process(self, arg0: str, arg1: bytes) -> None: ...
    def _remove_page(self, arg0: Object) -> None: ...
    def _replace_object(self, arg0: Tuple[int, int], arg1: Object) -> None: ...
    def _swap_objects(self, arg0: Tuple[int, int], arg1: Tuple[int, int]) -> None: ...
    def check(self) -> List[str]: ...
    def check_linearization(self, stream: object = ...) -> bool: ...
    def close(self) -> None: ...
    def copy_foreign(self, h: Object) -> Object: ...
    @overload
    def get_object(self, objgen: Tuple[int, int]) -> Object: ...
    @overload
    def get_object(self, objid: int, gen: int) -> Object: ...
    def get_warnings(self) -> list: ...
    @overload
    def make_indirect(self, h: T) -> T: ...
    @overload
    def make_indirect(self, obj: Any) -> Object: ...
    def make_stream(self, data: bytes, d=None, **kwargs) -> Stream: ...
    @classmethod
    def new(cls) -> 'Pdf': ...
    @staticmethod
    def open(
        filename_or_stream: Union[Path, str, BinaryIO],
        *,
        password: Union[str, bytes] = "",
        hex_password: bool = False,
        ignore_xref_streams: bool = False,
        suppress_warnings: bool = True,
        attempt_recovery: bool = True,
        inherit_page_attributes: bool = True,
        access_mode: AccessMode = AccessMode.default,
        allow_overwriting_input: bool = False,
    ) -> 'Pdf': ...
    def open_metadata(
        self,
        set_pikepdf_as_editor: bool = True,
        update_docinfo: bool = True,
        strict: bool = False,
    ) -> PdfMetadata: ...
    def open_outline(self, max_depth: int = 15, strict: bool = False) -> Outline: ...
    def remove_unreferenced_resources(self) -> None: ...
    def save(
        self,
        filename_or_stream: Union[Path, str, BinaryIO, None] = None,
        *,
        static_id: bool = False,
        preserve_pdfa: bool = True,
        min_version: Union[str, Tuple[str, int]] = "",
        force_version: Union[str, Tuple[str, int]] = "",
        fix_metadata_version: bool = True,
        compress_streams: bool = True,
        stream_decode_level: Optional[StreamDecodeLevel] = None,
        object_stream_mode: ObjectStreamMode = ObjectStreamMode.preserve,
        normalize_content: bool = False,
        linearize: bool = False,
        qdf: bool = False,
        progress: Callable[[int], None] = None,
        encryption: Optional[Union[Encryption, bool]] = None,
        recompress_flate: bool = False,
    ) -> None: ...
    def show_xref_table(self) -> None: ...
    @property
    def Root(self) -> Object: ...
    @property
    def _allow_accessibility(self) -> bool: ...
    @property
    def _allow_extract(self) -> bool: ...
    @property
    def _allow_modify_all(self) -> bool: ...
    @property
    def _allow_modify_annotation(self) -> bool: ...
    @property
    def _allow_modify_assembly(self) -> bool: ...
    @property
    def _allow_modify_form(self) -> bool: ...
    @property
    def _allow_modify_other(self) -> bool: ...
    @property
    def _allow_print_highres(self) -> bool: ...
    @property
    def _allow_print_lowres(self) -> bool: ...
    @property
    def _encryption_data(self) -> dict: ...
    @property
    def _pages(self) -> Any: ...
    @property
    def allow(self) -> Permissions: ...
    @property
    def docinfo(self) -> Object: ...
    @docinfo.setter
    def docinfo(self, val: Object) -> None: ...
    @property
    def encryption(self) -> EncryptionInfo: ...
    @property
    def extension_level(self) -> int: ...
    @property
    def filename(self) -> str: ...
    @property
    def is_encrypted(self) -> bool: ...
    @property
    def is_linearized(self) -> bool: ...
    @property
    def objects(self) -> Any: ...
    @property
    def pages(self) -> PageList: ...
    @property
    def pdf_version(self) -> str: ...
    @property
    def root(self) -> Object: ...
    @property
    def trailer(self) -> Object: ...

class Rectangle:
    llx: float = ...
    lly: float = ...
    urx: float = ...
    ury: float = ...
    @overload
    def __init__(self, llx: float, lly: float, urx: float, ury: float) -> None: ...
    @overload
    def __init__(self, a: Array) -> None: ...
    @property
    def width(self) -> float: ...
    @property
    def height(self) -> float: ...
    @property
    def lower_left(self) -> Tuple[float, float]: ...
    @property
    def lower_right(self) -> Tuple[float, float]: ...
    @property
    def upper_left(self) -> Tuple[float, float]: ...
    @property
    def upper_right(self) -> Tuple[float, float]: ...
    def as_array(self) -> 'Array': ...

class NameTreeIterator:
    def __iter__(self) -> 'NameTreeIterator': ...
    def __next__(self) -> Tuple[str, Object]: ...

class NameTree(MutableMapping[Union[str, bytes], Object]):
    def __contains__(self, name: object) -> bool: ...
    def __delitem__(self, name: Union[str, bytes]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __getitem__(self, name: Union[str, bytes]) -> Object: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, name: Union[str, bytes], o: Object) -> None: ...
    def __init__(self, obj: Object, *, auto_repair: bool = ...) -> None: ...
    def _as_map(self) -> _ObjectMapping: ...
    def _contains(self, name: str) -> bool: ...
    def _delitem(self, name: str) -> None: ...
    def _getitem(self, name: str) -> Object: ...
    def _nameval_iter(self) -> NameTreeIterator: ...
    @overload
    def _setitem(self, name: str, obj: Object) -> None: ...
    @overload
    def _setitem(self, name: str, obj: object) -> None: ...
    @property
    def obj(self) -> Object: ...

def _Null() -> Any: ...
def _encode(handle: Any) -> Object: ...
def _new_array(arg0: Iterable) -> Object: ...
def _new_boolean(arg0: bool) -> Object: ...
def _new_dictionary(arg0: dict) -> Object: ...
def _new_integer(arg0: int) -> Object: ...
def _new_name(arg0: str) -> Name: ...
def _new_operator(op: str) -> Object: ...
@overload
def _new_real(arg0: str) -> Object: ...
@overload
def _new_real(value: float, places: int = ...) -> Object: ...
@overload
def _new_real(*args, **kwargs) -> Any: ...
def _new_stream(arg0: Pdf, arg1: bytes) -> Object: ...
def _new_string(s: Union[str, bytes]) -> Object: ...
def _new_string_utf8(s: str) -> Object: ...
def _test_file_not_found(*args, **kwargs) -> Any: ...
def _translate_qpdf(arg0: str) -> str: ...
def get_decimal_precision() -> int: ...
def pdf_doc_to_utf8(pdfdoc: bytes) -> str: ...
def qpdf_version() -> str: ...
def set_access_default_mmap(mmap: bool) -> bool: ...
def set_decimal_precision(prec: int) -> int: ...
def unparse(obj: Any) -> bytes: ...
def utf8_to_pdf_doc(utf8: str, unknown: bytes) -> Tuple[bool, bytes]: ...
def _unparse_content_stream(contentstream: Iterable[Any]) -> bytes: ...
