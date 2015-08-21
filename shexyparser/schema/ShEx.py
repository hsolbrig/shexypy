# ../shexyparser/schema/ShEx.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e868452c6455e6b80cb8bd5f90c308bc5a49c9be
# Generated 2015-08-21 09:18:50.819200 by PyXB version 1.2.4 using Python 3.4.3.final.0
# Namespace http://www.w3.org/shex/

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:df236cf6-47d4-11e5-8f2c-6c40088fdb3a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/shex/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.w3.org/shex/}NodeType
class NodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NodeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 174, 4)
    _Documentation = None
NodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NodeType, enum_prefix=None)
NodeType.IRI = NodeType._CF_enumeration.addEnumeration(unicode_value='IRI', tag='IRI')
NodeType.BNODE = NodeType._CF_enumeration.addEnumeration(unicode_value='BNODE', tag='BNODE')
NodeType.LITERAL = NodeType._CF_enumeration.addEnumeration(unicode_value='LITERAL', tag='LITERAL')
NodeType.NONLITERAL = NodeType._CF_enumeration.addEnumeration(unicode_value='NONLITERAL', tag='NONLITERAL')
NodeType._InitializeFacetMap(NodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NodeType', NodeType)

# Atomic simple type: {http://www.w3.org/shex/}UCASE_LABEL
class UCASE_LABEL (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UCASE_LABEL')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 213, 4)
    _Documentation = None
UCASE_LABEL._CF_pattern = pyxb.binding.facets.CF_pattern()
UCASE_LABEL._CF_pattern.addPattern(pattern='[A-Z_]+')
UCASE_LABEL._InitializeFacetMap(UCASE_LABEL._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UCASE_LABEL', UCASE_LABEL)

# Atomic simple type: {http://www.w3.org/shex/}IRI
class IRI (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IRI')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 352, 4)
    _Documentation = None
IRI._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IRI', IRI)

# Atomic simple type: {http://www.w3.org/shex/}PrefixedName
class PrefixedName (pyxb.binding.datatypes.QName):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PrefixedName')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 356, 4)
    _Documentation = None
PrefixedName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PrefixedName', PrefixedName)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 367, 20)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 370, 20)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.unbounded = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='unbounded', tag='unbounded')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {http://www.w3.org/shex/}ShapeLabel
class ShapeLabel (IRI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShapeLabel')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 316, 4)
    _Documentation = None
ShapeLabel._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ShapeLabel', ShapeLabel)

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 365, 12)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2)
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2.unbounded = 'unbounded'                # originally STD_ANON_.unbounded
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration,
   STD_ANON_2._CF_pattern)

# Complex type {http://www.w3.org/shex/}SemanticAction with content type MIXED
class SemanticAction (pyxb.binding.basis.complexTypeDefinition):
    """A "semantic action" with an optional name """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SemanticAction')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 192, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}codeLabel uses Python identifier codeLabel
    __codeLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codeLabel'), 'codeLabel', '__httpwww_w3_orgshex_SemanticAction_httpwww_w3_orgshexcodeLabel', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 197, 12), )

    
    codeLabel = property(__codeLabel.value, __codeLabel.set, None, None)

    
    # Element {http://www.w3.org/shex/}codeDecl uses Python identifier codeDecl
    __codeDecl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codeDecl'), 'codeDecl', '__httpwww_w3_orgshex_SemanticAction_httpwww_w3_orgshexcodeDecl', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 198, 12), )

    
    codeDecl = property(__codeDecl.value, __codeDecl.set, None, None)

    _ElementMap.update({
        __codeLabel.name() : __codeLabel,
        __codeDecl.name() : __codeDecl
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SemanticAction', SemanticAction)


# Complex type {http://www.w3.org/shex/}CodeDecl with content type MIXED
class CodeDecl (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}CodeDecl with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeDecl')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 202, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iri uses Python identifier iri
    __iri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iri'), 'iri', '__httpwww_w3_orgshex_CodeDecl_iri', pyxb.binding.datatypes.QName)
    __iri._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 206, 8)
    __iri._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 206, 8)
    
    iri = property(__iri.value, __iri.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iri.name() : __iri
    })
Namespace.addCategoryObject('typeBinding', 'CodeDecl', CodeDecl)


# Complex type {http://www.w3.org/shex/}SemanticActions with content type ELEMENT_ONLY
class SemanticActions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}SemanticActions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SemanticActions')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 219, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'action'), 'action', '__httpwww_w3_orgshex_SemanticActions_httpwww_w3_orgshexaction', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 221, 12), )

    
    action = property(__action.value, __action.set, None, None)

    _ElementMap.update({
        __action.name() : __action
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SemanticActions', SemanticActions)


# Complex type {http://www.w3.org/shex/}ValueClass with content type ELEMENT_ONLY
class ValueClass (pyxb.binding.basis.complexTypeDefinition):
    """Represents literal, iri, bnode and non-literal facets as well as multiple group shape and non
            simple value sets"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueClass')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 227, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexfacet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 233, 12), )

    
    facet = property(__facet.value, __facet.set, None, None)

    
    # Element {http://www.w3.org/shex/}groupShapeConstr uses Python identifier groupShapeConstr
    __groupShapeConstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr'), 'groupShapeConstr', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexgroupShapeConstr', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 234, 12), )

    
    groupShapeConstr = property(__groupShapeConstr.value, __groupShapeConstr.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueSet uses Python identifier valueSet
    __valueSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), 'valueSet', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexvalueSet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 235, 12), )

    
    valueSet = property(__valueSet.value, __valueSet.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueSetReference uses Python identifier valueSetReference
    __valueSetReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueSetReference'), 'valueSetReference', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexvalueSetReference', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 236, 12), )

    
    valueSetReference = property(__valueSetReference.value, __valueSetReference.set, None, None)

    _ElementMap.update({
        __facet.name() : __facet,
        __groupShapeConstr.name() : __groupShapeConstr,
        __valueSet.name() : __valueSet,
        __valueSetReference.name() : __valueSetReference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueClass', ValueClass)


# Complex type {http://www.w3.org/shex/}GroupShapeConstr with content type ELEMENT_ONLY
class GroupShapeConstr (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}GroupShapeConstr with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroupShapeConstr')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 240, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}groupShapeConstr uses Python identifier groupShapeConstr
    __groupShapeConstr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr'), 'groupShapeConstr', '__httpwww_w3_orgshex_GroupShapeConstr_httpwww_w3_orgshexgroupShapeConstr', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 242, 12), )

    
    groupShapeConstr = property(__groupShapeConstr.value, __groupShapeConstr.set, None, None)

    
    # Element {http://www.w3.org/shex/}stringFacet uses Python identifier stringFacet
    __stringFacet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stringFacet'), 'stringFacet', '__httpwww_w3_orgshex_GroupShapeConstr_httpwww_w3_orgshexstringFacet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 243, 12), )

    
    stringFacet = property(__stringFacet.value, __stringFacet.set, None, None)

    _ElementMap.update({
        __groupShapeConstr.name() : __groupShapeConstr,
        __stringFacet.name() : __stringFacet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GroupShapeConstr', GroupShapeConstr)


# Complex type {http://www.w3.org/shex/}XSFacet with content type ELEMENT_ONLY
class XSFacet (pyxb.binding.basis.complexTypeDefinition):
    """Union of StringFacet and NumericFacet"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'XSFacet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pattern'), 'pattern', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexpattern', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 263, 12), )

    
    pattern = property(__pattern.value, __pattern.set, None, None)

    
    # Element {http://www.w3.org/shex/}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexnot', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 264, 12), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {http://www.w3.org/shex/}minLength uses Python identifier minLength
    __minLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minLength'), 'minLength', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexminLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 265, 12), )

    
    minLength = property(__minLength.value, __minLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), 'maxLength', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexmaxLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 266, 12), )

    
    maxLength = property(__maxLength.value, __maxLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexlength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 267, 12), )

    
    length = property(__length.value, __length.set, None, None)

    
    # Element {http://www.w3.org/shex/}minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minValue'), 'minValue', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexminValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 268, 12), )

    
    minValue = property(__minValue.value, __minValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxValue uses Python identifier maxValue
    __maxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), 'maxValue', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexmaxValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12), )

    
    maxValue = property(__maxValue.value, __maxValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}totalDigits uses Python identifier totalDigits
    __totalDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), 'totalDigits', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshextotalDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 270, 12), )

    
    totalDigits = property(__totalDigits.value, __totalDigits.set, None, None)

    
    # Element {http://www.w3.org/shex/}fractionDigits uses Python identifier fractionDigits
    __fractionDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), 'fractionDigits', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexfractionDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 271, 12), )

    
    fractionDigits = property(__fractionDigits.value, __fractionDigits.set, None, None)

    _ElementMap.update({
        __pattern.name() : __pattern,
        __not.name() : __not,
        __minLength.name() : __minLength,
        __maxLength.name() : __maxLength,
        __length.name() : __length,
        __minValue.name() : __minValue,
        __maxValue.name() : __maxValue,
        __totalDigits.name() : __totalDigits,
        __fractionDigits.name() : __fractionDigits
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'XSFacet', XSFacet)


# Complex type {http://www.w3.org/shex/}Range with content type SIMPLE
class Range (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}Range with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.int
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Range')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 275, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute open uses Python identifier open
    __open = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'open'), 'open', '__httpwww_w3_orgshex_Range_open', pyxb.binding.datatypes.boolean, unicode_default='false')
    __open._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 278, 16)
    __open._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 278, 16)
    
    open = property(__open.value, __open.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __open.name() : __open
    })
