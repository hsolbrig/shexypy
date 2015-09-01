# ../shexypy/schema/ShEx.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e868452c6455e6b80cb8bd5f90c308bc5a49c9be
# Generated 2015-09-01 17:11:18.692238 by PyXB version 1.2.4 using Python 3.4.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5eb3921e-50f6-11e5-b2b3-6c40088fdb3a')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 235, 4)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 310, 4)
    _Documentation = None
UCASE_LABEL._CF_pattern = pyxb.binding.facets.CF_pattern()
UCASE_LABEL._CF_pattern.addPattern(pattern='[A-Z0-9_]+')
UCASE_LABEL._InitializeFacetMap(UCASE_LABEL._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UCASE_LABEL', UCASE_LABEL)

# Atomic simple type: {http://www.w3.org/shex/}IRI
class IRI (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IRI')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 460, 4)
    _Documentation = None
IRI._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IRI', IRI)

# Atomic simple type: {http://www.w3.org/shex/}PrefixedName
class PrefixedName (pyxb.binding.datatypes.QName):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PrefixedName')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 464, 4)
    _Documentation = None
PrefixedName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PrefixedName', PrefixedName)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 475, 20)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 478, 20)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.unbounded = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='unbounded', tag='unbounded')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {http://www.w3.org/shex/}ShapeLabel
class ShapeLabel (IRI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShapeLabel')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 424, 4)
    _Documentation = None
ShapeLabel._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ShapeLabel', ShapeLabel)

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 473, 12)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2)
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2.unbounded = 'unbounded'                # originally STD_ANON_.unbounded
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration,
   STD_ANON_2._CF_pattern)

# Complex type {http://www.w3.org/shex/}SemanticActions with content type ELEMENT_ONLY
class SemanticActions (pyxb.binding.basis.complexTypeDefinition):
    """An ordered list of semantic actions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SemanticActions')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 255, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'action'), 'action', '__httpwww_w3_orgshex_SemanticActions_httpwww_w3_orgshexaction', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 260, 12), )

    
    action = property(__action.value, __action.set, None, None)

    _ElementMap.update({
        __action.name() : __action
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SemanticActions', SemanticActions)


# Complex type {http://www.w3.org/shex/}SemanticAction with content type ELEMENT_ONLY
class SemanticAction (pyxb.binding.basis.complexTypeDefinition):
    """A semantic action"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SemanticAction')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 264, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}codeLabel uses Python identifier codeLabel
    __codeLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codeLabel'), 'codeLabel', '__httpwww_w3_orgshex_SemanticAction_httpwww_w3_orgshexcodeLabel', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12), )

    
    codeLabel = property(__codeLabel.value, __codeLabel.set, None, 'The name of a function that will be bound when the shape is evaluated')

    
    # Element {http://www.w3.org/shex/}codeDecl uses Python identifier codeDecl
    __codeDecl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codeDecl'), 'codeDecl', '__httpwww_w3_orgshex_SemanticAction_httpwww_w3_orgshexcodeDecl', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 274, 12), )

    
    codeDecl = property(__codeDecl.value, __codeDecl.set, None, 'The language specific function to be invoked')

    
    # Attribute validating uses Python identifier validating
    __validating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'validating'), 'validating', '__httpwww_w3_orgshex_SemanticAction_validating', pyxb.binding.datatypes.boolean, unicode_default='false')
    __validating._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 280, 8)
    __validating._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 280, 8)
    
    validating = property(__validating.value, __validating.set, None, 'If , the action returns a boolean value that determines whether the triples being being evalueated pass or fail. If , the action is involked\n                    strictly for side effects. A validating semantic action may be called any number of times for a given shape and in any order. A non-validating action will be called at most once\n                    and in a pre-established order with respect to other actions.')

    _ElementMap.update({
        __codeLabel.name() : __codeLabel,
        __codeDecl.name() : __codeDecl
    })
    _AttributeMap.update({
        __validating.name() : __validating
    })
Namespace.addCategoryObject('typeBinding', 'SemanticAction', SemanticAction)


# Complex type {http://www.w3.org/shex/}CodeDecl with content type MIXED
class CodeDecl (pyxb.binding.basis.complexTypeDefinition):
    """An arbitrary block of code that is evaluated in terms of the action/language set identified by the reference """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeDecl')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 289, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute iri uses Python identifier iri
    __iri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iri'), 'iri', '__httpwww_w3_orgshex_CodeDecl_iri', pyxb.binding.datatypes.anyURI)
    __iri._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 296, 8)
    __iri._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 296, 8)
    
    iri = property(__iri.value, __iri.set, None, 'An IRI that identifies the specific process to be used')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __iri.name() : __iri
    })
Namespace.addCategoryObject('typeBinding', 'CodeDecl', CodeDecl)


