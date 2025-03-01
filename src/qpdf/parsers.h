/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * Copyright (C) 2021, James R. Barlow (https://github.com/jbarlow83/)
 */

#pragma once

#include "pikepdf.h"

#include <qpdf/QPDFTokenizer.hh>

// Used to implement pikepdf.StreamParser, which can be subclassed to implement
// custom parsing.
class PyParserCallbacks : public QPDFObjectHandle::ParserCallbacks {
public:
    using QPDFObjectHandle::ParserCallbacks::ParserCallbacks;
    virtual ~PyParserCallbacks() = default;

    void handleObject(QPDFObjectHandle obj, size_t offset, size_t length) override;
    void handleEOF() override;
};

// Used for parse_content_stream. Handles each object by grouping into operands
// and operators. The whole parse stream can be retrived at once.
class OperandGrouper : public QPDFObjectHandle::ParserCallbacks {
public:
    OperandGrouper(const std::string &operators);
    void handleObject(QPDFObjectHandle obj) override;
    void handleEOF() override;

    py::list getInstructions() const;
    std::string getWarning() const;

private:
    std::set<std::string> whitelist;
    std::vector<QPDFObjectHandle> tokens;
    bool parsing_inline_image;
    std::vector<QPDFObjectHandle> inline_metadata;
    py::list instructions;
    uint count;
    std::string warning;
};

// unparse the list of instructions generated by an OperandGrouper
py::bytes unparse_content_stream(py::iterable contentstream);