Namespace.addCategoryObject('typeBinding', 'Range', Range)


# Complex type {http://www.w3.org/shex/}StringFacet with content type ELEMENT_ONLY
class StringFacet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}StringFacet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StringFacet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 283, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pattern'), 'pattern', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexpattern', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 285, 12), )

    
    pattern = property(__pattern.value, __pattern.set, None, None)

    
    # Element {http://www.w3.org/shex/}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexnot', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 286, 12), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {http://www.w3.org/shex/}minLength uses Python identifier minLength
    __minLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minLength'), 'minLength', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexminLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 287, 12), )

    
    minLength = property(__minLength.value, __minLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), 'maxLength', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexmaxLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 288, 12), )

    
    maxLength = property(__maxLength.value, __maxLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexlength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 289, 12), )

    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        __pattern.name() : __pattern,
        __not.name() : __not,
        __minLength.name() : __minLength,
        __maxLength.name() : __maxLength,
        __length.name() : __length
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'StringFacet', StringFacet)


# Complex type {http://www.w3.org/shex/}NumericFacet with content type ELEMENT_ONLY
class NumericFacet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}NumericFacet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumericFacet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 293, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minValue'), 'minValue', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexminValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 295, 12), )

    
    minValue = property(__minValue.value, __minValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxValue uses Python identifier maxValue
    __maxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), 'maxValue', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexmaxValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 296, 12), )

    
    maxValue = property(__maxValue.value, __maxValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}totalDigits uses Python identifier totalDigits
    __totalDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), 'totalDigits', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshextotalDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 297, 12), )

    
    totalDigits = property(__totalDigits.value, __totalDigits.set, None, None)

    
    # Element {http://www.w3.org/shex/}fractionDigits uses Python identifier fractionDigits
    __fractionDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), 'fractionDigits', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexfractionDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 298, 12), )

    
    fractionDigits = property(__fractionDigits.value, __fractionDigits.set, None, None)

    _ElementMap.update({
        __minValue.name() : __minValue,
        __maxValue.name() : __maxValue,
        __totalDigits.name() : __totalDigits,
        __fractionDigits.name() : __fractionDigits
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'NumericFacet', NumericFacet)


# Complex type {http://www.w3.org/shex/}ValueSet with content type ELEMENT_ONLY
class ValueSet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}ValueSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 305, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}iriRange uses Python identifier iriRange
    __iriRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iriRange'), 'iriRange', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexiriRange', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 307, 12), )

    
    iriRange = property(__iriRange.value, __iriRange.set, None, None)

    
    # Element {http://www.w3.org/shex/}rdfLiteral uses Python identifier rdfLiteral
    __rdfLiteral = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral'), 'rdfLiteral', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexrdfLiteral', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 308, 12), )

    
    rdfLiteral = property(__rdfLiteral.value, __rdfLiteral.set, None, None)

    
    # Element {http://www.w3.org/shex/}integer uses Python identifier integer
    __integer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'integer'), 'integer', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexinteger', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 309, 12), )

    
    integer = property(__integer.value, __integer.set, None, None)

    
    # Element {http://www.w3.org/shex/}decimal uses Python identifier decimal
    __decimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'decimal'), 'decimal', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexdecimal', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 310, 12), )

    
    decimal = property(__decimal.value, __decimal.set, None, None)

    
    # Element {http://www.w3.org/shex/}double uses Python identifier double
    __double = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'double'), 'double', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexdouble', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 311, 12), )

    
    double = property(__double.value, __double.set, None, None)

    
    # Element {http://www.w3.org/shex/}boolean uses Python identifier boolean
    __boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boolean'), 'boolean', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexboolean', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 312, 12), )

    
    boolean = property(__boolean.value, __boolean.set, None, None)

    _ElementMap.update({
        __iriRange.name() : __iriRange,
        __rdfLiteral.name() : __rdfLiteral,
        __integer.name() : __integer,
        __decimal.name() : __decimal,
        __double.name() : __double,
        __boolean.name() : __boolean
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueSet', ValueSet)


# Complex type {http://www.w3.org/shex/}IncludeProperty with content type EMPTY
class IncludeProperty (pyxb.binding.basis.complexTypeDefinition):
    """For valid typing.  A property that may be present in a graph that is not defined by a given shape."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncludeProperty')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 88, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IncludeProperty_ref', IRI, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 92, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 92, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'IncludeProperty', IncludeProperty)


# Complex type {http://www.w3.org/shex/}Annotation with content type ELEMENT_ONLY
class Annotation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}Annotation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Annotation')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 183, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}iriref uses Python identifier iriref
    __iriref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iriref'), 'iriref', '__httpwww_w3_orgshex_Annotation_httpwww_w3_orgshexiriref', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 185, 12), )

    
    iriref = property(__iriref.value, __iriref.set, None, None)

    
    # Element {http://www.w3.org/shex/}literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'literal'), 'literal', '__httpwww_w3_orgshex_Annotation_httpwww_w3_orgshexliteral', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 186, 12), )

    
    literal = property(__literal.value, __literal.set, None, None)

    
    # Attribute iri uses Python identifier iri
    __iri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iri'), 'iri', '__httpwww_w3_orgshex_Annotation_iri', IRI)
    __iri._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 188, 8)
    __iri._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 188, 8)
    
    iri = property(__iri.value, __iri.set, None, None)

    _ElementMap.update({
        __iriref.name() : __iriref,
        __literal.name() : __literal
    })
    _AttributeMap.update({
        __iri.name() : __iri
    })
Namespace.addCategoryObject('typeBinding', 'Annotation', Annotation)


# Complex type {http://www.w3.org/shex/}CodeLabel with content type EMPTY
class CodeLabel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}CodeLabel with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeLabel')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 209, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_CodeLabel_ref', UCASE_LABEL, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 210, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 210, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'CodeLabel', CodeLabel)


# Complex type {http://www.w3.org/shex/}IRIRef with content type EMPTY
class IRIRef (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}IRIRef with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IRIRef')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 247, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IRIRef_ref', IRI, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 248, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 248, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'IRIRef', IRIRef)


# Complex type {http://www.w3.org/shex/}IRIStem with content type EMPTY
class IRIStem (pyxb.binding.basis.complexTypeDefinition):
    """A set of IRIs. If  is , the set contains one member. If  is  then it references the set of 
                IRIs that begin with the referenced IRI"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IRIStem')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 320, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'base'), 'base', '__httpwww_w3_orgshex_IRIStem_base', IRI)
    __base._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 325, 8)
    __base._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 325, 8)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute stem uses Python identifier stem
    __stem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stem'), 'stem', '__httpwww_w3_orgshex_IRIStem_stem', pyxb.binding.datatypes.boolean, unicode_default='false')
    __stem._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 326, 8)
    __stem._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 326, 8)
    
    stem = property(__stem.value, __stem.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __base.name() : __base,
        __stem.name() : __stem
    })