# Complex type {http://www.w3.org/shex/}ValueClass with content type ELEMENT_ONLY
class ValueClass (pyxb.binding.basis.complexTypeDefinition):
    """Represents literal, iri, bnode and non-literal facets as well as multiple group shape and non simple value sets"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueClass')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 319, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexfacet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 324, 12), )

    
    facet = property(__facet.value, __facet.set, None, None)

    
    # Element {http://www.w3.org/shex/}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexor', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 325, 12), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueSet uses Python identifier valueSet
    __valueSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), 'valueSet', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexvalueSet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 326, 12), )

    
    valueSet = property(__valueSet.value, __valueSet.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueClassLabel uses Python identifier valueClassLabel
    __valueClassLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel'), 'valueClassLabel', '__httpwww_w3_orgshex_ValueClass_httpwww_w3_orgshexvalueClassLabel', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 327, 12), )

    
    valueClassLabel = property(__valueClassLabel.value, __valueClassLabel.set, None, None)

    _ElementMap.update({
        __facet.name() : __facet,
        __or.name() : __or,
        __valueSet.name() : __valueSet,
        __valueClassLabel.name() : __valueClassLabel
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueClass', ValueClass)


# Complex type {http://www.w3.org/shex/}FullValueClass with content type ELEMENT_ONLY
class FullValueClass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}FullValueClass with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FullValueClass')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 331, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}nodetype uses Python identifier nodetype
    __nodetype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nodetype'), 'nodetype', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexnodetype', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 333, 12), )

    
    nodetype = property(__nodetype.value, __nodetype.set, None, None)

    
    # Element {http://www.w3.org/shex/}datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'datatype'), 'datatype', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexdatatype', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 334, 12), )

    
    datatype = property(__datatype.value, __datatype.set, None, None)

    
    # Element {http://www.w3.org/shex/}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexfacet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 335, 12), )

    
    facet = property(__facet.value, __facet.set, None, None)

    
    # Element {http://www.w3.org/shex/}or uses Python identifier or_
    __or = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'or'), 'or_', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexor', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 336, 12), )

    
    or_ = property(__or.value, __or.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueSet uses Python identifier valueSet
    __valueSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), 'valueSet', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexvalueSet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 12), )

    
    valueSet = property(__valueSet.value, __valueSet.set, None, None)

    
    # Element {http://www.w3.org/shex/}valueClassLabel uses Python identifier valueClassLabel
    __valueClassLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel'), 'valueClassLabel', '__httpwww_w3_orgshex_FullValueClass_httpwww_w3_orgshexvalueClassLabel', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 338, 12), )

    
    valueClassLabel = property(__valueClassLabel.value, __valueClassLabel.set, None, None)

    _ElementMap.update({
        __nodetype.name() : __nodetype,
        __datatype.name() : __datatype,
        __facet.name() : __facet,
        __or.name() : __or,
        __valueSet.name() : __valueSet,
        __valueClassLabel.name() : __valueClassLabel
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FullValueClass', FullValueClass)


# Complex type {http://www.w3.org/shex/}ValueClassExpression with content type ELEMENT_ONLY
class ValueClassExpression (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}ValueClassExpression with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueClassExpression')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 342, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpwww_w3_orgshex_ValueClassExpression_httpwww_w3_orgshexentry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 344, 12), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueClassExpression', ValueClassExpression)


# Complex type {http://www.w3.org/shex/}GroupShapeConstr with content type ELEMENT_ONLY
class GroupShapeConstr (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}GroupShapeConstr with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroupShapeConstr')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 348, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}disjunct uses Python identifier disjunct
    __disjunct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disjunct'), 'disjunct', '__httpwww_w3_orgshex_GroupShapeConstr_httpwww_w3_orgshexdisjunct', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 350, 12), )

    
    disjunct = property(__disjunct.value, __disjunct.set, None, None)

    
    # Element {http://www.w3.org/shex/}stringFacet uses Python identifier stringFacet
    __stringFacet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stringFacet'), 'stringFacet', '__httpwww_w3_orgshex_GroupShapeConstr_httpwww_w3_orgshexstringFacet', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 351, 12), )

    
    stringFacet = property(__stringFacet.value, __stringFacet.set, None, None)

    _ElementMap.update({
        __disjunct.name() : __disjunct,
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 366, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pattern'), 'pattern', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexpattern', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 371, 12), )

    
    pattern = property(__pattern.value, __pattern.set, None, None)

    
    # Element {http://www.w3.org/shex/}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexnot', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 372, 12), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {http://www.w3.org/shex/}minLength uses Python identifier minLength
    __minLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minLength'), 'minLength', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexminLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 373, 12), )

    
    minLength = property(__minLength.value, __minLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), 'maxLength', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexmaxLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 374, 12), )

    
    maxLength = property(__maxLength.value, __maxLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexlength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 375, 12), )

    
    length = property(__length.value, __length.set, None, None)

    
    # Element {http://www.w3.org/shex/}minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minValue'), 'minValue', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexminValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 376, 12), )

    
    minValue = property(__minValue.value, __minValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxValue uses Python identifier maxValue
    __maxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), 'maxValue', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexmaxValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 377, 12), )

    
    maxValue = property(__maxValue.value, __maxValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}totalDigits uses Python identifier totalDigits
    __totalDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), 'totalDigits', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshextotalDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 378, 12), )

    
    totalDigits = property(__totalDigits.value, __totalDigits.set, None, None)

    
    # Element {http://www.w3.org/shex/}fractionDigits uses Python identifier fractionDigits
    __fractionDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), 'fractionDigits', '__httpwww_w3_orgshex_XSFacet_httpwww_w3_orgshexfractionDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 379, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 383, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute open uses Python identifier open
    __open = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'open'), 'open', '__httpwww_w3_orgshex_Range_open', pyxb.binding.datatypes.boolean, unicode_default='false')
    __open._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 386, 16)
    __open._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 386, 16)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 391, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}pattern uses Python identifier pattern
    __pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pattern'), 'pattern', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexpattern', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 393, 12), )

    
    pattern = property(__pattern.value, __pattern.set, None, None)

    
    # Element {http://www.w3.org/shex/}not uses Python identifier not_
    __not = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'not'), 'not_', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexnot', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 394, 12), )

    
    not_ = property(__not.value, __not.set, None, None)

    
    # Element {http://www.w3.org/shex/}minLength uses Python identifier minLength
    __minLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minLength'), 'minLength', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexminLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 395, 12), )

    
    minLength = property(__minLength.value, __minLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), 'maxLength', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexmaxLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 396, 12), )

    
    maxLength = property(__maxLength.value, __maxLength.set, None, None)

    
    # Element {http://www.w3.org/shex/}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpwww_w3_orgshex_StringFacet_httpwww_w3_orgshexlength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 397, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 401, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'minValue'), 'minValue', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexminValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 403, 12), )

    
    minValue = property(__minValue.value, __minValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}maxValue uses Python identifier maxValue
    __maxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), 'maxValue', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexmaxValue', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 404, 12), )

    
    maxValue = property(__maxValue.value, __maxValue.set, None, None)

    
    # Element {http://www.w3.org/shex/}totalDigits uses Python identifier totalDigits
    __totalDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), 'totalDigits', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshextotalDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 405, 12), )

    
    totalDigits = property(__totalDigits.value, __totalDigits.set, None, None)

    
    # Element {http://www.w3.org/shex/}fractionDigits uses Python identifier fractionDigits
    __fractionDigits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), 'fractionDigits', '__httpwww_w3_orgshex_NumericFacet_httpwww_w3_orgshexfractionDigits', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 406, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 413, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}iriRange uses Python identifier iriRange
    __iriRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iriRange'), 'iriRange', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexiriRange', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 415, 12), )

    
    iriRange = property(__iriRange.value, __iriRange.set, None, None)

    
    # Element {http://www.w3.org/shex/}rdfLiteral uses Python identifier rdfLiteral
    __rdfLiteral = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral'), 'rdfLiteral', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexrdfLiteral', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 416, 12), )

    
    rdfLiteral = property(__rdfLiteral.value, __rdfLiteral.set, None, None)

    
    # Element {http://www.w3.org/shex/}integer uses Python identifier integer
    __integer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'integer'), 'integer', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexinteger', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 417, 12), )

    
    integer = property(__integer.value, __integer.set, None, None)

    
    # Element {http://www.w3.org/shex/}decimal uses Python identifier decimal
    __decimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'decimal'), 'decimal', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexdecimal', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 418, 12), )

    
    decimal = property(__decimal.value, __decimal.set, None, None)

    
    # Element {http://www.w3.org/shex/}double uses Python identifier double
    __double = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'double'), 'double', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexdouble', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 419, 12), )

    
    double = property(__double.value, __double.set, None, None)

    
    # Element {http://www.w3.org/shex/}boolean uses Python identifier boolean
    __boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boolean'), 'boolean', '__httpwww_w3_orgshex_ValueSet_httpwww_w3_orgshexboolean', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 420, 12), )

    
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


# Complex type {http://www.w3.org/shex/}ValueClassDefinition with content type ELEMENT_ONLY
class ValueClassDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/shex/}ValueClassDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueClassDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}valueClass uses Python identifier valueClass
    __valueClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueClass'), 'valueClass', '__httpwww_w3_orgshex_ValueClassDefinition_httpwww_w3_orgshexvalueClass', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 96, 12), )

    
    valueClass = property(__valueClass.value, __valueClass.set, None, None)

    
    # Element {http://www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actions'), 'actions', '__httpwww_w3_orgshex_ValueClassDefinition_httpwww_w3_orgshexactions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 97, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute valueClassLabel uses Python identifier valueClassLabel
    __valueClassLabel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'valueClassLabel'), 'valueClassLabel', '__httpwww_w3_orgshex_ValueClassDefinition_valueClassLabel', IRI)
    __valueClassLabel._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 8)
    __valueClassLabel._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 99, 8)
    
    valueClassLabel = property(__valueClassLabel.value, __valueClassLabel.set, None, None)

    
    # Attribute external uses Python identifier external
    __external = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'external'), 'external', '__httpwww_w3_orgshex_ValueClassDefinition_external', pyxb.binding.datatypes.boolean, unicode_default='false')
    __external._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 8)
    __external._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 100, 8)
    
    external = property(__external.value, __external.set, None, None)

    _ElementMap.update({
        __valueClass.name() : __valueClass,
        __actions.name() : __actions
    })
    _AttributeMap.update({
        __valueClassLabel.name() : __valueClassLabel,
        __external.name() : __external
    })
Namespace.addCategoryObject('typeBinding', 'ValueClassDefinition', ValueClassDefinition)


# Complex type {http://www.w3.org/shex/}IncludeProperty with content type EMPTY
class IncludeProperty (pyxb.binding.basis.complexTypeDefinition):
    """For valid typing. A property that may be present in a graph that is not defined by a given shape."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncludeProperty')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 110, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IncludeProperty_ref', IRI, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 114, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 114, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 244, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}iriref uses Python identifier iriref
    __iriref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iriref'), 'iriref', '__httpwww_w3_orgshex_Annotation_httpwww_w3_orgshexiriref', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 246, 12), )

    
    iriref = property(__iriref.value, __iriref.set, None, None)

    
    # Element {http://www.w3.org/shex/}literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'literal'), 'literal', '__httpwww_w3_orgshex_Annotation_httpwww_w3_orgshexliteral', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 247, 12), )

    
    literal = property(__literal.value, __literal.set, None, None)

    
    # Attribute iri uses Python identifier iri
    __iri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iri'), 'iri', '__httpwww_w3_orgshex_Annotation_iri', IRI)
    __iri._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 249, 8)
    __iri._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 249, 8)
    
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
    """A label that identifies an external process to be invoked"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodeLabel')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 303, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_CodeLabel_ref', UCASE_LABEL, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 307, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 307, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 355, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IRIRef_ref', IRI, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 356, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 356, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 428, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'base'), 'base', '__httpwww_w3_orgshex_IRIStem_base', IRI)
    __base._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 433, 8)
    __base._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 433, 8)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute stem uses Python identifier stem
    __stem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stem'), 'stem', '__httpwww_w3_orgshex_IRIStem_stem', pyxb.binding.datatypes.boolean, unicode_default='false')
    __stem._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 434, 8)
    __stem._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 434, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 451, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datatype'), 'datatype', '__httpwww_w3_orgshex_RDFLiteral_datatype', IRI)
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 454, 16)
    __datatype._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 454, 16)
    
    datatype = property(__datatype.value, __datatype.set, None, None)

    
    # Attribute langtag uses Python identifier langtag
    __langtag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'langtag'), 'langtag', '__httpwww_w3_orgshex_RDFLiteral_langtag', pyxb.binding.datatypes.string)
    __langtag._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 455, 16)
    __langtag._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 455, 16)
    
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
    """A shape definition document. A shape definition or "Schema" consists of: """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Schema')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}startActions uses Python identifier startActions
    __startActions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startActions'), 'startActions', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexstartActions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 28, 12), )

    
    startActions = property(__startActions.value, __startActions.set, None, 'A set of semantic actions to be invoked  the shape is evaluated')

    
    # Element {http://www.w3.org/shex/}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shape'), 'shape', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexshape', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 33, 12), )

    
    shape = property(__shape.value, __shape.set, None, 'An unordered list of labeled shape definitions')

    
    # Element {http://www.w3.org/shex/}valueClass uses Python identifier valueClass
    __valueClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueClass'), 'valueClass', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexvalueClass', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 38, 12), )

    
    valueClass = property(__valueClass.value, __valueClass.set, None, 'An unordered set of labeled value class definitions. Labels can either be explicit or internally generated')

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__httpwww_w3_orgshex_Schema__start', ShapeLabel)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 44, 8)
    __start._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 44, 8)
    
    start = property(__start.value, __start.set, None, 'The label initial shape (entry point) in the definition. If absent, the start shape must be supplied by the application')

    
    # Attribute exclude-prefixes uses Python identifier exclude_prefixes
    __exclude_prefixes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exclude-prefixes'), 'exclude_prefixes', '__httpwww_w3_orgshex_Schema__exclude_prefixes', pyxb.binding.datatypes.string)
    __exclude_prefixes._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 49, 8)
    __exclude_prefixes._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 49, 8)
    
    exclude_prefixes = property(__exclude_prefixes.value, __exclude_prefixes.set, None, 'A space separated list of namespaces to be excluded from the target ShEx document')

    
    # Attribute default-namespace uses Python identifier default_namespace
    __default_namespace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default-namespace'), 'default_namespace', '__httpwww_w3_orgshex_Schema__default_namespace', pyxb.binding.datatypes.anyURI)
    __default_namespace._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 54, 8)
    __default_namespace._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 54, 8)
    
    default_namespace = property(__default_namespace.value, __default_namespace.set, None, "The URI of the default ShEx namespace, if any. Corresponds to the ShEx ':' namespace")

    _ElementMap.update({
        __startActions.name() : __startActions,
        __shape.name() : __shape,
        __valueClass.name() : __valueClass
    })
    _AttributeMap.update({
        __start.name() : __start,
        __exclude_prefixes.name() : __exclude_prefixes,
        __default_namespace.name() : __default_namespace
    })
Namespace.addCategoryObject('typeBinding', 'Schema', Schema_)


# Complex type {http://www.w3.org/shex/}Shape with content type ELEMENT_ONLY
class Shape (pyxb.binding.basis.complexTypeDefinition):
    """A labeled definition of an RDF shape."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Shape')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 63, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}extra uses Python identifier extra
    __extra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extra'), 'extra', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexextra', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 70, 12), )

    
    extra = property(__extra.value, __extra.set, None, 'The set of properties included with the shape definition. Must be empty if  is true.')

    
    # Element {http://www.w3.org/shex/}someOf uses Python identifier someOf
    __someOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'someOf'), 'someOf', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexsomeOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16), )

    
    someOf = property(__someOf.value, __someOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://www.w3.org/shex/}tripleConstraint uses Python identifier tripleConstraint
    __tripleConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), 'tripleConstraint', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshextripleConstraint', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16), )

    
    tripleConstraint = property(__tripleConstraint.value, __tripleConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexinclude', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.w3.org/shex/}wrapper uses Python identifier wrapper
    __wrapper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), 'wrapper', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexwrapper', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16), )

    
    wrapper = property(__wrapper.value, __wrapper.set, None, None)

    
    # Element {http://www.w3.org/shex/}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexannotation', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actions'), 'actions', '__httpwww_w3_orgshex_Shape_httpwww_w3_orgshexactions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httpwww_w3_orgshex_Shape_label', ShapeLabel, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 76, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 76, 8)
    
    label = property(__label.value, __label.set, None, "The name of the shape. The local name of an anonymous shape begins with an underscore ('_') (i.e. it is a blank node")

    
    # Attribute virtual uses Python identifier virtual
    __virtual = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'virtual'), 'virtual', '__httpwww_w3_orgshex_Shape_virtual', pyxb.binding.datatypes.boolean, unicode_default='false')
    __virtual._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 81, 8)
    __virtual._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 81, 8)
    
    virtual = property(__virtual.value, __virtual.set, None, 'If true, this shape cannot be applied directly and may only be included in another shape definition.')

    
    # Attribute closed uses Python identifier closed
    __closed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'closed'), 'closed', '__httpwww_w3_orgshex_Shape_closed', pyxb.binding.datatypes.boolean, unicode_default='false')
    __closed._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 86, 8)
    __closed._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 86, 8)
    
    closed = property(__closed.value, __closed.set, None, 'If true, this shape definition is "strict", in the sense that  of the triples in the graph must match the shape definition. If false, graphs that\n                         the matching shape definition are considered passing. ')

    _ElementMap.update({
        __extra.name() : __extra,
        __someOf.name() : __someOf,
        __group.name() : __group,
        __tripleConstraint.name() : __tripleConstraint,
        __include.name() : __include,
        __wrapper.name() : __wrapper,
        __annotation.name() : __annotation,
        __actions.name() : __actions
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 103, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_IncludeShape_ref', ShapeLabel, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 107, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 107, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', 'IncludeShape', IncludeShape)


# Complex type {http://www.w3.org/shex/}Wrapper with content type ELEMENT_ONLY
class Wrapper (pyxb.binding.basis.complexTypeDefinition):
    """Wrapper implements the  construct, providing a point to hang:
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Wrapper')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 140, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}someOf uses Python identifier someOf
    __someOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'someOf'), 'someOf', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexsomeOf', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16), )

    
    someOf = property(__someOf.value, __someOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexgroup', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://www.w3.org/shex/}tripleConstraint uses Python identifier tripleConstraint
    __tripleConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), 'tripleConstraint', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshextripleConstraint', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16), )

    
    tripleConstraint = property(__tripleConstraint.value, __tripleConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexinclude', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.w3.org/shex/}wrapper uses Python identifier wrapper
    __wrapper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), 'wrapper', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexwrapper', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16), )

    
    wrapper = property(__wrapper.value, __wrapper.set, None, None)

    
    # Element {http://www.w3.org/shex/}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexannotation', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 12), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actions'), 'actions', '__httpwww_w3_orgshex_Wrapper_httpwww_w3_orgshexactions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 153, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_orgshex_Wrapper_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_orgshex_Wrapper_max', STD_ANON_2, unicode_default='1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __someOf.name() : __someOf,
        __group.name() : __group,
        __tripleConstraint.name() : __tripleConstraint,
        __include.name() : __include,
        __wrapper.name() : __wrapper,
        __annotation.name() : __annotation,
        __actions.name() : __actions
    })
    _AttributeMap.update({
        __min.name() : __min,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', 'Wrapper', Wrapper)


# Complex type {http://www.w3.org/shex/}ShapeConstraint with content type ELEMENT_ONLY
class ShapeConstraint (pyxb.binding.basis.complexTypeDefinition):
    """A complete shape constraint."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShapeConstraint')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 165, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}someOf uses Python identifier someOf
    __someOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'someOf'), 'someOf', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexsomeOf', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16), )

    
    someOf = property(__someOf.value, __someOf.set, None, None)

    
    # Element {http://www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'group'), 'group', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://www.w3.org/shex/}tripleConstraint uses Python identifier tripleConstraint
    __tripleConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), 'tripleConstraint', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshextripleConstraint', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16), )

    
    tripleConstraint = property(__tripleConstraint.value, __tripleConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexinclude', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.w3.org/shex/}wrapper uses Python identifier wrapper
    __wrapper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), 'wrapper', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexwrapper', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16), )

    
    wrapper = property(__wrapper.value, __wrapper.set, None, None)

    
    # Element {http://www.w3.org/shex/}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexannotation', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actions'), 'actions', '__httpwww_w3_orgshex_ShapeConstraint_httpwww_w3_orgshexactions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_orgshex_ShapeConstraint_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_orgshex_ShapeConstraint_max', STD_ANON_2, unicode_default='1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __someOf.name() : __someOf,
        __group.name() : __group,
        __tripleConstraint.name() : __tripleConstraint,
        __include.name() : __include,
        __wrapper.name() : __wrapper,
        __annotation.name() : __annotation,
        __actions.name() : __actions
    })
    _AttributeMap.update({
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 176, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/shex/}objectConstraint uses Python identifier objectConstraint
    __objectConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint'), 'objectConstraint', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexobjectConstraint', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 180, 16), )

    
    objectConstraint = property(__objectConstraint.value, __objectConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}subjectConstraint uses Python identifier subjectConstraint
    __subjectConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint'), 'subjectConstraint', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexsubjectConstraint', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 181, 16), )

    
    subjectConstraint = property(__subjectConstraint.value, __subjectConstraint.set, None, None)

    
    # Element {http://www.w3.org/shex/}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexannotation', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 183, 12), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actions'), 'actions', '__httpwww_w3_orgshex_TripleConstraint_httpwww_w3_orgshexactions', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 184, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute predicate uses Python identifier predicate
    __predicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'predicate'), 'predicate', '__httpwww_w3_orgshex_TripleConstraint_predicate', IRI, required=True)
    __predicate._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 186, 8)
    __predicate._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 186, 8)
    
    predicate = property(__predicate.value, __predicate.set, None, None)

    
    # Attribute inverse uses Python identifier inverse
    __inverse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inverse'), 'inverse', '__httpwww_w3_orgshex_TripleConstraint_inverse', pyxb.binding.datatypes.boolean)
    __inverse._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 187, 8)
    __inverse._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 187, 8)
    
    inverse = property(__inverse.value, __inverse.set, None, 'Only used in the case of a reverse predicate with any subject ({ ^ :p .})')

    
    # Attribute object uses Python identifier object
    __object = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'object'), 'object', '__httpwww_w3_orgshex_TripleConstraint_object', IRI)
    __object._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 192, 8)
    __object._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 192, 8)
    
    object = property(__object.value, __object.set, None, 'A simple object IRI. Equivalent to a single, non-stemmed value set in the object position.')

    
    # Attribute subject uses Python identifier subject
    __subject = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subject'), 'subject', '__httpwww_w3_orgshex_TripleConstraint_subject', IRI)
    __subject._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 197, 8)
    __subject._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 197, 8)
    
    subject = property(__subject.value, __subject.set, None, 'A simple subject IRI. Used for a single, non-stemmed value set in the subject position.')

    
    # Attribute objectShape uses Python identifier objectShape
    __objectShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'objectShape'), 'objectShape', '__httpwww_w3_orgshex_TripleConstraint_objectShape', ShapeLabel)
    __objectShape._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 202, 8)
    __objectShape._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 202, 8)
    
    objectShape = property(__objectShape.value, __objectShape.set, None, 'A reference to a shape. Used with a single groupShapeConstrin the object position.')

    
    # Attribute subjectShape uses Python identifier subjectShape
    __subjectShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subjectShape'), 'subjectShape', '__httpwww_w3_orgshex_TripleConstraint_subjectShape', ShapeLabel)
    __subjectShape._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 207, 8)
    __subjectShape._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 207, 8)
    
    subjectShape = property(__subjectShape.value, __subjectShape.set, None, 'A reference to a shape. Used with a single groupShapeConstr in the subject position.')

    
    # Attribute objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'objectType'), 'objectType', '__httpwww_w3_orgshex_TripleConstraint_objectType', NodeType)
    __objectType._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 212, 8)
    __objectType._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 212, 8)
    
    objectType = property(__objectType.value, __objectType.set, None, 'A constraint on the type of object.')

    
    # Attribute subjectType uses Python identifier subjectType
    __subjectType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'subjectType'), 'subjectType', '__httpwww_w3_orgshex_TripleConstraint_subjectType', NodeType)
    __subjectType._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 217, 8)
    __subjectType._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 217, 8)
    
    subjectType = property(__subjectType.value, __subjectType.set, None, 'A constraint on the type of subject')

    
    # Attribute datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datatype'), 'datatype', '__httpwww_w3_orgshex_TripleConstraint_datatype', pyxb.binding.datatypes.anyURI)
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 222, 8)
    __datatype._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 222, 8)
    
    datatype = property(__datatype.value, __datatype.set, None, 'The URI of a datatype. Used for a single datatype in the object position, with or without facets')

    
    # Attribute negated uses Python identifier negated
    __negated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negated'), 'negated', '__httpwww_w3_orgshex_TripleConstraint_negated', pyxb.binding.datatypes.boolean, unicode_default='false')
    __negated._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 227, 8)
    __negated._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 227, 8)
    
    negated = property(__negated.value, __negated.set, None, 'True means that the match is NOT what is in the constraint')

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_orgshex_TripleConstraint_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default='1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 471, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_orgshex_TripleConstraint_max', STD_ANON_2, unicode_default='1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 472, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __objectConstraint.name() : __objectConstraint,
        __subjectConstraint.name() : __subjectConstraint,
        __annotation.name() : __annotation,
        __actions.name() : __actions
    })
    _AttributeMap.update({
        __predicate.name() : __predicate,
        __inverse.name() : __inverse,
        __object.name() : __object,
        __subject.name() : __subject,
        __objectShape.name() : __objectShape,
        __subjectShape.name() : __subjectShape,
        __objectType.name() : __objectType,
        __subjectType.name() : __subjectType,
        __datatype.name() : __datatype,
        __negated.name() : __negated,
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 359, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ref'), 'ref', '__httpwww_w3_orgshex_ShapeRef_ref', ShapeLabel, required=True)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 360, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 360, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 437, 4)
    _ElementMap = IRIStem._ElementMap.copy()
    _AttributeMap = IRIStem._AttributeMap.copy()
    # Base type is IRIStem
    
    # Element {http://www.w3.org/shex/}exclusion uses Python identifier exclusion
    __exclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exclusion'), 'exclusion', '__httpwww_w3_orgshex_IRIRange_httpwww_w3_orgshexexclusion', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 445, 20), )

    
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



SemanticActions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'action'), SemanticAction, scope=SemanticActions, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 260, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticActions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'action')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SemanticActions._Automaton = _BuildAutomaton()




