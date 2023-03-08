import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 125X, data")

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
#'/store/group/phys_heavyions/mnguyen/HIRun2022A/RecoPatfromRaw_RAW2DIGI_L1Reco_RECO_PAT_inMINIAOD.root',
#'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/219/00000/d0a95156-a786-4e2c-8549-2a39e5f293c0.root',
#'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/229/00000/c5e5fbc5-b1c4-4920-9422-5116256f7fdf.root',
# 'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/243/00000/27d8b18f-2261-4c21-8a16-2dd50fcc4373.root'

## file dataset=/HITestRaw0/HIRun2022A-PromptReco-v1/AOD  run in [362318]        
#'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/318/00000/06d04439-5784-498c-a4af-3fffc3545a96.root',
#'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/318/00000/1077f7d6-e4cc-49cd-8d15-f4d145e9f869.root',
#'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/318/00000/22e8fcab-0b8f-4504-8b38-3c99e95bf833.root',
'root://cms-xrd-global.cern.ch//store/hidata/HIRun2022A/HITestRaw0/AOD/PromptReco-v1/000/362/318/00000/3fb50183-105d-46d8-9c44-95fd1b2ae44a.root',
    ), 
)

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '125X_dataRun3_relval_v6', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

###############################################################################
#centralityTag = "CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"
#process.HiForestInfo.info.append(centralityTag)
#
#print('\n')
#print('\033[31m~*~ CENTRALITY TABLE FOR 2018 PBPB DATA ~*~\033[0m')
#print('\033[36m~*~ TAG: ' + centralityTag + ' ~*~\033[0m')
#print('\n')
#process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
#process.GlobalTag.toGet.extend([
#    cms.PSet(
#        record = cms.string("HeavyIonRcd"),
#        tag = cms.string(centralityTag),
#        label = cms.untracked.string("HFtowers"),
#        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#        ),
#    ])
#
#process.GlobalTag.toGet.extend([
#    cms.PSet(
#        record = cms.string("BTagTrackProbability3DRcd"),
#        tag = cms.string("JPcalib_Data103X_2018PbPb_v1"),
#        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#        )
#    ])
#
###############################################################################

# root output
#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#         )
#     )

# process.output_path = cms.EndPath(process.output)

###############################################################################

# event analysis
# process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
#process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
#process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

#from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_mc
#process.hltobject.triggerNames = trigger_list_mc

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
################################
# electrons, photons, muons
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_data_cff')
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
# muons (FTW)
process.load("HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi")
process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")

#############################################################################
# high level trigger
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltfilter = hltHighLevel.clone(
    HLTPaths = [
      # "HLT_HIZeroBias_v4",                                                     
  # "HLT_HIMinimumBias_v2",
#"HLT_HIUPC_ZeroBias_MinPixelCluster400_MaxPixelCluster10000_v2"
#"HLT_HIUPC_SingleMuOpen_NotMBHF2OR_MaxPixelTrack_v4"
#'HLT_HIUPC_DoubleEG2_BptxAND_SinglePixelTrack_MaxPixelTrack_v4"
"HLT_HIUPC_ZeroBias_SinglePixelTrackLowPt_MaxPixelCluster400_v2"
#"HLT_HIUPC_ZeroBias_SinglePixelTrackLowPt_MaxPixelCluster400_v2"
#"HLT_HIUPC_SingleMuOpen_OR_SingleMuCosmic_EMTF_NotMBHF2AND_v2"
   ]
)

#########################################################################
# Muon filter
process.goodMuons = cms.EDFilter("MuonSelector",
   src = cms.InputTag("muons"),
   cut = cms.string('pt > 1.0'),
   filter = cms.bool(True)
 )

###############################################################################
# main forest sequence
process.forest = cms.Path(
     process.hltfilter  +
     process.goodMuons
    #process.hltfilter+
  #  process.HiForestInfo 
    #process.hltanalysis  
   # process.trackSequencePbPb +
   # process.particleFlowAnalyser +
   # process.hiEvtAnalyzer 
   ####process.ggHiNtuplizer +
   # process.akCs4PFJetAnalyzer +
   #process.unpackedMuons+
   # process.muonAnalyzer
    )
###############################################################################
#output module configuration

#from Configuration.EventContent.EventContent_cff import *
#skimeventcontent = cms.PSet(
#    outputCommands = cms.untracked.vstring()
# )
#skimeventcontent.outputCommands.extend(AODEventContent.outputCommands)

process.load('Configuration.EventContent.EventContentHeavyIons_cff')

#skimeventselection =  cms.PSet(SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('forest')))


# Add PoolOutputModule
process.output = cms.OutputModule( "PoolOutputModule",
   process.FEVTEventContent, 
#   skimeventselection,
   SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('forest')
    ),
   dataset = cms.untracked.PSet(
         filterName = cms.untracked.string('miniAOD'),
         dataTier = cms.untracked.string('USER')
   ),    
   fileName = cms.untracked.string('file:skimmed.root'),  # output file name

# save only events passing the "skimPath"
#    outputCommands = cms.untracked.vstring('keep *'), # keep all collections
)

process.ep =cms.EndPath(process.output)