Namespace.addCategoryObject('typeBinding', 'IRIStem', IRIStem)


# Complex type {http://www.w3.org/shex/}RDFLiteral with content type SIMPLE
class RDFLiteral (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}RDFLiteral with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RDFLiteral')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 343, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datatype'), 'datatype', '__httpwww_w3_orgshex_RDFLiteral_datatype', IRI)
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 346, 16)
    __datatype._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 346, 16)
    
    datatype = property(__datatype.value, __datatype.set, None, None)

    
    # Attribute langtag uses Python identifier langtag
    __langtag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'langtag'), 'langtag', '__httpwww_w3_orgshex_RDFLiteral_langtag', pyxb.binding.datatypes.string)
    __langtag._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 347, 16)
    __langtag._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 347, 16)
    
    langtag = property(__langtag.value, __langtag.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __datatype.name() : __datatype,
        __langtag.name() : __langtag
    })
Namespace.addCategoryObject('typeBinding', 'RDFLiteral', RDFLiteral)


# Complex type {http://www.w3.org/shex/}Schema with content type ELEMENT_ONLY
class Schema_ (pyxb.binding.basis.complexTypeDefinition):
    """A shape definition document"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Schema')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}startActions uses Python identifier startActions
    __startActions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startActions'), 'startActions', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexstartActions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 21, 12), )

    
    startActions = property(__startActions.value, __startActions.set, None, 'A set of semantic actions to be invoked  the shape is evaluated')

    
    # Element {http://www.w3.org/shex/}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shape'), 'shape', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexshape', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 26, 12), )

    
    shape = property(__shape.value, __shape.set, None, 'An unordered list of shape definitions')

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__httpwww_w3_orgshex_Schema__start', ShapeLabel)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 32, 8)
    __start._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 32, 8)
    
    start = property(__start.value, __start.set, None, 'The initial shape (entry point) in the definition.  If absent, the start shape must be supplied by the application')

    
    # Attribute exclude-prefixes uses Python identifier exclude_prefixes
    __exclude_prefixes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exclude-prefixes'), 'exclude_prefixes', '__httpwww_w3_orgshex_Schema__exclude_prefixes', pyxb.binding.datatypes.string)
    __exclude_prefixes._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 37, 8)
    __exclude_prefixes._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 37, 8)
    
    exclude_prefixes = property(__exclude_prefixes.value, __exclude_prefixes.set, None, 'A space separated list of namespaces to be excluded from the target ShEx document')

    
    # Attribute default-namespace uses Python identifier default_namespace
    __default_namespace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default-namespace'), 'default_namespace', '__httpwww_w3_orgshex_Schema__default_namespace', pyxb.binding.datatypes.anyURI)
    __default_namespace._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 42, 8)
    __default_namespace._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 42, 8)
    
    default_namespace = property(__default_namespace.value, __default_namespace.set, None, "The URI of the default ShEx namespace, if any.  Corresponds to the ShEx ':' namespace")

    _ElementMap.update({
        __startActions.name() : __startActions,
        __shape.name() : __shape
    })
    _AttributeMap.update({
        __start.name() : __start,
        __exclude_prefixes.name() : __exclude_prefixes,
        __default_namespace.name() : __default_namespace
    })
Namespace.addCategoryObject('typeBinding', 'Schema', Schema_)


# Complex type {http://www.w3.org/shex/}Shape with content type MIXED
class Shape (pyxb.binding.basis.complexTypeDefinition):
    """A labeled definition of an RDF shape."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Shape')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}extra uses Python identifier extra
    __extra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extra'), 'extra', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexextra', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 57, 12), )

    
    extra = property(__extra.value, __extra.set, None, 'The set of properties included with the shape definition.  Must be empty if  is true.')

    
    # Element {http://www.w3.org/shex/}tripleConstraint uses Python identifier tripleConstraint
    __tripleConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), 'tripleConstraint', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshextripleConstraint', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16), )

    
    tripleConstraint = property(__tripleConstraint.value, __tripleConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}oneOf uses Python identifier oneOf
    __oneOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oneOf'), 'oneOf', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexoneOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16), )

    
    oneOf = property(__oneOf.value, __oneOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}someOf uses Python identifier someOf
    __someOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'someOf'), 'someOf', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexsomeOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16), )

    
    someOf = property(__someOf.value, __someOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://www.w3.org/shex/}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexinclude', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.w3.org/shex/}semanticActions uses Python identifier semanticActions
    __semanticActions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), 'semanticActions', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexsemanticActions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12), )

    
    semanticActions = property(__semanticActions.value, __semanticActions.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httpwww_w3_orgshex_Shape_label', ShapeLabel, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 63, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 63, 8)
    
    label = property(__label.value, __label.set, None, "The name of the shape.  The local name of an anonymous shape begins with an underscore ('_') (i.e. it is a blank node")

    
    # Attribute virtual uses Python identifier virtual
    __virtual = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'virtual'), 'virtual', '__httpwww_w3_orgshex_Shape_virtual', pyxb.binding.datatypes.boolean, unicode_default='false')
    __virtual._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 68, 8)
    __virtual._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 68, 8)
    
    virtual = property(__virtual.value, __virtual.set, None, 'If true, this shape cannot be applied directly and may only be included in another shape definition.')

    
    # Attribute closed uses Python identifier closed
    __closed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'closed'), 'closed', '__httpwww_w3_orgshex_Shape_closed', pyxb.binding.datatypes.boolean, unicode_default='false')
    __closed._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 73, 8)
    __closed._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 73, 8)
    
    closed = property(__closed.value, __closed.set, None, 'If true, this shape definition is "strict", in the sense that  of the triples in the graph must match the\n                shape definition.  If false, graphs that  the matching shape definition are considered passing. ')

    _ElementMap.update({
        __extra.name() : __extra,
        __tripleConstraint.name() : __tripleConstraint,
        __oneOf.name() : __oneOf,
        __someOf.name() : __someOf,
        __group.name() : __group,
        __include.name() : __include,
        __semanticActions.name() : __semanticActions
    })
    _AttributeMap.update({
        __label.name() : __label,
        __virtual.name() : __virtual,
        __closed.name() : __closed
    })