SemanticAction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codeLabel'), CodeLabel, scope=SemanticAction, documentation='The name of a function that will be bound when the shape is evaluated', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12)))

SemanticAction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codeDecl'), CodeDecl, scope=SemanticAction, documentation='The language specific function to be invoked', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 274, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticAction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codeLabel')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 269, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SemanticAction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codeDecl')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 274, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SemanticAction._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 294, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 294, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CodeDecl._Automaton = _BuildAutomaton_2()




ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), XSFacet, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 324, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), GroupShapeConstr, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 325, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), ValueSet, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 326, 12)))

ValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel'), IRIRef, scope=ValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 327, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 324, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 325, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueSet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 326, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 327, 12))
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




FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nodetype'), NodeType, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 333, 12)))

FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'datatype'), pyxb.binding.datatypes.anyURI, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 334, 12)))

FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), XSFacet, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 335, 12)))

FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'or'), GroupShapeConstr, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 336, 12)))

FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueSet'), ValueSet, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 12)))

FullValueClass._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel'), IRIRef, scope=FullValueClass, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 338, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nodetype')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 333, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'datatype')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 334, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 335, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'or')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 336, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueSet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 337, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FullValueClass._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueClassLabel')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 338, 12))
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
FullValueClass._Automaton = _BuildAutomaton_4()




