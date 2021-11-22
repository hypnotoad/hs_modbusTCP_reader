#!/bin/bash
(cd ../../; python2 ./generator.pyc hs_modbusTCP_reader utf-8)
markdown2 --extras tables,fenced-code-blocks,strike,target-blank-links doc/log14184.md > release/log14184.html
(cd release; zip -r 14184_hs_modbusTCP_reader.hslz *)