Namespace.addCategoryObject('typeBinding', 'Shape', Shape)


# Complex type {http://www.w3.org/shex/}IncludeShape with content type EMPTY
class IncludeShape (pyxb.binding.basis.complexTypeDefinition):
    """A reference to an external or internal shape definition that is considered to be part of this shape definition."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncludeShape')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 81, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IncludeShape_ref', ShapeLabel, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 85, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 85, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'IncludeShape', IncludeShape)


# Complex type {http://www.w3.org/shex/}ShapeConstraint with content type ELEMENT_ONLY
class ShapeConstraint (pyxb.binding.basis.complexTypeDefinition):
    """A complete shape constraint."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShapeConstraint')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 108, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}tripleConstraint uses Python identifier tripleConstraint
    __tripleConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), 'tripleConstraint', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshextripleConstraint', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16), )

    
    tripleConstraint = property(__tripleConstraint.value, __tripleConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}oneOf uses Python identifier oneOf
    __oneOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'oneOf'), 'oneOf', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexoneOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16), )

    
    oneOf = property(__oneOf.value, __oneOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}someOf uses Python identifier someOf
    __someOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'someOf'), 'someOf', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexsomeOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16), )

    
    someOf = property(__someOf.value, __someOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://www.w3.org/shex/}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexinclude', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.w3.org/shex/}semanticActions uses Python identifier semanticActions
    __semanticActions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), 'semanticActions', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexsemanticActions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12), )

    
    semanticActions = property(__semanticActions.value, __semanticActions.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httpwww_w3_orgshex_ShapeConstraint_label', ShapeLabel)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 116, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 116, 8)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_orgshex_ShapeConstraint_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 363, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 363, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_orgshex_ShapeConstraint_max', STD_ANON_2, unicode_default='1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 364, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 364, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __tripleConstraint.name() : __tripleConstraint,
        __oneOf.name() : __oneOf,
        __someOf.name() : __someOf,
        __group.name() : __group,
        __include.name() : __include,
        __semanticActions.name() : __semanticActions
    })
    _AttributeMap.update({
        __label.name() : __label,
        __min.name() : __min,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', 'ShapeConstraint', ShapeConstraint)


# Complex type {http://www.w3.org/shex/}TripleConstraint with content type ELEMENT_ONLY
class TripleConstraint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}TripleConstraint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TripleConstraint')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 119, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}objectConstraint uses Python identifier objectConstraint
    __objectConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint'), 'objectConstraint', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexobjectConstraint', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 123, 16), )

    
    objectConstraint = property(__objectConstraint.value, __objectConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}subjectConstraint uses Python identifier subjectConstraint
    __subjectConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint'), 'subjectConstraint', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexsubjectConstraint', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 124, 16), )

    
    subjectConstraint = property(__subjectConstraint.value, __subjectConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexannotation', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 126, 12), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://www.w3.org/shex/}semanticActions uses Python identifier semanticActions
    __semanticActions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), 'semanticActions', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexsemanticActions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 127, 12), )

    
    semanticActions = property(__semanticActions.value, __semanticActions.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httpwww_w3_orgshex_TripleConstraint_label', ShapeLabel)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 130, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 130, 8)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute predicate uses Python identifier predicate
    __predicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'predicate'), 'predicate', '__httpwww_w3_orgshex_TripleConstraint_predicate', IRI, required=True)
    __predicate._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 8)
    __predicate._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 8)
    
    predicate = property(__predicate.value, __predicate.set, None, None)

    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'object'), 'object', '__httpwww_w3_orgshex_TripleConstraint_object', IRI)
    __object._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 8)
    __object._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 8)
    
    object = property(__object.value, __object.set, None, 'A simple object IRI.  Equivalent to a single, non-stemmed value set in the object position.')

    
    # Attribute objectShape uses Python identifier objectShape
    __objectShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'objectShape'), 'objectShape', '__httpwww_w3_orgshex_TripleConstraint_objectShape', ShapeLabel)
    __objectShape._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 137, 8)
    __objectShape._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 137, 8)
    
    objectShape = property(__objectShape.value, __objectShape.set, None, 'A reference to a shape.  Used with a single groupShapeConstrin the object position.')

    
    # Attribute subject uses Python identifier subject
    __subject = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subject'), 'subject', '__httpwww_w3_orgshex_TripleConstraint_subject', IRI)
    __subject._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 142, 8)
    __subject._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 142, 8)
    
    subject = property(__subject.value, __subject.set, None, 'A simple subject IRI.  Used for a single, non-stemmed value set in the subject position.')

    
    # Attribute subjectShape uses Python identifier subjectShape
    __subjectShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subjectShape'), 'subjectShape', '__httpwww_w3_orgshex_TripleConstraint_subjectShape', ShapeLabel)
    __subjectShape._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 147, 8)
    __subjectShape._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 147, 8)
    
    subjectShape = property(__subjectShape.value, __subjectShape.set, None, 'A reference to a shape.  Used with a single groupShapeConstr in the subject position.')

    
    # Attribute negated uses Python identifier negated
    __negated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negated'), 'negated', '__httpwww_w3_orgshex_TripleConstraint_negated', pyxb.binding.datatypes.boolean, unicode_default='false')
    __negated._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 8)
    __negated._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 8)
    
    negated = property(__negated.value, __negated.set, None, 'True means that the match is NOT what is in the constraint')

    
    # Attribute datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datatype'), 'datatype', '__httpwww_w3_orgshex_TripleConstraint_datatype', pyxb.binding.datatypes.anyURI)
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 157, 8)
    __datatype._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 157, 8)
    
    datatype = property(__datatype.value, __datatype.set, None, 'The URI of a datatype. Used for a single datatype in the object position, with or without facets')

    
    # Attribute objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'objectType'), 'objectType', '__httpwww_w3_orgshex_TripleConstraint_objectType', NodeType)
    __objectType._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 162, 8)
    __objectType._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 162, 8)
    
    objectType = property(__objectType.value, __objectType.set, None, 'A constraint on the type of object.')

    
    # Attribute subjectType uses Python identifier subjectType
    __subjectType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subjectType'), 'subjectType', '__httpwww_w3_orgshex_TripleConstraint_subjectType', NodeType)
    __subjectType._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 167, 8)
    __subjectType._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 167, 8)
    
    subjectType = property(__subjectType.value, __subjectType.set, None, 'A constraint on the type of subject')

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_orgshex_TripleConstraint_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 363, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 363, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_orgshex_TripleConstraint_max', STD_ANON_2, unicode_default='1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 364, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 364, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __objectConstraint.name() : __objectConstraint,
        __subjectConstraint.name() : __subjectConstraint,
        __annotation.name() : __annotation,
        __semanticActions.name() : __semanticActions
    })
    _AttributeMap.update({
        __label.name() : __label,
        __predicate.name() : __predicate,
        __object.name() : __object,
        __objectShape.name() : __objectShape,
        __subject.name() : __subject,
        __subjectShape.name() : __subjectShape,
        __negated.name() : __negated,
        __datatype.name() : __datatype,
        __objectType.name() : __objectType,
        __subjectType.name() : __subjectType,
        __min.name() : __min,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', 'TripleConstraint', TripleConstraint)


# Complex type {http://www.w3.org/shex/}ShapeRef with content type EMPTY
class ShapeRef (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}ShapeRef with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShapeRef')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 251, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_ShapeRef_ref', ShapeLabel, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 252, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 252, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'ShapeRef', ShapeRef)


# Complex type {http://www.w3.org/shex/}IRIRange with content type ELEMENT_ONLY
class IRIRange (IRIStem):
    """A set of IRI's that ar defined by a base  and collection of IRI sets that are excluded from the base. If the base is absent,  IRI serves as
                the base"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IRIRange')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 329, 4)
    _ElementMap = IRIStem._ElementMap.copy()
    _AttributeMap = IRIStem._AttributeMap.copy()
    # Base type is IRIStem
    
    # Element {http://www.w3.org/shex/}exclusion uses Python identifier exclusion
    __exclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusion'), 'exclusion', '__httpwww_w3_orgshex_IRIRange_httpwww_w3_orgshexexclusion', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 20), )

    
    exclusion = property(__exclusion.value, __exclusion.set, None, None)

    
    # Attribute base inherited from {http://www.w3.org/shex/}IRIStem
    
    # Attribute stem inherited from {http://www.w3.org/shex/}IRIStem
    _ElementMap.update({
        __exclusion.name() : __exclusion
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IRIRange', IRIRange)


Schema = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Schema'), Schema_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', Schema.name().localName(), Schema)



SemanticAction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codeLabel'), CodeLabel, scope=SemanticAction, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 197, 12)))

SemanticAction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codeDecl'), CodeDecl, scope=SemanticAction, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 198, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticAction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codeLabel')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 197, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticAction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codeDecl')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 198, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SemanticAction._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 204, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 204, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CodeDecl._Automaton = _BuildAutomaton_()




SemanticActions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'action'), SemanticAction, scope=SemanticActions, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 221, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticActions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'action')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 221, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SemanticActions._Automaton = _BuildAutomaton_2()




ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), XSFacet, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 233, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr'), GroupShapeConstr, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 234, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), ValueSet, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 235, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueSetReference'), IRIRef, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 236, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 233, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 234, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueSet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 235, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueSetReference')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 236, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueClass._Automaton = _BuildAutomaton_3()




GroupShapeConstr._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr'), ShapeRef, scope=GroupShapeConstr, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 242, 12)))

GroupShapeConstr._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stringFacet'), StringFacet, scope=GroupShapeConstr, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 243, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 242, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 243, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroupShapeConstr._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupShapeConstr')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 242, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroupShapeConstr._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stringFacet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 243, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GroupShapeConstr._Automaton = _BuildAutomaton_4()




XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pattern'), pyxb.binding.datatypes.string, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 263, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), pyxb.binding.datatypes.string, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 264, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minLength'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 265, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 266, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 267, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minValue'), Range, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 268, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), Range, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 270, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 271, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pattern')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 263, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 264, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 265, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 266, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 267, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 268, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 270, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 271, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
XSFacet._Automaton = _BuildAutomaton_5()




StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pattern'), pyxb.binding.datatypes.string, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 285, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), pyxb.binding.datatypes.string, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 286, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minLength'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 287, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 288, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 289, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pattern')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 285, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 286, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 287, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 288, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 289, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StringFacet._Automaton = _BuildAutomaton_6()




NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minValue'), Range, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 295, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), Range, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 296, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), pyxb.binding.datatypes.int, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 297, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), pyxb.binding.datatypes.int, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 298, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 295, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 296, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 297, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 298, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NumericFacet._Automaton = _BuildAutomaton_7()




ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iriRange'), IRIRange, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 307, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral'), RDFLiteral, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 308, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'integer'), pyxb.binding.datatypes.int, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 309, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'decimal'), pyxb.binding.datatypes.decimal, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 310, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'double'), pyxb.binding.datatypes.double, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 311, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boolean'), pyxb.binding.datatypes.boolean, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 312, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iriRange')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 307, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 308, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'integer')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 309, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'decimal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 310, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'double')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 311, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boolean')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 312, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueSet._Automaton = _BuildAutomaton_8()




Annotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iriref'), IRI, scope=Annotation, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 185, 12)))

Annotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'literal'), RDFLiteral, scope=Annotation, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 186, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Annotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iriref')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 185, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Annotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'literal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 186, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Annotation._Automaton = _BuildAutomaton_9()




Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startActions'), SemanticActions, scope=Schema_, documentation='A set of semantic actions to be invoked  the shape is evaluated', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 21, 12)))

Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shape'), Shape, scope=Schema_, documentation='An unordered list of shape definitions', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 26, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 21, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 26, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startActions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shape')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 26, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Schema_._Automaton = _BuildAutomaton_10()




Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extra'), IncludeProperty, scope=Shape, documentation='The set of properties included with the shape definition.  Must be empty if  is true.', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 57, 12)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), TripleConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oneOf'), ShapeConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'someOf'), ShapeConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), ShapeConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), IncludeShape, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), SemanticActions, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 56, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 57, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oneOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'someOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semanticActions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extra')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 57, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Shape._Automaton = _BuildAutomaton_11()




ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), TripleConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'oneOf'), ShapeConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'someOf'), ShapeConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), ShapeConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), IncludeShape, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), SemanticActions, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 98, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'oneOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'someOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 101, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 102, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semanticActions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 104, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShapeConstraint._Automaton = _BuildAutomaton_12()




TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint'), ValueClass, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 123, 16)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint'), ValueClass, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 124, 16)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), Annotation, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 126, 12)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'semanticActions'), SemanticActions, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 127, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 122, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 126, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 127, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 123, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 124, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 126, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'semanticActions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 127, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TripleConstraint._Automaton = _BuildAutomaton_13()




IRIRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusion'), IRIStem, scope=IRIRange, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 20)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IRIRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusion')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IRIRange._Automaton = _BuildAutomaton_14()