ValueClassExpression._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), FullValueClass, scope=ValueClassExpression, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 344, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueClassExpression._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 344, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueClassExpression._Automaton = _BuildAutomaton_5()




GroupShapeConstr._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disjunct'), ShapeRef, scope=GroupShapeConstr, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 350, 12)))

GroupShapeConstr._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stringFacet'), StringFacet, scope=GroupShapeConstr, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 351, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 350, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 351, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroupShapeConstr._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disjunct')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 350, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroupShapeConstr._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stringFacet')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 351, 12))
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
GroupShapeConstr._Automaton = _BuildAutomaton_6()




XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pattern'), pyxb.binding.datatypes.string, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 371, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), pyxb.binding.datatypes.string, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 372, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minLength'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 373, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 374, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 375, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minValue'), Range, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 376, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), Range, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 377, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 378, 12)))

XSFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), pyxb.binding.datatypes.int, scope=XSFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 379, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pattern')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 371, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 372, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 373, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 374, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 375, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 376, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 377, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 378, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XSFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 379, 12))
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
XSFacet._Automaton = _BuildAutomaton_7()




StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pattern'), pyxb.binding.datatypes.string, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 393, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'not'), pyxb.binding.datatypes.string, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 394, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minLength'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 395, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxLength'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 396, 12)))

StringFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), pyxb.binding.datatypes.int, scope=StringFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 397, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pattern')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 393, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'not')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 394, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 395, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 396, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 397, 12))
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
StringFacet._Automaton = _BuildAutomaton_8()




NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minValue'), Range, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 403, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), Range, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 404, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalDigits'), pyxb.binding.datatypes.int, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 405, 12)))

NumericFacet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits'), pyxb.binding.datatypes.int, scope=NumericFacet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 406, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'minValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxValue')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumericFacet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionDigits')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 406, 12))
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
NumericFacet._Automaton = _BuildAutomaton_9()




ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iriRange'), IRIRange, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 415, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral'), RDFLiteral, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 416, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'integer'), pyxb.binding.datatypes.int, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 417, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'decimal'), pyxb.binding.datatypes.decimal, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 418, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'double'), pyxb.binding.datatypes.double, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 419, 12)))

ValueSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boolean'), pyxb.binding.datatypes.boolean, scope=ValueSet, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 420, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iriRange')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 415, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rdfLiteral')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 416, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'integer')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 417, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'decimal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 418, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'double')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 419, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueSet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boolean')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 420, 12))
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
ValueSet._Automaton = _BuildAutomaton_10()




ValueClassDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueClass'), ValueClassExpression, scope=ValueClassDefinition, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 96, 12)))

ValueClassDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), SemanticActions, scope=ValueClassDefinition, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 97, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 96, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 97, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValueClassDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueClass')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 96, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ValueClassDefinition._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 97, 12))
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
ValueClassDefinition._Automaton = _BuildAutomaton_11()




Annotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iriref'), IRI, scope=Annotation, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 246, 12)))

Annotation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'literal'), RDFLiteral, scope=Annotation, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 247, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Annotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iriref')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Annotation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'literal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 247, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Annotation._Automaton = _BuildAutomaton_12()




Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startActions'), SemanticActions, scope=Schema_, documentation='A set of semantic actions to be invoked  the shape is evaluated', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 28, 12)))

Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shape'), Shape, scope=Schema_, documentation='An unordered list of labeled shape definitions', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 33, 12)))

Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueClass'), ValueClassDefinition, scope=Schema_, documentation='An unordered set of labeled value class definitions. Labels can either be explicit or internally generated', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 38, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 28, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 33, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 38, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startActions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 28, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shape')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 33, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueClass')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 38, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Schema_._Automaton = _BuildAutomaton_13()




Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extra'), IncludeProperty, scope=Shape, documentation='The set of properties included with the shape definition. Must be empty if  is true.', location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 70, 12)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'someOf'), ShapeConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), ShapeConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), TripleConstraint, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), IncludeShape, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), Wrapper, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), Annotation, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12)))

Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), SemanticActions, scope=Shape, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 68, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 70, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'someOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wrapper')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extra')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 70, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Shape._Automaton = _BuildAutomaton_14()




Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'someOf'), ShapeConstraint, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), ShapeConstraint, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), TripleConstraint, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), IncludeShape, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), Wrapper, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), Annotation, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 12)))

Wrapper._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), SemanticActions, scope=Wrapper, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 153, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 153, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'someOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wrapper')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 152, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Wrapper._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 153, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Wrapper._Automaton = _BuildAutomaton_15()




ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'someOf'), ShapeConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'group'), ShapeConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint'), TripleConstraint, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), IncludeShape, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'wrapper'), Wrapper, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), Annotation, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12)))

ShapeConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), SemanticActions, scope=ShapeConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'someOf')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 131, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'group')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 132, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tripleConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 133, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 134, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'wrapper')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 135, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 160, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ShapeConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 161, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShapeConstraint._Automaton = _BuildAutomaton_16()




TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint'), ValueClass, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 180, 16)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint'), ValueClass, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 181, 16)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), Annotation, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 183, 12)))

TripleConstraint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actions'), SemanticActions, scope=TripleConstraint, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 184, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 179, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 183, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 184, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 180, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subjectConstraint')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 181, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 183, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TripleConstraint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actions')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 184, 12))
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
TripleConstraint._Automaton = _BuildAutomaton_17()




IRIRange._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exclusion'), IRIStem, scope=IRIRange, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 445, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 445, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IRIRange._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exclusion')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd', 445, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IRIRange._Automaton = _BuildAutomaton_18()

