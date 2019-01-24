# ######################################################################################################################
# SYS ID DEFINE
# ======================================================================================================================
eSysElementSysNull = 0x0000
eSysId_DemoElement = eSysElementSysNull + 1
eSysId_OutPhPhVolSetting = eSysId_DemoElement + 1
eSysId_OutVolToleranceSetting = eSysId_OutPhPhVolSetting + 1
eSysId_OutVolCompSetting = eSysId_OutVolToleranceSetting + 1
eSysId_OutFreqSetting = eSysId_OutVolCompSetting + 1
eSysId_OutFreqToleranceSetting = eSysId_OutFreqSetting + 1
eSysId_OutFreqSyncSpeed = eSysId_OutFreqToleranceSetting + 1
eSysId_3PhIn1PhOut = eSysId_OutFreqSyncSpeed + 1
eSysId_ChgRegVolRef = eSysId_3PhIn1PhOut + 1
eSysId_ChgRegCurLim = eSysId_ChgRegVolRef + 1
eSysId_SlcChgEn = eSysId_ChgRegCurLim + 1
eSysId_MinChgVolRef = eSysId_SlcChgEn + 1
eSysId_MinChgCurLim = eSysId_MinChgVolRef + 1
eSysId_BattTestActive = eSysId_MinChgCurLim + 1
eSysId_MainsCurrentRampInTime = eSysId_BattTestActive + 1
eSysId_NeutralPresentSetting = eSysId_MainsCurrentRampInTime + 1
eSysId_InputFuseSetting = eSysId_NeutralPresentSetting + 1
eSysId_OutputFuseSetting = eSysId_InputFuseSetting + 1
eSysId_TotalLoadRate = eSysId_OutputFuseSetting + 1
eSysId_FanStates = eSysId_TotalLoadRate + 1
eSysId_BattMidPointPressentSetting = eSysId_FanStates + 1
eSysId_SlcSettingsConfirmed = eSysId_BattMidPointPressentSetting + 1
eSysId_PmSelftestStartAllowed = eSysId_SlcSettingsConfirmed + 1
eSysId_SbscDeviceVerification = eSysId_PmSelftestStartAllowed + 1
eSysId_EconvHarmCompEnableSetting = eSysId_SbscDeviceVerification + 1
eSysId_NpiTestModeEnabled = eSysId_EconvHarmCompEnableSetting + 1
eSysId_BattVolHighWarnLvl = eSysId_NpiTestModeEnabled + 1
eSysId_BattVolHighShutdownLvl = eSysId_BattVolHighWarnLvl + 1
eSysId_BattVolLowWarnLvl = eSysId_BattVolHighShutdownLvl + 1
eSysId_BattVolLowShutdownLvl = eSysId_BattVolLowWarnLvl + 1
eSysId_BattVolCollapseLvl = eSysId_BattVolLowShutdownLvl + 1
eSysId_BattVolCollapseClearLvl = eSysId_BattVolCollapseLvl + 1
eSysId_BbTripStatus = eSysId_BattVolCollapseClearLvl + 1
eSysId_BatteryRelayCloseAllowed = eSysId_BbTripStatus + 1
eSysId_PmcInvRlyOpenCmd = eSysId_BatteryRelayCloseAllowed + 1
eSysId_EnergyStorageAutoDisconnectStatus = eSysId_PmcInvRlyOpenCmd + 1
eSysId_PfcSysCtrlOpMode = eSysId_EnergyStorageAutoDisconnectStatus + 1
eSysId_PfcSysCtrlTransition = eSysId_PfcSysCtrlOpMode + 1
eSysId_PmcInvSysCtrlTransition = eSysId_PfcSysCtrlTransition + 1
eSysId_PfcInitRampInDone = eSysId_PmcInvSysCtrlTransition + 1
eSysId_PfcMainsRampInDone = eSysId_PfcInitRampInDone + 1
eSysId_RampInTimeChanged = eSysId_PfcMainsRampInDone + 1
eSysId_PmcChgStatus = eSysId_RampInTimeChanged + 1
eSysId_PmcInvSysCtrlOpMode = eSysId_PmcChgStatus + 1
eSysId_PfcCurrentReduced = eSysId_PmcInvSysCtrlOpMode + 1
eSysId_PmcInvSysCtrlInvOperable = eSysId_PfcCurrentReduced + 1
eSysId_InvSysCtrlOpMode = eSysId_PmcInvSysCtrlInvOperable + 1
eSysId_InvSysCtrlTransition = eSysId_InvSysCtrlOpMode + 1
eSysId_BypChgActive = eSysId_InvSysCtrlTransition + 1
eSysId_InvConvEn = eSysId_BypChgActive + 1
eSysId_DcGainEn = eSysId_InvConvEn + 1
eSysId_EconvHarmCompEnable = eSysId_DcGainEn + 1
eSysId_UpsSysCtrlUpsOpMode = eSysId_EconvHarmCompEnable + 1
eSysId_UpsSysCtrlTransition = eSysId_UpsSysCtrlUpsOpMode + 1
eSysId_UpsSysCtrlUpsOpsModeBatteryOp = eSysId_UpsSysCtrlTransition + 1
eSysId_UpsSysCtrlUpsOpModeNormalOp = eSysId_UpsSysCtrlUpsOpsModeBatteryOp + 1
eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypassFromOff = eSysId_UpsSysCtrlUpsOpModeNormalOp + 1
eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypass = eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypassFromOff + 1
eSysId_UpsSysCtrlUpsOpModeForcedStaticBypass = eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypass + 1
eSysId_UpsSysCtrlUpsOpModeMaintenanceBypass = eSysId_UpsSysCtrlUpsOpModeForcedStaticBypass + 1
eSysId_UpsSysCtrlUpsOpModeInverterStandby = eSysId_UpsSysCtrlUpsOpModeMaintenanceBypass + 1
eSysId_UpsSysCtrlUpsOpModeStaticBypassStandby = eSysId_UpsSysCtrlUpsOpModeInverterStandby + 1
eSysId_UpsSysCtrlUpsOpModeInverterSPoT = eSysId_UpsSysCtrlUpsOpModeStaticBypassStandby + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserRedundancy = eSysId_UpsSysCtrlUpsOpModeInverterSPoT + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserOffConfirm = eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserRedundancy + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerForcedStaticBypassDueToOffBt = eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserOffConfirm + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromOff = eSysId_UpsSysCtrlUpsOpModeReqHandlerForcedStaticBypassDueToOffBt + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromReqBypass = eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromOff + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerOnButtonPressed = eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromReqBypass + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerRequestedBypass = eSysId_UpsSysCtrlUpsOpModeReqHandlerOnButtonPressed + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerBypassBurnInTest = eSysId_UpsSysCtrlUpsOpModeReqHandlerRequestedBypass + 1
eSysId_UpsSysCtrlUpsOpModeReqHandlerDischargeBurnInTest = eSysId_UpsSysCtrlUpsOpModeReqHandlerBypassBurnInTest + 1
eSysId_UpsSysCtrlUpsSysCtrlAutostartActivated = eSysId_UpsSysCtrlUpsOpModeReqHandlerDischargeBurnInTest + 1
eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassInvShutdown = eSysId_UpsSysCtrlUpsSysCtrlAutostartActivated + 1
eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassShortRegByp = eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassInvShutdown + 1
eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOutVqdErr = eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassShortRegByp + 1
eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOverload = eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOutVqdErr + 1
eSysId_UpsSysCtrlActivateStaticBypassSwitchNoBreak = eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOverload + 1
eSysId_UpsSysCtrlActivateStaticBypassSwitchWithBreak = eSysId_UpsSysCtrlActivateStaticBypassSwitchNoBreak + 1
eSysId_UpsSysCtrlDeactivateStaticBypassSwitch = eSysId_UpsSysCtrlActivateStaticBypassSwitchWithBreak + 1
eSysId_UpsSysCtrlUpsShutdownDueToLowBattery = eSysId_UpsSysCtrlDeactivateStaticBypassSwitch + 1
eSysId_UpsSysCtrlSbsOpModeCmd = eSysId_UpsSysCtrlUpsShutdownDueToLowBattery + 1
eSysId_UpsSysCtrlSystemAutoRestarted = eSysId_UpsSysCtrlSbsOpModeCmd + 1
eSysId_UpsSysCtrlSmoothTransferToBypassEn = eSysId_UpsSysCtrlSystemAutoRestarted + 1
eSysId_UpsSysCtrlDisChargeBurnInTestMode = eSysId_UpsSysCtrlSmoothTransferToBypassEn + 1
eSysId_UpsSysCtrlPfcOpModeNumberInBattOp = eSysId_UpsSysCtrlDisChargeBurnInTestMode + 1
eSysId_UpsSysCtrlPfcOpModeAllBattOp = eSysId_UpsSysCtrlPfcOpModeNumberInBattOp + 1
eSysId_UpsSysCtrlPfcOpModeAllNormOp = eSysId_UpsSysCtrlPfcOpModeAllBattOp + 1
eSysId_UpsSysCtrlPfcOpModeOneBattOp = eSysId_UpsSysCtrlPfcOpModeAllNormOp + 1
eSysId_UpsSysCtrlPfcOpModeOneNormOp = eSysId_UpsSysCtrlPfcOpModeOneBattOp + 1
eSysId_UpsSysCtrlPfcOpModeOneNormOpOrRampIn = eSysId_UpsSysCtrlPfcOpModeOneNormOp + 1
eSysId_UpsSysCtrlPfcOpModeOneOffOp = eSysId_UpsSysCtrlPfcOpModeOneNormOpOrRampIn + 1
eSysId_UpsSysCtrlEndOfDischargeTimeoutReached = eSysId_UpsSysCtrlPfcOpModeOneOffOp + 1
eSysId_UpsSysCtrlPowerCabinetRedundancySetting = eSysId_UpsSysCtrlEndOfDischargeTimeoutReached + 1
eSysId_UpsSysCtrlPowerCabinetPresentSetting = eSysId_UpsSysCtrlPowerCabinetRedundancySetting + 1
eSysId_UpsSysCtrlPowerSectionAvailableBF = eSysId_UpsSysCtrlPowerCabinetPresentSetting + 1
eSysId_UpsSysCtrlCbusMcComStatus = eSysId_UpsSysCtrlPowerSectionAvailableBF + 1
eSysId_UpsSysCtrlUpsOpModeCmd = eSysId_UpsSysCtrlCbusMcComStatus + 1
eSysId_UpsSysCtrlUpsOffButtonAct = eSysId_UpsSysCtrlUpsOpModeCmd + 1
eSysId_UpsSysCtrlUpsOnButtonAct = eSysId_UpsSysCtrlUpsOffButtonAct + 1
eSysId_UpsSysCtrlOutputContactorOpenRequest = eSysId_UpsSysCtrlUpsOnButtonAct + 1
eSysId_UpsSysCtrlUpsModeUserReq = eSysId_UpsSysCtrlOutputContactorOpenRequest + 1
eSysId_UpsSysCtrlLi_IonBattTempEstimatorStatus = eSysId_UpsSysCtrlUpsModeUserReq + 1
eSysId_UpsSysCtrlBattTestStatus = eSysId_UpsSysCtrlLi_IonBattTempEstimatorStatus + 1
eSysId_UpsSysCtrlBatteryConnected = eSysId_UpsSysCtrlBattTestStatus + 1
eSysId_UpsSysCtrlPfcRegWindUp = eSysId_UpsSysCtrlBatteryConnected + 1
eSysId_UpsSysCtrlBurnInStatus = eSysId_UpsSysCtrlPfcRegWindUp + 1
eSysId_UpsSysCtrlChgSysCtrlOpMode = eSysId_UpsSysCtrlBurnInStatus + 1
eSysId_UpsSysCtrlUpsOnButtonAccepted = eSysId_UpsSysCtrlChgSysCtrlOpMode + 1
eSysId_UpsSysCtrlUpsOffButtonAccepted = eSysId_UpsSysCtrlUpsOnButtonAccepted + 1
eSysId_UpsSysCtrlConfirmRedundancyLost = eSysId_UpsSysCtrlUpsOffButtonAccepted + 1
eSysId_UpsSysCtrlConfirmTurnLoadOff = eSysId_UpsSysCtrlConfirmRedundancyLost + 1
eSysId_UpsSysCtrlInverterOffDueToOffButton = eSysId_UpsSysCtrlConfirmTurnLoadOff + 1
eSysId_UpsSysCtrlUpsOverLoad = eSysId_UpsSysCtrlInverterOffDueToOffButton + 1
eSysId_UpsSysCtrlUpsOpModeCorrected = eSysId_UpsSysCtrlUpsOverLoad + 1
eSysId_UpsSysCtrlUpsPowerRating = eSysId_UpsSysCtrlUpsOpModeCorrected + 1
eSysId_UpsSysCtrlEnergyStorage = eSysId_UpsSysCtrlUpsPowerRating + 1
eSysId_UpsSysCtrlFrequencyConverterModeSetting = eSysId_UpsSysCtrlEnergyStorage + 1
eSysId_EconvMode = eSysId_UpsSysCtrlFrequencyConverterModeSetting + 1
eSysId_ReturnFromMaintenanceBypassSetting = eSysId_EconvMode + 1
eSysId_ReturnFromMaintenanceBypassForcedLockStatus = eSysId_ReturnFromMaintenanceBypassSetting + 1
eSysId_ReturnFromMaintenanceBypassClearForcedLock = eSysId_ReturnFromMaintenanceBypassForcedLockStatus + 1
eSysId_UpsSysCtrlExitEcoModeDueToLowDcBus = eSysId_ReturnFromMaintenanceBypassClearForcedLock + 1
eSysId_ParMastrSelctParMastermode = eSysId_UpsSysCtrlExitEcoModeDueToLowDcBus + 1
eSysId_ParMastrSelctMasterCollissionError = eSysId_ParMastrSelctParMastermode + 1
eSysId_ParMastrSelctNoMasterPresent = eSysId_ParMastrSelctMasterCollissionError + 1
eSysId_ParMastrSelctMasterId = eSysId_ParMastrSelctNoMasterPresent + 1
eSysId_MQTTInverterOffCommand = eSysId_ParMastrSelctMasterId + 1
eSysId_MQTTInverterOnCommand = eSysId_MQTTInverterOffCommand + 1
eSysId_MQTTInverterToStaticBypassCommand = eSysId_MQTTInverterOnCommand + 1
eSysId_MQTTStaticBypassToInverterCommand = eSysId_MQTTInverterToStaticBypassCommand + 1
eSysId_MQTTConfirmTurnInverterOffCommand = eSysId_MQTTStaticBypassToInverterCommand + 1
eSysId_MQTTSwitchgearSettingUIB = eSysId_MQTTConfirmTurnInverterOffCommand + 1
eSysId_MQTTSwitchgearSettingSSIB = eSysId_MQTTSwitchgearSettingUIB + 1
eSysId_MQTTSwitchgearSettingUOB = eSysId_MQTTSwitchgearSettingSSIB + 1
eSysId_MQTTSwitchgearSettingMBB = eSysId_MQTTSwitchgearSettingUOB + 1
eSysId_MQTTSwitchgearSettingSIB = eSysId_MQTTSwitchgearSettingMBB + 1
eSysId_MQTTSwitchgearSettingIMB = eSysId_MQTTSwitchgearSettingSIB + 1
eSysId_MQTTSwitchgearSettingRIMB = eSysId_MQTTSwitchgearSettingIMB + 1
eSysId_MQTTSwitchgearStatusUIBClosed = eSysId_MQTTSwitchgearSettingRIMB + 1
eSysId_MQTTSwitchgearStatusSSIBClosed = eSysId_MQTTSwitchgearStatusUIBClosed + 1
eSysId_MQTTSwitchgearStatusUOBClosed = eSysId_MQTTSwitchgearStatusSSIBClosed + 1
eSysId_MQTTSwitchgearStatusMBBClosed = eSysId_MQTTSwitchgearStatusUOBClosed + 1
eSysId_MQTTSwitchgearStatusSIBClosed = eSysId_MQTTSwitchgearStatusMBBClosed + 1
eSysId_MQTTSwitchgearStatusIMBClosed = eSysId_MQTTSwitchgearStatusSIBClosed + 1
eSysId_MQTTSwitchgearStatusRIMBClosed = eSysId_MQTTSwitchgearStatusIMBClosed + 1
eSysId_ParSysCtrlTransition = eSysId_MQTTSwitchgearStatusRIMBClosed + 1
eSysId_ParSysCtrlReducedOverloadStepIndex = eSysId_ParSysCtrlTransition + 1
eSysId_ParSysCtrlSystemLocked = eSysId_ParSysCtrlReducedOverloadStepIndex + 1
eSysId_SysInhibitTransferFromBypass = eSysId_ParSysCtrlSystemLocked + 1
eSysId_RelayControlExtUseStaticBypassStandbyAct = eSysId_SysInhibitTransferFromBypass + 1
eSysId_InhibitTransferFromBypass = eSysId_RelayControlExtUseStaticBypassStandbyAct + 1
eSysId_ParUpsMgrOpMode = eSysId_InhibitTransferFromBypass + 1
eSysId_ParUpsMgrParSysTurnOffUpsOk = eSysId_ParUpsMgrOpMode + 1
eSysId_ParUpsMgrParMixedMode = eSysId_ParUpsMgrParSysTurnOffUpsOk + 1
eSysId_ParUpsMgrParallelRedundancyLost = eSysId_ParUpsMgrParMixedMode + 1
eSysId_ParUpsMgrTrans = eSysId_ParUpsMgrParallelRedundancyLost + 1
eSysId_ParUpsDevMgrOpMode = eSysId_ParUpsMgrTrans + 1
eSysId_ParExtSyncSourceErrorStatus = eSysId_ParUpsDevMgrOpMode + 1
eSysId_ParSibClosed = eSysId_ParExtSyncSourceErrorStatus + 1
eSysId_ParUibClosed = eSysId_ParSibClosed + 1
eSysId_ParSsibClosed = eSysId_ParUibClosed + 1
eSysId_ParallelUnitPresent = eSysId_ParSsibClosed + 1
eSysId_ParSysMains1CurRmsL1 = eSysId_ParallelUnitPresent + 1
eSysId_ParSysMains1CurRmsL2 = eSysId_ParSysMains1CurRmsL1 + 1
eSysId_ParSysMains1CurRmsL3 = eSysId_ParSysMains1CurRmsL2 + 1
eSysId_ParSysMains2CurRmsL1 = eSysId_ParSysMains1CurRmsL3 + 1
eSysId_ParSysMains2CurRmsL2 = eSysId_ParSysMains2CurRmsL1 + 1
eSysId_ParSysMains2CurRmsL3 = eSysId_ParSysMains2CurRmsL2 + 1
eSysId_ParSysOutCurRmsL1 = eSysId_ParSysMains2CurRmsL3 + 1
eSysId_ParSysOutCurRmsL2 = eSysId_ParSysOutCurRmsL1 + 1
eSysId_ParSysOutCurRmsL3 = eSysId_ParSysOutCurRmsL2 + 1
eSysId_ParSysOutApparentPwr = eSysId_ParSysOutCurRmsL3 + 1
eSysId_ParSysOutApparentPwrL1 = eSysId_ParSysOutApparentPwr + 1
eSysId_ParSysOutApparentPwrL2 = eSysId_ParSysOutApparentPwrL1 + 1
eSysId_ParSysOutApparentPwrL3 = eSysId_ParSysOutApparentPwrL2 + 1
eSysId_TimeReceived = eSysId_ParSysOutApparentPwrL3 + 1
eSysId_ParAddressError = eSysId_TimeReceived + 1
eSysId_parallelUnitCompatibility = eSysId_ParAddressError + 1
eSysId_parallelSynchronizationStatus = eSysId_parallelUnitCompatibility + 1
eSysId_SysOpModeParMaster = eSysId_parallelSynchronizationStatus + 1
eSysId_Pbus1CanComOk = eSysId_SysOpModeParMaster + 1
eSysId_Pbus2CanComOk = eSysId_Pbus1CanComOk + 1
eSysId_AlarmParCriticalStatus = eSysId_Pbus2CanComOk + 1
eSysId_AlarmParInfo = eSysId_AlarmParCriticalStatus + 1
eSysId_AlarmParWarningStatus = eSysId_AlarmParInfo + 1
eSysId_ParMains1SyncSourceErrorStatus = eSysId_AlarmParWarningStatus + 1
eSysId_ParSysActivePwrL1 = eSysId_ParMains1SyncSourceErrorStatus + 1
eSysId_ParSysActivePwrL2 = eSysId_ParSysActivePwrL1 + 1
eSysId_ParSysActivePwrL3 = eSysId_ParSysActivePwrL2 + 1
eSysId_ParMixedUpsSizeError = eSysId_ParSysActivePwrL3 + 1
eSysId_ParBreakerPresent = eSysId_ParMixedUpsSizeError + 1
eSysId_ParBbClosed = eSysId_ParBreakerPresent + 1
eSysId_AlarmParInfoStatus = eSysId_ParBbClosed + 1
eSysId_ParIntBypassSyncSourceErrorStatus = eSysId_AlarmParInfoStatus + 1
eSysId_OutActivePower = eSysId_ParIntBypassSyncSourceErrorStatus + 1
eSysId_TimeSet = eSysId_OutActivePower + 1
eSysId_OutTotalApparentPower = eSysId_TimeSet + 1
eSysId_AlarmCriticalAct = eSysId_OutTotalApparentPower + 1
eSysId_AlarmWarningAct = eSysId_AlarmCriticalAct + 1
eSysId_AlarmInfoAct = eSysId_AlarmWarningAct + 1
eSysId_UpsPowerRatingSetting = eSysId_AlarmInfoAct + 1
eSysId_MQTTEcoModeScheduling = eSysId_UpsPowerRatingSetting + 1
eSysId_EcoModeStartDay = eSysId_MQTTEcoModeScheduling + 1
eSysId_EcoModeStartTime = eSysId_EcoModeStartDay + 1
eSysId_EcoModeStopDay = eSysId_EcoModeStartTime + 1
eSysId_EcoModeStopTime = eSysId_EcoModeStopDay + 1
eSysId_EcoModeProgramEnable = eSysId_EcoModeStopTime + 1
eSysId_MQTTMainsConfigurationSetting = eSysId_EcoModeProgramEnable + 1
eSysId_CommonInputBreakerPresentSetting = eSysId_MQTTMainsConfigurationSetting + 1
eSysId_UpsSystemFWversionMajor = eSysId_CommonInputBreakerPresentSetting + 1
eSysId_UpsSystemFWversionMinor = eSysId_UpsSystemFWversionMajor + 1
eSysId_UpsSystemFWversionDeviation = eSysId_UpsSystemFWversionMinor + 1
eSysId_UpsSystemFWversionBuild = eSysId_UpsSystemFWversionDeviation + 1
eSysId_UpsSerialNumber = eSysId_UpsSystemFWversionBuild + 1
eSysId_UpsSerialNumberUps1 = eSysId_UpsSerialNumber + 1
eSysId_UpsSerialNumberUps2 = eSysId_UpsSerialNumberUps1 + 1
eSysId_UpsSerialNumberUps3 = eSysId_UpsSerialNumberUps2 + 1
eSysId_UpsSerialNumberUps4 = eSysId_UpsSerialNumberUps3 + 1
eSysId_UpsSerialNumberUps5 = eSysId_UpsSerialNumberUps4 + 1
eSysId_Pbus1Rs485Error = eSysId_UpsSerialNumberUps5 + 1
eSysId_Pbus2Rs485Error = eSysId_Pbus1Rs485Error + 1
eSysId_BreakerMgrUibClosed = eSysId_Pbus2Rs485Error + 1
eSysId_BreakerMgrSsibClosed = eSysId_BreakerMgrUibClosed + 1
eSysId_BreakerMgrUobClosed = eSysId_BreakerMgrSsibClosed + 1
eSysId_BreakerMgrMbbClosed = eSysId_BreakerMgrUobClosed + 1
eSysId_BreakerMgrSibClosed = eSysId_BreakerMgrMbbClosed + 1
eSysId_BreakerMgrImbClosed = eSysId_BreakerMgrSibClosed + 1
eSysId_BreakerMgrRimbClosed = eSysId_BreakerMgrImbClosed + 1
eSysId_SysReqHandlerSysMaintenanceRequest = eSysId_BreakerMgrRimbClosed + 1
eSysId_SysReqHandlerSysForcedStaticBypassduetoVQDErrorRequest = eSysId_SysReqHandlerSysMaintenanceRequest + 1
eSysId_SysReqHandlerForcedStaticBypassRequest = eSysId_SysReqHandlerSysForcedStaticBypassduetoVQDErrorRequest + 1
eSysId_SysReqHandlerForcedStaticBypassDueToOverloadRequest = eSysId_SysReqHandlerForcedStaticBypassRequest + 1
eSysId_SysReqHandlerForcedStaticBypassDueToOffButtonRequest = eSysId_SysReqHandlerForcedStaticBypassDueToOverloadRequest + 1
eSysId_SysReqHandlerRequestedStaticBypassRequest = eSysId_SysReqHandlerForcedStaticBypassDueToOffButtonRequest + 1
eSysId_SysReqHandlerInverterOnRequest = eSysId_SysReqHandlerRequestedStaticBypassRequest + 1
eSysId_SysReqHandlerInverterOffRequest = eSysId_SysReqHandlerInverterOnRequest + 1
eSysId_SysReqHandlerBypassBurnInTestRequest = eSysId_SysReqHandlerInverterOffRequest + 1
eSysId_SysReqHandlerSysOpModeReq = eSysId_SysReqHandlerBypassBurnInTestRequest + 1
eSysId_SysBypassCtrlTransition = eSysId_SysReqHandlerSysOpModeReq + 1
eSysId_SysBypassCtrlSbsReadyToTurnOn = eSysId_SysBypassCtrlTransition + 1
eSysId_EcoModeReqBypassAct = eSysId_SysBypassCtrlSbsReadyToTurnOn + 1
eSysId_EcoModeHandlerUpsInEcoMode = eSysId_EcoModeReqBypassAct + 1
eSysId_EcoModeHandlerOpMode = eSysId_EcoModeHandlerUpsInEcoMode + 1
eSysId_EcoModeAllowedStatus = eSysId_EcoModeHandlerOpMode + 1
eSysId_EcoModeHandlerState = eSysId_EcoModeAllowedStatus + 1
eSysId_EcoModeBasicAllowed = eSysId_EcoModeHandlerState + 1
eSysId_MQTTHighEfficiencyModeSetting = eSysId_EcoModeBasicAllowed + 1
eSysId_MQTTHighEfficiencyModeEnabled = eSysId_MQTTHighEfficiencyModeSetting + 1
eSysId_InverterStandbyActive = eSysId_MQTTHighEfficiencyModeEnabled + 1
eSysId_ParSmartBatOpCtrlOpMode = eSysId_InverterStandbyActive + 1
eSysId_SbsOpMode = eSysId_ParSmartBatOpCtrlOpMode + 1
eSysId_SysOpMode = eSysId_SbsOpMode + 1
eSysId_SysOpModeCorrected = eSysId_SysOpMode + 1
eSysId_ParUpsReadyToTurnOn = eSysId_SysOpModeCorrected + 1
eSysId_MinUpsToSupplyLoadSetting = eSysId_ParUpsReadyToTurnOn + 1
eSysId_MinUpsToSupplyLoadPresent = eSysId_MinUpsToSupplyLoadSetting + 1
eSysId_NotEnoughUpsReadyToTurnOn = eSysId_MinUpsToSupplyLoadPresent + 1
eSysId_SysBypassOpMode = eSysId_NotEnoughUpsReadyToTurnOn + 1
eSysId_SysBypassOpModeCmd = eSysId_SysBypassOpMode + 1
eSysId_StaticBypassWithBreakRequired = eSysId_SysBypassOpModeCmd + 1
eSysId_ParUobClosed = eSysId_StaticBypassWithBreakRequired + 1
eSysId_ParMbbClosed = eSysId_ParUobClosed + 1
eSysId_ParImbClosed = eSysId_ParMbbClosed + 1
eSysId_ParInhibitTransferFromBypass = eSysId_ParImbClosed + 1
eSysId_ParRedundancy = eSysId_ParInhibitTransferFromBypass + 1
eSysId_ParUpsOutputOverload = eSysId_ParRedundancy + 1
eSysId_ParUpsPowerRatings = eSysId_ParUpsOutputOverload + 1
eSysId_UpsOpModeReq = eSysId_ParUpsPowerRatings + 1
eSysId_ParUpsReadyForNormalOp = eSysId_UpsOpModeReq + 1
eSysId_AdvBattOpMgrDisabledAct = eSysId_ParUpsReadyForNormalOp + 1
eSysId_FactoryTestModeEn = eSysId_AdvBattOpMgrDisabledAct + 1
eSysId_TransToStaticBypOnEpoSetting = eSysId_FactoryTestModeEn + 1
eSysId_ParOperationRedundancyModeSetting = eSysId_TransToStaticBypOnEpoSetting + 1
eSysId_UpsAutoStartEnSetting = eSysId_ParOperationRedundancyModeSetting + 1
eSysId_MainsDualFeedPresentSetting = eSysId_UpsAutoStartEnSetting + 1
eSysId_EconvHamCompEnable = eSysId_MainsDualFeedPresentSetting + 1
eSysId_CommonBatterySetting = eSysId_EconvHamCompEnable + 1
eSysId_UpsIsPreferredExtSyncSourceSetting = eSysId_CommonBatterySetting + 1
eSysId_FrequencyConverterModeSetting = eSysId_UpsIsPreferredExtSyncSourceSetting + 1
eSysId_UpsIsFixedExtSyncMasterSetting = eSysId_FrequencyConverterModeSetting + 1
eSysId_ParUpsIsFixedExtSyncMaster = eSysId_UpsIsFixedExtSyncMasterSetting + 1
eSysId_UpsMinFwMajor = eSysId_ParUpsIsFixedExtSyncMaster + 1
eSysIdSyncSourceSysCtrlTransition = eSysId_UpsMinFwMajor + 1
eSysIdSyncSourceSysCtrlOpMode = eSysIdSyncSourceSysCtrlTransition + 1
eSysIdSyncSourceSysCtrlBypassError = eSysIdSyncSourceSysCtrlOpMode + 1
eSysIdSyncSourceSysCtrlMains1Error = eSysIdSyncSourceSysCtrlBypassError + 1
eSysIdSyncSourceSysCtrlExtSyncInvPllLockFailed = eSysIdSyncSourceSysCtrlMains1Error + 1
eSysIdSyncSourceSysCtrlExtSyncSourceError = eSysIdSyncSourceSysCtrlExtSyncInvPllLockFailed + 1
eSysIdSyncSourceSysCtrlExtSyncSourceErrorCustom = eSysIdSyncSourceSysCtrlExtSyncSourceError + 1
eSysIdSyncSourceSysCtrlForceExtSyncOut = eSysIdSyncSourceSysCtrlExtSyncSourceErrorCustom + 1
eSysIdSyncSourceSysCtrlExtSyncReqOut = eSysIdSyncSourceSysCtrlForceExtSyncOut + 1
eSysId_InvA1 = eSysIdSyncSourceSysCtrlExtSyncReqOut + 1
eSysId_InvA2 = eSysId_InvA1 + 1
eSysId_InvB0 = eSysId_InvA2 + 1
eSysId_InvB1 = eSysId_InvB0 + 1
eSysId_InvB2 = eSysId_InvB1 + 1
eSysId_InvK1 = eSysId_InvB2 + 1
eSysId_DisableClassBoost = eSysId_InvK1 + 1
eSysId_OutVolComp = eSysId_DisableClassBoost + 1
eSysId_InvPllSyncError = eSysId_OutVolComp + 1
eSysId_InvPllSynchronizationStatus = eSysId_InvPllSyncError + 1
eSysId_InvPllInvPllLocked = eSysId_InvPllSynchronizationStatus + 1
eSysId_InvCurLimAct = eSysId_InvPllInvPllLocked + 1
eSysId_InvLoadAboveLim = eSysId_InvCurLimAct + 1
eSysId_EnInvLimit = eSysId_InvLoadAboveLim + 1
eSysId_ChgInCurLim = eSysId_EnInvLimit + 1
eSysId_SelChgVolLog = eSysId_ChgInCurLim + 1
eSysId_SelChgCurLog = eSysId_SelChgVolLog + 1
eSysId_UpsChgOn = eSysId_SelChgCurLog + 1
eSysId_VqdRmsSts = eSysId_UpsChgOn + 1
eSysId_VqdRmsPhaseSts = eSysId_VqdRmsSts + 1
eSysId_VqdMissingPhSts = eSysId_VqdRmsPhaseSts + 1
eSysId_VqdFreqSts = eSysId_VqdMissingPhSts + 1
eSysId_VqdNeuDispSts = eSysId_VqdFreqSts + 1
eSysId_VqdPhRotSts = eSysId_VqdNeuDispSts + 1
eSysId_VqdPllSts = eSysId_VqdPhRotSts + 1
eSysId_VqdDcOnOutSts = eSysId_VqdPllSts + 1
eSysId_VqdBattSts = eSysId_VqdDcOnOutSts + 1
eSysId_VqdWaveformSts = eSysId_VqdBattSts + 1
eSysId_VqdWaveformPhaseSts = eSysId_VqdWaveformSts + 1
eSysId_VqdMains1VolPhPhRms = eSysId_VqdWaveformPhaseSts + 1
eSysId_VqdMains1VolRms = eSysId_VqdMains1VolPhPhRms + 1
eSysId_VqdMains2VolPhPhRms = eSysId_VqdMains1VolRms + 1
eSysId_VqdMains2VolRms = eSysId_VqdMains2VolPhPhRms + 1
eSysId_VqdExtSyncVolRms = eSysId_VqdMains2VolRms + 1
eSysId_VqdOutVolPhPhRms = eSysId_VqdExtSyncVolRms + 1
eSysId_VqdOutVolRms = eSysId_VqdOutVolPhPhRms + 1
eSysId_VqdOutVolAvg = eSysId_VqdOutVolRms + 1
eSysId_VqdOutVolPhPhAvg = eSysId_VqdOutVolAvg + 1
eSysId_VqdNeuChgVolAvg = eSysId_VqdOutVolPhPhAvg + 1
eSysId_PmcVqdRmsSts = eSysId_VqdNeuChgVolAvg + 1
eSysId_PmcVqdRmsPhaseSts = eSysId_PmcVqdRmsSts + 1
eSysId_PmcVqdMissingPhSts = eSysId_PmcVqdRmsPhaseSts + 1
eSysId_PmcVqdNeuDispSts = eSysId_PmcVqdMissingPhSts + 1
eSysId_PmcVqdDcBusSts = eSysId_PmcVqdNeuDispSts + 1
eSysId_PmcVqdFreqSts = eSysId_PmcVqdDcBusSts + 1
eSysId_PmcVqdPhRotSts = eSysId_PmcVqdFreqSts + 1
eSysId_PmcVqdPllSts = eSysId_PmcVqdPhRotSts + 1
eSysId_PmcVqdDcOnOutSts = eSysId_PmcVqdPllSts + 1
eSysId_PmcVqdBattSts = eSysId_PmcVqdDcOnOutSts + 1
eSysId_PmcVqdWaveformSts = eSysId_PmcVqdBattSts + 1
eSysId_PmcVqdWaveformPhaseSts = eSysId_PmcVqdWaveformSts + 1
eSysId_SelftestState = eSysId_PmcVqdWaveformPhaseSts + 1
eSysId_PmcSelftestState = eSysId_SelftestState + 1
eSysId_PmcHsTemp1Min = eSysId_PmcSelftestState + 1
eSysId_PmcHsTemp1Mean = eSysId_PmcHsTemp1Min + 1
eSysId_PmcHsTemp1Max = eSysId_PmcHsTemp1Mean + 1
eSysId_PmcHsTemp2Min = eSysId_PmcHsTemp1Max + 1
eSysId_PmcHsTemp2Mean = eSysId_PmcHsTemp2Min + 1
eSysId_PmcHsTemp2Max = eSysId_PmcHsTemp2Mean + 1
eSysId_PmcAirInletTemp = eSysId_PmcHsTemp2Max + 1
eSysId_PmcAirOutletTemp = eSysId_PmcAirInletTemp + 1
eSysId_PmcFanStates = eSysId_PmcAirOutletTemp + 1
eSysId_PmcFanSpeed = eSysId_PmcFanStates + 1
eSysId_PmcMainsRlyEn = eSysId_PmcFanSpeed + 1
eSysId_PmcChgRlyEn = eSysId_PmcMainsRlyEn + 1
eSysId_PmcInvRlyEn = eSysId_PmcChgRlyEn + 1
eSysId_SysDataMains1VolPhPhRms = eSysId_PmcInvRlyEn + 1
eSysId_SysDataMains1VolRms = eSysId_SysDataMains1VolPhPhRms + 1
eSysId_SysDataMains2VolRms = eSysId_SysDataMains1VolRms + 1
eSysId_SysDataMains2VolPhPhRms = eSysId_SysDataMains2VolRms + 1
eSysId_SysDataOutVolRms = eSysId_SysDataMains2VolPhPhRms + 1
eSysId_SysDataOutVolPhPhRms = eSysId_SysDataOutVolRms + 1
eSysId_SysDataBattVol = eSysId_SysDataOutVolPhPhRms + 1
eSysId_SysDataBattVolTotal = eSysId_SysDataBattVol + 1
eSysId_SysDataMains1CurRms = eSysId_SysDataBattVolTotal + 1
eSysId_SysDataMains2CurRms = eSysId_SysDataMains1CurRms + 1
eSysId_SysDataOutCurRms = eSysId_SysDataMains2CurRms + 1
eSysId_SysDataBattCur = eSysId_SysDataOutCurRms + 1
eSysId_SysDataBattCurMax = eSysId_SysDataBattCur + 1
eSysId_SysDataMains1Freq = eSysId_SysDataBattCurMax + 1
eSysId_SysDataMains2Freq = eSysId_SysDataMains1Freq + 1
eSysId_SysDataOutFreq = eSysId_SysDataMains2Freq + 1
eSysId_SysDataMains1PwrFactor = eSysId_SysDataOutFreq + 1
eSysId_SysDataMains2PwrFactor = eSysId_SysDataMains1PwrFactor + 1
eSysId_SysDataOutPwrFactor = eSysId_SysDataMains2PwrFactor + 1
eSysId_SysDataMains1RealPwr = eSysId_SysDataOutPwrFactor + 1
eSysId_SysDataMains2RealPwr = eSysId_SysDataMains1RealPwr + 1
eSysId_SysDataOutRealPwr = eSysId_SysDataMains2RealPwr + 1
eSysId_SysDataBattRealPwr = eSysId_SysDataOutRealPwr + 1
eSysId_SysDataBattRealPwrSum = eSysId_SysDataBattRealPwr + 1
eSysId_SysDataMains1RealPwrSum = eSysId_SysDataBattRealPwrSum + 1
eSysId_SysDataMains2RealPwrSum = eSysId_SysDataMains1RealPwrSum + 1
eSysId_SysDataOutRealPwrSum = eSysId_SysDataMains2RealPwrSum + 1
eSysId_SysDataMains1AppPwr = eSysId_SysDataOutRealPwrSum + 1
eSysId_SysDataMains2AppPwr = eSysId_SysDataMains1AppPwr + 1
eSysId_SysDataOutAppPwr = eSysId_SysDataMains2AppPwr + 1
eSysId_SysDataMains1AppPwrSum = eSysId_SysDataOutAppPwr + 1
eSysId_SysDataMains2AppPwrSum = eSysId_SysDataMains1AppPwrSum + 1
eSysId_SysDataOutAppPwrSum = eSysId_SysDataMains2AppPwrSum + 1
eSysId_SysDataOutAppPwrPct = eSysId_SysDataOutAppPwrSum + 1
eSysId_SysDataInEnergy = eSysId_SysDataOutAppPwrPct + 1
eSysId_SysDataOutEnergy = eSysId_SysDataInEnergy + 1
eSysId_SysDataOutLoadRate = eSysId_SysDataOutEnergy + 1
eSysId_SysDataOutLoadRateMax = eSysId_SysDataOutLoadRate + 1
eSysId_SysDataMains1LoadRate = eSysId_SysDataOutLoadRateMax + 1
eSysId_SysDataMains2LoadRate = eSysId_SysDataMains1LoadRate + 1
eSysId_SysDataPmcInvLoadRate = eSysId_SysDataMains2LoadRate + 1
eSysId_SysDataOutCrestFactor = eSysId_SysDataPmcInvLoadRate + 1
eSysId_SysDataOutPeakCur = eSysId_SysDataOutCrestFactor + 1
eSysId_SysDataMains1PeakCur = eSysId_SysDataOutPeakCur + 1
eSysId_SysDataMains2PeakCur = eSysId_SysDataMains1PeakCur + 1
eSysId_SysDataOutCurThd = eSysId_SysDataMains2PeakCur + 1
eSysId_SysDataOutNeuCurRms = eSysId_SysDataOutCurThd + 1
eSysId_OutLoadAboveCustomerLim = eSysId_SysDataOutNeuCurRms + 1
eSysId_OutLoadCustomerLim = eSysId_OutLoadAboveCustomerLim + 1
eSysId_SysDataParSysTotalMains1CurRms = eSysId_OutLoadCustomerLim + 1
eSysId_SysDataParSysTotalMains2CurRms = eSysId_SysDataParSysTotalMains1CurRms + 1
eSysId_SysDataParSysTotalOutCurRms = eSysId_SysDataParSysTotalMains2CurRms + 1
eSysId_SysDataParSysTotalOutAppPwrSum = eSysId_SysDataParSysTotalOutCurRms + 1
eSysId_SysDataParSysTotalOutAppPwrPhSum = eSysId_SysDataParSysTotalOutAppPwrSum + 1
eSysId_SysDataParSysTotalOutRealPwrSum = eSysId_SysDataParSysTotalOutAppPwrPhSum + 1
eSysId_SysDataParTotalOutLoad = eSysId_SysDataParSysTotalOutRealPwrSum + 1
eSysId_SysDataParSysTotalOutRealPwr = eSysId_SysDataParTotalOutLoad + 1
eSysId_SysDataAmbientTemp = eSysId_SysDataParSysTotalOutRealPwr + 1
eSysId_SysDataOverloadDueToHighAmbTemp = eSysId_SysDataAmbientTemp + 1
eSysId_UcMains1VolSnsScaleVtoQ = eSysId_SysDataOverloadDueToHighAmbTemp + 1
eSysId_UcMains1VolSnsScaleQtoV = eSysId_UcMains1VolSnsScaleVtoQ + 1
eSysId_UcMains1VolSnsScaleVtoQmul2Pow16 = eSysId_UcMains1VolSnsScaleQtoV + 1
eSysId_UcMains1VolSnsScaleQtoVmul2Pow16 = eSysId_UcMains1VolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcMains2VolSnsScaleVtoQ = eSysId_UcMains1VolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcMains2VolSnsScaleQtoV = eSysId_UcMains2VolSnsScaleVtoQ + 1
eSysId_UcMains2VolSnsScaleVtoQmul2Pow16 = eSysId_UcMains2VolSnsScaleQtoV + 1
eSysId_UcMains2VolSnsScaleQtoVmul2Pow16 = eSysId_UcMains2VolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcOutVolSnsScaleVtoQ = eSysId_UcMains2VolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcOutVolSnsScaleQtoV = eSysId_UcOutVolSnsScaleVtoQ + 1
eSysId_UcOutVolSnsScaleVtoQmul2Pow16 = eSysId_UcOutVolSnsScaleQtoV + 1
eSysId_UcOutVolSnsScaleQtoVmul2Pow16 = eSysId_UcOutVolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcExtSyncVolSnsScaleVtoQ = eSysId_UcOutVolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcExtSyncVolSnsScaleQtoV = eSysId_UcExtSyncVolSnsScaleVtoQ + 1
eSysId_UcExtSyncVolSnsScaleVtoQmul2Pow16 = eSysId_UcExtSyncVolSnsScaleQtoV + 1
eSysId_UcExtSyncVolSnsScaleQtoVmul2Pow16 = eSysId_UcExtSyncVolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcBattVolSnsScaleVtoQ = eSysId_UcExtSyncVolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcBattVolSnsScaleQtoV = eSysId_UcBattVolSnsScaleVtoQ + 1
eSysId_UcBattVolSnsScaleVtoQmul2Pow16 = eSysId_UcBattVolSnsScaleQtoV + 1
eSysId_UcBattVolSnsScaleQtoVmul2Pow16 = eSysId_UcBattVolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcNeuChgVolSnsScaleVtoQ = eSysId_UcBattVolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcNeuChgVolSnsScaleQtoV = eSysId_UcNeuChgVolSnsScaleVtoQ + 1
eSysId_UcNeuChgVolSnsScaleVtoQmul2Pow16 = eSysId_UcNeuChgVolSnsScaleQtoV + 1
eSysId_UcNeuChgVolSnsScaleQtoVmul2Pow16 = eSysId_UcNeuChgVolSnsScaleVtoQmul2Pow16 + 1
eSysId_UcOutCurSnsScaleItoQ = eSysId_UcNeuChgVolSnsScaleQtoVmul2Pow16 + 1
eSysId_UcOutCurSnsScaleQtoI = eSysId_UcOutCurSnsScaleItoQ + 1
eSysId_UcOutCurSnsScaleItoQmul2Pow16 = eSysId_UcOutCurSnsScaleQtoI + 1
eSysId_UcOutCurSnsScaleQtoImul2Pow16 = eSysId_UcOutCurSnsScaleItoQmul2Pow16 + 1
eSysId_SysAppPwrRating = eSysId_UcOutCurSnsScaleQtoImul2Pow16 + 1
eSysId_SysPowerFactor = eSysId_SysAppPwrRating + 1
eSysId_SysCrestFactor = eSysId_SysPowerFactor + 1
eSysId_UcMaxChgVolLevel = eSysId_SysCrestFactor + 1
eSysId_UcMinChgVolLevel = eSysId_UcMaxChgVolLevel + 1
eSysId_AlphaRfiFilterMains1 = eSysId_UcMinChgVolLevel + 1
eSysId_AlphaRfiFilterInv = eSysId_AlphaRfiFilterMains1 + 1
eSysId_AlphaRfiFilterMains2 = eSysId_AlphaRfiFilterInv + 1
eSysId_PmcInvCurSnsL1 = eSysId_AlphaRfiFilterMains2 + 1
eSysId_PmcInvCurSnsL2 = eSysId_PmcInvCurSnsL1 + 1
eSysId_PmcInvCurSnsL3 = eSysId_PmcInvCurSnsL2 + 1
eSysId_PmcInvCurRmsL1 = eSysId_PmcInvCurSnsL3 + 1
eSysId_PmcInvCurRmsL2 = eSysId_PmcInvCurRmsL1 + 1
eSysId_PmcInvCurRmsL3 = eSysId_PmcInvCurRmsL2 + 1
eSysId_PmcMains1CurRmsL1 = eSysId_PmcInvCurRmsL3 + 1
eSysId_PmcMains1CurRmsL2 = eSysId_PmcMains1CurRmsL1 + 1
eSysId_PmcMains1CurRmsL3 = eSysId_PmcMains1CurRmsL2 + 1
eSysId_PmcMains1PwrFactL1 = eSysId_PmcMains1CurRmsL3 + 1
eSysId_PmcMains1PwrFactL2 = eSysId_PmcMains1PwrFactL1 + 1
eSysId_PmcMains1PwrFactL3 = eSysId_PmcMains1PwrFactL2 + 1
eSysId_PmcMains1RealPwrL1 = eSysId_PmcMains1PwrFactL3 + 1
eSysId_PmcMains1RealPwrL2 = eSysId_PmcMains1RealPwrL1 + 1
eSysId_PmcMains1RealPwrL3 = eSysId_PmcMains1RealPwrL2 + 1
eSysId_PmcMains1PeakCurL1 = eSysId_PmcMains1RealPwrL3 + 1
eSysId_PmcMains1PeakCurL2 = eSysId_PmcMains1PeakCurL1 + 1
eSysId_PmcMains1PeakCurL3 = eSysId_PmcMains1PeakCurL2 + 1
eSysId_PmcBattCurPos = eSysId_PmcMains1PeakCurL3 + 1
eSysId_PmcBattCurNeg = eSysId_PmcBattCurPos + 1
eSysId_PmcInvCurSnsScaleItoQ = eSysId_PmcBattCurNeg + 1
eSysId_PmcInvCurSnsScaleQtoI = eSysId_PmcInvCurSnsScaleItoQ + 1
eSysId_PmcInvCurSnsScaleItoQmul2Pow16 = eSysId_PmcInvCurSnsScaleQtoI + 1
eSysId_PmcInvCurSnsScaleQtoImul2Pow16 = eSysId_PmcInvCurSnsScaleItoQmul2Pow16 + 1
eSysId_PmcOutVolRmsL1 = eSysId_PmcInvCurSnsScaleQtoImul2Pow16 + 1
eSysId_PmcOutVolRmsL2 = eSysId_PmcOutVolRmsL1 + 1
eSysId_PmcOutVolRmsL3 = eSysId_PmcOutVolRmsL2 + 1
eSysId_DevInfoFWversionMajor = eSysId_PmcOutVolRmsL3 + 1
eSysId_DevInfoFWversionMinor = eSysId_DevInfoFWversionMajor + 1
eSysId_DevInfoFWversionDeviation = eSysId_DevInfoFWversionMinor + 1
eSysId_DevInfoFWversionBuild = eSysId_DevInfoFWversionDeviation + 1
eSysId_DevInfoFPGAversionMajor = eSysId_DevInfoFWversionBuild + 1
eSysId_DevInfoFPGAversionMinor = eSysId_DevInfoFPGAversionMajor + 1
eSysId_DevInfoFPGAversionDeviation = eSysId_DevInfoFPGAversionMinor + 1
eSysId_DevInfoFPGAversionBuild = eSysId_DevInfoFPGAversionDeviation + 1
eSysId_DevInfoHWrevision = eSysId_DevInfoFPGAversionBuild + 1
eSysId_DevInfoHWconfiguration = eSysId_DevInfoHWrevision + 1
eSysId_DevInfoHWidCode = eSysId_DevInfoHWconfiguration + 1
eSysId_DevInfoProductVersion = eSysId_DevInfoHWidCode + 1
eSysId_DevInfoModelNrPart1 = eSysId_DevInfoProductVersion + 1
eSysId_DevInfoModelNrPart2 = eSysId_DevInfoModelNrPart1 + 1
eSysId_DevInfoModelNrPart3 = eSysId_DevInfoModelNrPart2 + 1
eSysId_DevInfoModelNrPart4 = eSysId_DevInfoModelNrPart3 + 1
eSysId_DevInfoModelNrPart5 = eSysId_DevInfoModelNrPart4 + 1
eSysId_DevInfoModelNrPart6 = eSysId_DevInfoModelNrPart5 + 1
eSysId_DevInfoModelNrPart7 = eSysId_DevInfoModelNrPart6 + 1
eSysId_DevInfoModelNrPart8 = eSysId_DevInfoModelNrPart7 + 1
eSysId_DevInfoSerialNrPart1 = eSysId_DevInfoModelNrPart8 + 1
eSysId_DevInfoSerialNrPart2 = eSysId_DevInfoSerialNrPart1 + 1
eSysId_DevInfoSerialNrPart3 = eSysId_DevInfoSerialNrPart2 + 1
eSysId_DevInfoSerialNrPart4 = eSysId_DevInfoSerialNrPart3 + 1
eSysId_PmcDevInfoFWversionMajor = eSysId_DevInfoSerialNrPart4 + 1
eSysId_PmcDevInfoFWversionMinor = eSysId_PmcDevInfoFWversionMajor + 1
eSysId_PmcDevInfoFWversionDeviation = eSysId_PmcDevInfoFWversionMinor + 1
eSysId_PmcDevInfoFWversionBuild = eSysId_PmcDevInfoFWversionDeviation + 1
eSysId_PmcDevInfoFPGAversionMajor = eSysId_PmcDevInfoFWversionBuild + 1
eSysId_PmcDevInfoFPGAversionMinor = eSysId_PmcDevInfoFPGAversionMajor + 1
eSysId_PmcDevInfoFPGAversionDeviation = eSysId_PmcDevInfoFPGAversionMinor + 1
eSysId_PmcDevInfoFPGAversionBuild = eSysId_PmcDevInfoFPGAversionDeviation + 1
eSysId_PmcDevInfoHWrevision = eSysId_PmcDevInfoFPGAversionBuild + 1
eSysId_PmcDevInfoHWconfiguration = eSysId_PmcDevInfoHWrevision + 1
eSysId_PmcDevInfoHWidCode = eSysId_PmcDevInfoHWconfiguration + 1
eSysId_PmcDevInfoModelNrPart1 = eSysId_PmcDevInfoHWidCode + 1
eSysId_PmcDevInfoModelNrPart2 = eSysId_PmcDevInfoModelNrPart1 + 1
eSysId_PmcDevInfoModelNrPart3 = eSysId_PmcDevInfoModelNrPart2 + 1
eSysId_PmcDevInfoModelNrPart4 = eSysId_PmcDevInfoModelNrPart3 + 1
eSysId_PmcDevInfoModelNrPart5 = eSysId_PmcDevInfoModelNrPart4 + 1
eSysId_PmcDevInfoModelNrPart6 = eSysId_PmcDevInfoModelNrPart5 + 1
eSysId_PmcDevInfoModelNrPart7 = eSysId_PmcDevInfoModelNrPart6 + 1
eSysId_PmcDevInfoModelNrPart8 = eSysId_PmcDevInfoModelNrPart7 + 1
eSysId_PmcDevInfoSerialNrPart1 = eSysId_PmcDevInfoModelNrPart8 + 1
eSysId_PmcDevInfoSerialNrPart2 = eSysId_PmcDevInfoSerialNrPart1 + 1
eSysId_PmcDevInfoSerialNrPart3 = eSysId_PmcDevInfoSerialNrPart2 + 1
eSysId_PmcDevInfoSerialNrPart4 = eSysId_PmcDevInfoSerialNrPart3 + 1
eSysId_PmcDevInfoHeartbeat = eSysId_PmcDevInfoSerialNrPart4 + 1
eSysId_PmcDevInfoCbusVersion = eSysId_PmcDevInfoHeartbeat + 1
eSysId_PmcSurvHwStsReg = eSysId_PmcDevInfoCbusVersion + 1
eSysId_PmcSurvLocalStsReg1 = eSysId_PmcSurvHwStsReg + 1
eSysId_PmcSurvLocalStsReg2 = eSysId_PmcSurvLocalStsReg1 + 1
eSysId_PmcSurvSupplyStsReg = eSysId_PmcSurvLocalStsReg2 + 1
eSysId_PmcSurvTemperatureStsReg = eSysId_PmcSurvSupplyStsReg + 1
eSysId_PmcFaultHandlerStsReg = eSysId_PmcSurvTemperatureStsReg + 1
eSysId_PmcInletTempStatus = eSysId_PmcFaultHandlerStsReg + 1
eSysId_PmcOutletTempStatus = eSysId_PmcInletTempStatus + 1
eSysId_PmcHSTemp1Sns1Status = eSysId_PmcOutletTempStatus + 1
eSysId_PmcHSTemp1Sns2Status = eSysId_PmcHSTemp1Sns1Status + 1
eSysId_PmcHSTemp1Sns3Status = eSysId_PmcHSTemp1Sns2Status + 1
eSysId_PmcHSTemp1Sns4Status = eSysId_PmcHSTemp1Sns3Status + 1
eSysId_PmcHSTemp1Sns5Status = eSysId_PmcHSTemp1Sns4Status + 1
eSysId_PmcHSTemp1Sns6Status = eSysId_PmcHSTemp1Sns5Status + 1
eSysId_PmcHSTemp1Sns7Status = eSysId_PmcHSTemp1Sns6Status + 1
eSysId_PmcHSTemp1Sns8Status = eSysId_PmcHSTemp1Sns7Status + 1
eSysId_PmcHSTemp2Sns1Status = eSysId_PmcHSTemp1Sns8Status + 1
eSysId_PmcHSTemp2Sns2Status = eSysId_PmcHSTemp2Sns1Status + 1
eSysId_PmcHSTemp2Sns3Status = eSysId_PmcHSTemp2Sns2Status + 1
eSysId_PmcHSTemp2Sns4Status = eSysId_PmcHSTemp2Sns3Status + 1
eSysId_PmcHSTemp2Sns5Status = eSysId_PmcHSTemp2Sns4Status + 1
eSysId_PmcHSTemp2Sns6Status = eSysId_PmcHSTemp2Sns5Status + 1
eSysId_PmcHSTemp2Sns7Status = eSysId_PmcHSTemp2Sns6Status + 1
eSysId_PmcHSTemp2Sns8Status = eSysId_PmcHSTemp2Sns7Status + 1
eSysId_PmFaultHandlerPfcShutdownLocked = eSysId_PmcHSTemp2Sns8Status + 1
eSysId_PmFaultHandlerInvShutdownLocked = eSysId_PmFaultHandlerPfcShutdownLocked + 1
eSysId_PmFaultHandlerChgShutdownLocked = eSysId_PmFaultHandlerInvShutdownLocked + 1
eSysId_PmFaultHandlerPfcShutdown = eSysId_PmFaultHandlerChgShutdownLocked + 1
eSysId_PmFaultHandlerInvShutdown = eSysId_PmFaultHandlerPfcShutdown + 1
eSysId_PmFaultHandlerChgShutdown = eSysId_PmFaultHandlerInvShutdown + 1
eSysId_SurvUcHwStsReg = eSysId_PmFaultHandlerChgShutdown + 1
eSysId_SurvInputFuseL1NotOk = eSysId_SurvUcHwStsReg + 1
eSysId_SurvInputFuseL2NotOk = eSysId_SurvInputFuseL1NotOk + 1
eSysId_SurvInputFuseL3NotOk = eSysId_SurvInputFuseL2NotOk + 1
eSysId_SurvOutputFuseL1NotOk = eSysId_SurvInputFuseL3NotOk + 1
eSysId_SurvOutputFuseL2NotOk = eSysId_SurvOutputFuseL1NotOk + 1
eSysId_SurvOutputFuseL3NotOk = eSysId_SurvOutputFuseL2NotOk + 1
eSysId_SurvBatFusePosNotOk = eSysId_SurvOutputFuseL3NotOk + 1
eSysId_SurvBatFuseNegNotOk = eSysId_SurvBatFusePosNotOk + 1
eSysId_SurvAdc0Fault = eSysId_SurvBatFuseNegNotOk + 1
eSysId_SurvFpgaBcAct = eSysId_SurvAdc0Fault + 1
eSysId_SurvFpgaEPsuNotOk = eSysId_SurvFpgaBcAct + 1
eSysId_SurvFpgaEpoAct = eSysId_SurvFpgaEPsuNotOk + 1
eSysId_SurvA24vNotOk = eSysId_SurvFpgaEpoAct + 1
eSysId_SurvA5vNotOk = eSysId_SurvA24vNotOk + 1
eSysId_SurvA5vNegNotOk = eSysId_SurvA5vNotOk + 1
eSysId_SurvA15vNotOk = eSysId_SurvA5vNegNotOk + 1
eSysId_SurvA15vNegNotOk = eSysId_SurvA15vNotOk + 1
eSysId_SurvOnButtonAct = eSysId_SurvA15vNegNotOk + 1
eSysId_SurvOffButtonAct = eSysId_SurvOnButtonAct + 1
eSysId_SurvCbusPm1EnetLinkNotOk = eSysId_SurvOffButtonAct + 1
eSysId_SurvCbusPm2EnetLinkNotOk = eSysId_SurvCbusPm1EnetLinkNotOk + 1
eSysId_SurvCbusPm3EnetLinkNotOk = eSysId_SurvCbusPm2EnetLinkNotOk + 1
eSysId_SurvCbusPm4EnetLinkNotOk = eSysId_SurvCbusPm3EnetLinkNotOk + 1
eSysId_SurvCbusPm5EnetLinkNotOk = eSysId_SurvCbusPm4EnetLinkNotOk + 1
eSysId_SurvPm1Present = eSysId_SurvCbusPm5EnetLinkNotOk + 1
eSysId_SurvPm2Present = eSysId_SurvPm1Present + 1
eSysId_SurvPm3Present = eSysId_SurvPm2Present + 1
eSysId_SurvPm4Present = eSysId_SurvPm3Present + 1
eSysId_SurvPm5Present = eSysId_SurvPm4Present + 1
eSysId_SurvUcEnabled = eSysId_SurvPm5Present + 1
eSysId_SurvSbsPresent = eSysId_SurvUcEnabled + 1
eSysId_SurvUcHwStsReg1 = eSysId_SurvSbsPresent + 1
eSysId_SurvUcAmbTemperatureFault = eSysId_SurvUcHwStsReg1 + 1
eSysId_SurvUcAmbTemperatureHigh = eSysId_SurvUcAmbTemperatureFault + 1
eSysId_SurvUcOutVolSnsFaultL1 = eSysId_SurvUcAmbTemperatureHigh + 1
eSysId_SurvUcOutVolSnsFaultL2 = eSysId_SurvUcOutVolSnsFaultL1 + 1
eSysId_SurvUcOutVolSnsFaultL3 = eSysId_SurvUcOutVolSnsFaultL2 + 1
eSysId_UcOperableStatus = eSysId_SurvUcOutVolSnsFaultL3 + 1
eSysId_FaultHandlerUcAnyFault = eSysId_UcOperableStatus + 1
eSysId_FaultHandlerUcShutdown = eSysId_FaultHandlerUcAnyFault + 1
eSysId_FaultHandlerUcShutdownLocked = eSysId_FaultHandlerUcShutdown + 1
eSysId_SurvDigIoOverrideEnOutputs = eSysId_FaultHandlerUcShutdownLocked + 1
eSysId_SurvDigIoOverrideValOutputs = eSysId_SurvDigIoOverrideEnOutputs + 1
eSysId_SurvDigIoOverrideEnInputs = eSysId_SurvDigIoOverrideValOutputs + 1
eSysId_SurvDigIoOverrideValInputs = eSysId_SurvDigIoOverrideEnInputs + 1
eSysId_SbscDevInfoFWversionMajor = eSysId_SurvDigIoOverrideValInputs + 1
eSysId_SbscDevInfoFWversionMinor = eSysId_SbscDevInfoFWversionMajor + 1
eSysId_SbscDevInfoFWversionDeviation = eSysId_SbscDevInfoFWversionMinor + 1
eSysId_SbscDevInfoFWversionBuild = eSysId_SbscDevInfoFWversionDeviation + 1
eSysId_SbscDevInfoHWrevision = eSysId_SbscDevInfoFWversionBuild + 1
eSysId_SbscDevInfoHWconfiguration = eSysId_SbscDevInfoHWrevision + 1
eSysId_SbscDevInfoHWidCode = eSysId_SbscDevInfoHWconfiguration + 1
eSysId_SbscDevInfoModelNrPart1 = eSysId_SbscDevInfoHWidCode + 1
eSysId_SbscDevInfoModelNrPart2 = eSysId_SbscDevInfoModelNrPart1 + 1
eSysId_SbscDevInfoModelNrPart3 = eSysId_SbscDevInfoModelNrPart2 + 1
eSysId_SbscDevInfoModelNrPart4 = eSysId_SbscDevInfoModelNrPart3 + 1
eSysId_SbscDevInfoModelNrPart5 = eSysId_SbscDevInfoModelNrPart4 + 1
eSysId_SbscDevInfoModelNrPart6 = eSysId_SbscDevInfoModelNrPart5 + 1
eSysId_SbscDevInfoModelNrPart7 = eSysId_SbscDevInfoModelNrPart6 + 1
eSysId_SbscDevInfoModelNrPart8 = eSysId_SbscDevInfoModelNrPart7 + 1
eSysId_SbscDevInfoSerialNrPart1 = eSysId_SbscDevInfoModelNrPart8 + 1
eSysId_SbscDevInfoSerialNrPart2 = eSysId_SbscDevInfoSerialNrPart1 + 1
eSysId_SbscDevInfoSerialNrPart3 = eSysId_SbscDevInfoSerialNrPart2 + 1
eSysId_SbscDevInfoSerialNrPart4 = eSysId_SbscDevInfoSerialNrPart3 + 1
eSysId_SbcFwVerBootImageMajor = eSysId_SbscDevInfoSerialNrPart4 + 1
eSysId_SbcFwVerBootImageMinor = eSysId_SbcFwVerBootImageMajor + 1
eSysId_SbcFwVerBootImageDeviation = eSysId_SbcFwVerBootImageMinor + 1
eSysId_SbcFwVerBootImageBuild = eSysId_SbcFwVerBootImageDeviation + 1
eSysId_SbsCtrlTransition = eSysId_SbcFwVerBootImageBuild + 1
eSysId_SbcCmd = eSysId_SbsCtrlTransition + 1
eSysId_SbsEconversionMode = eSysId_SbcCmd + 1
eSysId_SbcSerialNumber = eSysId_SbsEconversionMode + 1
eSysId_SbcModelNumber = eSysId_SbcSerialNumber + 1
eSysId_SbsCommunication = eSysId_SbcModelNumber + 1
eSysId_SbcState = eSysId_SbsCommunication + 1
eSysId_SbcFrameSize = eSysId_SbcState + 1
eSysId_SbsStateInfo = eSysId_SbcFrameSize + 1
eSysId_EcoModeSbcReqHandler = eSysId_SbsStateInfo + 1
eSysId_SbsTempError = eSysId_EcoModeSbcReqHandler + 1
eSysId_SbsFanError = eSysId_SbsTempError + 1
eSysId_SbsHeartbeat = eSysId_SbsFanError + 1
eSysId_SbsHeartbeatError = eSysId_SbsHeartbeat + 1
eSysId_SbsBackFeedError = eSysId_SbsHeartbeatError + 1
eSysId_SbsInputFreqStatus = eSysId_SbsBackFeedError + 1
eSysId_SbsErrorStatus = eSysId_SbsInputFreqStatus + 1
eSysId_SbsSelfTestError = eSysId_SbsErrorStatus + 1
eSysId_SbsSelfTestStatus = eSysId_SbsSelfTestError + 1
eSysId_SbsOutputVoltageState = eSysId_SbsSelfTestStatus + 1
eSysId_SbsScrFault = eSysId_SbsOutputVoltageState + 1
eSysId_SbsOutputFreqStatus = eSysId_SbsScrFault + 1
eSysId_SbsDcErrorOnOutput = eSysId_SbsOutputFreqStatus + 1
eSysId_SbsInputVoltageStatus = eSysId_SbsDcErrorOnOutput + 1
eSysId_SbcFirmwareVersionIncompatible = eSysId_SbsInputVoltageStatus + 1
eSysId_SbcHardwareVersionIncompatible = eSysId_SbcFirmwareVersionIncompatible + 1
eSysId_SbsPsuError = eSysId_SbcHardwareVersionIncompatible + 1
eSysId_SbcFwVersion = eSysId_SbsPsuError + 1
eSysId_Bf2TripActive = eSysId_SbcFwVersion + 1
eSysId_SbcDevMgrState = eSysId_Bf2TripActive + 1
eSysId_SbsBfContactorActive = eSysId_SbcDevMgrState + 1
eSysId_UepProtocolVersion = eSysId_SbsBfContactorActive + 1
eSysId_SbsModuleDisabled = eSysId_UepProtocolVersion + 1
eSysId_SbsConnectionStatus = eSysId_SbsModuleDisabled + 1
eSysId_SbcInputJumperMissing = eSysId_SbsConnectionStatus + 1
eSysId_FwuSparepartUpdate = eSysId_SbcInputJumperMissing + 1
eSysId_ParallelUpsIdSetting = eSysId_FwuSparepartUpdate + 1
eSysId_NumberOfParallelUpsSetting = eSysId_ParallelUpsIdSetting + 1
eSysId_TransToSbsDisableSetting = eSysId_NumberOfParallelUpsSetting + 1
eSysId_TransToSbsVolOutOfToleranceSetting = eSysId_TransToSbsDisableSetting + 1
eSysId_EcoModeSbcReq = eSysId_TransToSbsVolOutOfToleranceSetting + 1
eSysId_ExtForceExtSyncInAct = eSysId_EcoModeSbcReq + 1
eSysId_ExternalSyncModeSetting = eSysId_ExtForceExtSyncInAct + 1
eSysId_ForceExternalSyncSetting = eSysId_ExternalSyncModeSetting + 1
eSysId_Mains2TransitionTimePeriodSetting = eSysId_ForceExternalSyncSetting + 1
eSysId_EnableStaticBypStdbyInDualSyncSetting = eSysId_Mains2TransitionTimePeriodSetting + 1
eSysId_PmChargePowerReduced = eSysId_EnableStaticBypStdbyInDualSyncSetting + 1
eSysId_PmcChgOneCharging = eSysId_PmChargePowerReduced + 1
eSysId_NumberOfPowerModuleAvailable = eSysId_PmcChgOneCharging + 1
eSysId_PmChargePowerReducedActiveBF = eSysId_NumberOfPowerModuleAvailable + 1
eSysId_PmcFirmwareVersionIncompatible = eSysId_PmChargePowerReducedActiveBF + 1
eSysId_UpsTotalAvailablePower = eSysId_PmcFirmwareVersionIncompatible + 1
eSysId_UpsTotalDeratedAvailablePower = eSysId_UpsTotalAvailablePower + 1
eSysId_ConfigManagerErrorCode = eSysId_UpsTotalDeratedAvailablePower + 1
eSysId_ConfigManagerWarningCode = eSysId_ConfigManagerErrorCode + 1
eSysId_ConfigManagerExecuteState = eSysId_ConfigManagerWarningCode + 1
eSysId_ConfigManagerExpectedPmPresentBF = eSysId_ConfigManagerExecuteState + 1
eSysId_ConfigManagerUpsInstallationSizeKW = eSysId_ConfigManagerExpectedPmPresentBF + 1
eSysId_ConfigManagerUpsSystemConfiguredBatteryNominalVoltage = eSysId_ConfigManagerUpsInstallationSizeKW + 1
eSysId_ConfigManagerUpsSystemTotalBatteryAhInstalled = eSysId_ConfigManagerUpsSystemConfiguredBatteryNominalVoltage + 1
eSysId_ConfigManagerUpsSystemDeratingFactor = eSysId_ConfigManagerUpsSystemTotalBatteryAhInstalled + 1
eSysId_ConfigManagerOperatingAltitudeAboveSeaLevel = eSysId_ConfigManagerUpsSystemDeratingFactor + 1
eSysId_ConfigManagerPmRedundancyConfiguration = eSysId_ConfigManagerOperatingAltitudeAboveSeaLevel + 1
eSysId_ConfigManagerDetectedPmSizeKW = eSysId_ConfigManagerPmRedundancyConfiguration + 1
eSysId_ConfigManagerDetectedPmType = eSysId_ConfigManagerDetectedPmSizeKW + 1
eSysId_ConfigManagerDetectedSbsSizeKW = eSysId_ConfigManagerDetectedPmType + 1
eSysId_ConfigManagerDetectedSbsType = eSysId_ConfigManagerDetectedSbsSizeKW + 1
eSysId_ConfigManagerRFIDupsFrameSizeKW = eSysId_ConfigManagerDetectedSbsType + 1
eSysId_ConfigManagerRFIDupsFrameType = eSysId_ConfigManagerRFIDupsFrameSizeKW + 1
eSysId_ConfigManagerRFIDupsPmType = eSysId_ConfigManagerRFIDupsFrameType + 1
eSysId_ConfigManagerRFIDupsSbsType = eSysId_ConfigManagerRFIDupsPmType + 1
eSysId_CommunicationStatus = eSysId_ConfigManagerRFIDupsSbsType + 1
eSysId_VoltageACRange = eSysId_CommunicationStatus + 1
eSysId_CbusProtocolConnectionState = eSysId_VoltageACRange + 1
eSysId_CbusDataIntegrityStatus = eSysId_CbusProtocolConnectionState + 1
eSysId_MQTTEventLogPerformanceData = eSysId_CbusDataIntegrityStatus + 1
eSysId_MQTTstartEventLogTestCommand = eSysId_MQTTEventLogPerformanceData + 1
eSysId_MQTTstopEventLogTestCommand = eSysId_MQTTstartEventLogTestCommand + 1
eSysId_MQTTEventLogTestRateX100 = eSysId_MQTTstopEventLogTestCommand + 1
eSysId_MQTTperformanceData = eSysId_MQTTEventLogTestRateX100 + 1
eSysId_MQTTstartPerfTestCommand = eSysId_MQTTperformanceData + 1
eSysId_MQTTstopPerfTestCommand = eSysId_MQTTstartPerfTestCommand + 1
eSysId_MQTTPerfTestRateX100 = eSysId_MQTTstopPerfTestCommand + 1
eSysId_LcmPmcElapsedTimeFanSetting = eSysId_MQTTPerfTestRateX100 + 1
eSysId_LcmPmcElapsedTimeData = eSysId_LcmPmcElapsedTimeFanSetting + 1
eSysId_LcmPmcRestartFanCommand = eSysId_LcmPmcElapsedTimeData + 1
eSysId_LcmPmcRequestElapsedTimeCommand = eSysId_LcmPmcRestartFanCommand + 1
eSysId_LcmSbsElapsedTimeFanSetting = eSysId_LcmPmcRequestElapsedTimeCommand + 1
eSysId_LcmSbsElapsedTimeData = eSysId_LcmSbsElapsedTimeFanSetting + 1
eSysId_LcmSbsRestartFanCommand = eSysId_LcmSbsElapsedTimeData + 1
eSysId_LcmSbsRequestElapsedTimeCommand = eSysId_LcmSbsRestartFanCommand + 1
eSysId_LcmTestAccelerateTestActive = eSysId_LcmSbsRequestElapsedTimeCommand + 1
eSysId_LcmStartAcceleratedTestCommand = eSysId_LcmTestAccelerateTestActive + 1
eSysId_LcmStopAcceleratedTestCommand = eSysId_LcmStartAcceleratedTestCommand + 1
eSysId_BaseModelNumber = eSysId_LcmStopAcceleratedTestCommand + 1
eSysId_ConfigManagerBaseModelWarning = eSysId_BaseModelNumber + 1
eSysId_ConfigPowerModuleOk = eSysId_ConfigManagerBaseModelWarning + 1
eSysId_ConfigPMTypeOKFromUC = eSysId_ConfigPowerModuleOk + 1
eSysId_WdiLatchStatus = eSysId_ConfigPMTypeOKFromUC + 1
eSysId_NmcNtpEnabled = eSysId_WdiLatchStatus + 1
eSysId_ParNmcNtpEnabled = eSysId_NmcNtpEnabled + 1
eSysId_TransformerVolCompSetting = eSysId_ParNmcNtpEnabled + 1
eSysId_TransformerPresentSetting = eSysId_TransformerVolCompSetting + 1
eSysId_MQTTHighEffScheduleWriterFLag = eSysId_TransformerPresentSetting + 1
eSysElementMax = eSysId_MQTTHighEffScheduleWriterFLag + 1

# ######################################################################################################################
# DATA TYPE DEFINE
# 4 bit
# ======================================================================================================================
SYS_INFO_DATA_INVALID = 0x0
SYS_INFO_DATA_BOOL = 0x1
SYS_INFO_DATA_INT8 = 0x2
SYS_INFO_DATA_INT16 = 0x3
SYS_INFO_DATA_INT32 = 0x4
SYS_INFO_DATA_F32 = 0x5

# ######################################################################################################################
# DATA MAP DEFINE
# id: (data_type, array_length)
# ======================================================================================================================
sys_info_data_map = dict(
    (
        (eSysId_DemoElement, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_OutPhPhVolSetting, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_OutFreqSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_OutFreqToleranceSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_OutVolCompSetting, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_ChgRegVolRef, (SYS_INFO_DATA_F32, 1)),
        (eSysId_ChgRegCurLim, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SlcChgEn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MinChgVolRef, (SYS_INFO_DATA_F32, 1)),
        (eSysId_MinChgCurLim, (SYS_INFO_DATA_F32, 1)),
        (eSysId_BattTestActive, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MainsCurrentRampInTime, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_OutFreqSyncSpeed, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_3PhIn1PhOut, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BattMidPointPressentSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_NeutralPresentSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_OutVolToleranceSetting, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_SlcSettingsConfirmed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_PmSelftestStartAllowed, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_NpiTestModeEnabled, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BattVolHighWarnLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_BattVolHighShutdownLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_BattVolLowWarnLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_BattVolLowShutdownLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_BattVolCollapseLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_BattVolCollapseClearLvl, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_EconvHarmCompEnableSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BbTripStatus, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BatteryRelayCloseAllowed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_PmcInvRlyOpenCmd, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_EnergyStorageAutoDisconnectStatus, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SelftestState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_PmcSelftestState, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHsTemp1Min, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcHsTemp1Mean, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcHsTemp1Max, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcHsTemp2Min, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcHsTemp2Mean, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcHsTemp2Max, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcAirInletTemp, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcAirOutletTemp, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcFanSpeed, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcFanStates, (SYS_INFO_DATA_INT8, 3)),
        (eSysId_PmcMainsRlyEn, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcChgRlyEn, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcInvRlyEn, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_BypChgActive, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_InvSysCtrlOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvSysCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvConvEn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_DcGainEn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_EconvHarmCompEnable, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlActivateStaticBypassSwitchNoBreak, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlActivateStaticBypassSwitchWithBreak, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlBattTestStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlBatteryConnected, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlBurnInStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlCbusMcComStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlChgSysCtrlOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlConfirmRedundancyLost, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlConfirmTurnLoadOff, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlDeactivateStaticBypassSwitch, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlDisChargeBurnInTestMode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlEndOfDischargeTimeoutReached, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlEnergyStorage, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlFrequencyConverterModeSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlInverterOffDueToOffButton, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_UpsSysCtrlLi_IonBattTempEstimatorStatus, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlUpsOpMode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlUpsOpModeCorrected, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlOutputContactorOpenRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlPfcOpModeAllBattOp, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlPfcOpModeAllNormOp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlPfcOpModeNumberInBattOp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlPfcOpModeOneBattOp, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlPfcOpModeOneNormOp, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlPfcOpModeOneNormOpOrRampIn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlPfcOpModeOneOffOp, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlPfcRegWindUp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlPowerCabinetPresentSetting, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlPowerCabinetRedundancySetting, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlPowerSectionAvailableBF, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlSbsOpModeCmd, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlSmoothTransferToBypassEn, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlSystemAutoRestarted, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsModeUserReq, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOffButtonAccepted, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOffButtonAct, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOnButtonAccepted, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOnButtonAct, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeCmd, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsSysCtrlUpsOpModeForcedStaticBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeInverterSPoT, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeInverterStandby, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeMaintenanceBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeNormalOp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassInvShutdown, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOutVqdErr, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassOverload, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqForcedStaticBypassShortRegByp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerBypassBurnInTest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerDischargeBurnInTest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerForcedStaticBypassDueToOffBt, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerOnButtonPressed, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromOff, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerOnFromReqBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerRequestedBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserOffConfirm, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeReqHandlerWaitForUserRedundancy, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeRequestedStaticBypassFromOff, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpModeStaticBypassStandby, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOpsModeBatteryOp, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsOverLoad, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSysCtrlUpsPowerRating, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsShutdownDueToLowBattery, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsSysCtrlUpsSysCtrlAutostartActivated, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EconvMode, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ReturnFromMaintenanceBypassSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ReturnFromMaintenanceBypassForcedLockStatus, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ReturnFromMaintenanceBypassClearForcedLock, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_NotEnoughUpsReadyToTurnOn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParSysCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParSysCtrlReducedOverloadStepIndex, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysInhibitTransferFromBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParSysCtrlSystemLocked, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_RelayControlExtUseStaticBypassStandbyAct, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InhibitTransferFromBypass, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParUpsDevMgrOpMode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_SysOpModeParMaster, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParMains1SyncSourceErrorStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParExtSyncSourceErrorStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParIntBypassSyncSourceErrorStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParSibClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParSsibClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParUibClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParallelUnitPresent, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParSysMains1CurRmsL1, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysMains1CurRmsL2, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysMains1CurRmsL3, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysMains2CurRmsL1, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysMains2CurRmsL2, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysMains2CurRmsL3, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutCurRmsL1, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutCurRmsL2, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutCurRmsL3, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutApparentPwr, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutApparentPwrL1, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutApparentPwrL2, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysOutApparentPwrL3, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysActivePwrL1, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysActivePwrL2, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParSysActivePwrL3, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_TimeReceived, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParAddressError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_parallelUnitCompatibility, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_parallelSynchronizationStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_OutActivePower, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_MQTTEcoModeScheduling, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeStartDay, (SYS_INFO_DATA_INT8, 7)),
        (eSysId_EcoModeStartTime, (SYS_INFO_DATA_INT32, 7)),
        (eSysId_EcoModeStopDay, (SYS_INFO_DATA_INT8, 7)),
        (eSysId_EcoModeStopTime, (SYS_INFO_DATA_INT32, 7)),
        (eSysId_EcoModeProgramEnable, (SYS_INFO_DATA_BOOL, 7)),
        (eSysId_ParUpsMgrOpMode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParUpsMgrParMixedMode, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParUpsMgrParSysTurnOffUpsOk, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParUpsMgrTrans, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParUpsMgrParallelRedundancyLost, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MinUpsToSupplyLoadPresent, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrMbbClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrUobClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrSibClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrSsibClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrImbClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrRimbClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BreakerMgrUibClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SysReqHandlerSysMaintenanceRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerSysForcedStaticBypassduetoVQDErrorRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerForcedStaticBypassRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerForcedStaticBypassDueToOverloadRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerForcedStaticBypassDueToOffButtonRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerRequestedStaticBypassRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerInverterOnRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerInverterOffRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerBypassBurnInTestRequest, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysReqHandlerSysOpModeReq, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParMastrSelctParMastermode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParMastrSelctMasterCollissionError, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParMastrSelctNoMasterPresent, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParMastrSelctMasterId, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_InverterStandbyActive, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParSmartBatOpCtrlOpMode, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_MQTTInverterOffCommand, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTInverterOnCommand, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTInverterToStaticBypassCommand, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTStaticBypassToInverterCommand, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTConfirmTurnInverterOffCommand, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTSwitchgearSettingUIB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingSSIB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingUOB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingMBB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingSIB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingIMB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearSettingRIMB, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusMBBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusUOBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusSIBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusSSIBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusIMBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusRIMBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTSwitchgearStatusUIBClosed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_CommonInputBreakerPresentSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsSystemFWversionMajor, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_UpsSystemFWversionMinor, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_UpsSystemFWversionDeviation, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_UpsSystemFWversionBuild, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_UpsSerialNumber, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_UpsSerialNumberUps1, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_UpsSerialNumberUps2, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_UpsSerialNumberUps3, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_UpsSerialNumberUps4, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_UpsSerialNumberUps5, (SYS_INFO_DATA_INT32, 8)),
        (eSysId_NmcNtpEnabled, (SYS_INFO_DATA_BOOL, 2)),
        (eSysId_ParNmcNtpEnabled, (SYS_INFO_DATA_BOOL, 5)),
        (eSysId_SysBypassCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysBypassCtrlSbsReadyToTurnOn, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_EcoModeReqBypassAct, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeAllowedStatus, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_EcoModeHandlerOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeHandlerState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeBasicAllowed, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTHighEfficiencyModeSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTHighEfficiencyModeEnabled, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeHandlerUpsInEcoMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysOpModeCorrected, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParUpsReadyToTurnOn, (SYS_INFO_DATA_BOOL, 5)),
        (eSysId_SysBypassOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysBypassOpModeCmd, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_StaticBypassWithBreakRequired, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParUobClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParMbbClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParImbClosed, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParInhibitTransferFromBypass, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParRedundancy, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_ParUpsOutputOverload, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParUpsPowerRatings, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_UpsOpModeReq, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_ParUpsReadyForNormalOp, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_AdvBattOpMgrDisabledAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_FactoryTestModeEn, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_AlarmCriticalAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_AlarmWarningAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_AlarmInfoAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_Pbus1CanComOk, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_Pbus2CanComOk, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_AlarmParCriticalStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_AlarmParInfo, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParMixedUpsSizeError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParBreakerPresent, (SYS_INFO_DATA_INT16, 5)),
        (eSysId_ParBbClosed, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_AlarmParInfoStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_TimeSet, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_OutTotalApparentPower, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_AlarmParWarningStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ParallelUpsIdSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_MinUpsToSupplyLoadSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_TransToStaticBypOnEpoSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParOperationRedundancyModeSetting, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_UpsAutoStartEnSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MainsDualFeedPresentSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_EconvHamCompEnable, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_CommonBatterySetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsIsPreferredExtSyncSourceSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_FrequencyConverterModeSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UpsIsFixedExtSyncMasterSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ParUpsIsFixedExtSyncMaster, (SYS_INFO_DATA_BOOL, 5)),
        (eSysId_UpsMinFwMajor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_Pbus1Rs485Error, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_Pbus2Rs485Error, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysIdSyncSourceSysCtrlOpMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysIdSyncSourceSysCtrlBypassError, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlMains1Error, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlExtSyncInvPllLockFailed, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlExtSyncSourceError, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlExtSyncSourceErrorCustom, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlForceExtSyncOut, (SYS_INFO_DATA_BOOL, 1)),
        (eSysIdSyncSourceSysCtrlExtSyncReqOut, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_InvA1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvA2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvB0, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvB1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvB2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvK1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DisableClassBoost, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_InvPllSyncError, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_InvPllSynchronizationStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_InvPllInvPllLocked, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_OutVolComp, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_InvCurLimAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_InvLoadAboveLim, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_EnInvLimit, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ChgInCurLim, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SelChgVolLog, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SelChgCurLog, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsChgOn, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_VqdRmsSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdRmsPhaseSts, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_VqdMissingPhSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdPhRotSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdPllSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdBattSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdDcOnOutSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdFreqSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdNeuDispSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdWaveformSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_VqdWaveformPhaseSts, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_PmcVqdRmsSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdRmsPhaseSts, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcVqdMissingPhSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdNeuDispSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdDcBusSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdPhRotSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdPllSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdBattSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdDcOnOutSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdFreqSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdWaveformSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcVqdWaveformPhaseSts, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdMains1VolRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdMains1VolPhPhRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdMains2VolRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdMains2VolPhPhRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdOutVolPhPhRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdOutVolRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdOutVolAvg, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdOutVolPhPhAvg, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdExtSyncVolRms, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_VqdNeuChgVolAvg, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_InputFuseSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_OutputFuseSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysDataMains1VolRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains1VolPhPhRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2VolRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2VolPhPhRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutVolRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutVolPhPhRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataBattVol, (SYS_INFO_DATA_F32, 2)),
        (eSysId_SysDataBattVolTotal, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataBattCur, (SYS_INFO_DATA_F32, 2)),
        (eSysId_SysDataBattCurMax, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains1CurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2CurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutCurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains1Freq, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains2Freq, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOutFreq, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains1PwrFactor, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2PwrFactor, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutPwrFactor, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains1RealPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2RealPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutRealPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataBattRealPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataBattRealPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains1RealPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains2RealPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOutRealPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains1AppPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2AppPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutAppPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains1AppPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains2AppPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOutAppPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOutAppPwrPct, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataInEnergy, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOutEnergy, (SYS_INFO_DATA_F32, 1)),
        (eSysId_TotalLoadRate, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_SysDataOutLoadRate, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutLoadRateMax, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataMains1LoadRate, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2LoadRate, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataPmcInvLoadRate, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutCrestFactor, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutPeakCur, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains1PeakCur, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataMains2PeakCur, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutCurThd, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataOutNeuCurRms, (SYS_INFO_DATA_F32, 1)),
        (eSysId_OutLoadAboveCustomerLim, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_OutLoadCustomerLim, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_SysDataParSysTotalMains1CurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataParSysTotalMains2CurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataParSysTotalOutCurRms, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataParSysTotalOutAppPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataParSysTotalOutAppPwrPhSum, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataParSysTotalOutRealPwrSum, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataParSysTotalOutRealPwr, (SYS_INFO_DATA_F32, 3)),
        (eSysId_SysDataParTotalOutLoad, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataAmbientTemp, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysDataOverloadDueToHighAmbTemp, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_PfcSysCtrlOpMode, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PfcSysCtrlTransition, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcInvSysCtrlTransition, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PfcInitRampInDone, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_RampInTimeChanged, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PfcMainsRampInDone, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcChgStatus, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcInvSysCtrlOpMode, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PfcCurrentReduced, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcChgOneCharging, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_NumberOfPowerModuleAvailable, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_PmChargePowerReduced, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmChargePowerReducedActiveBF, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_PmcFirmwareVersionIncompatible, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmcInvSysCtrlInvOperable, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_UcMains1VolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcMains1VolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcMains1VolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcMains1VolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcMains2VolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcMains2VolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcMains2VolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcMains2VolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcOutVolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcOutVolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcOutVolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcOutVolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcExtSyncVolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcExtSyncVolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcExtSyncVolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcExtSyncVolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcBattVolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcBattVolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcBattVolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcBattVolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcNeuChgVolSnsScaleVtoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcNeuChgVolSnsScaleQtoV, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcNeuChgVolSnsScaleVtoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcNeuChgVolSnsScaleQtoVmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcOutCurSnsScaleItoQ, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcOutCurSnsScaleQtoI, (SYS_INFO_DATA_F32, 1)),
        (eSysId_UcOutCurSnsScaleItoQmul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UcOutCurSnsScaleQtoImul2Pow16, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SysPowerFactor, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysCrestFactor, (SYS_INFO_DATA_F32, 1)),
        (eSysId_SysAppPwrRating, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_UcMaxChgVolLevel, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_UcMinChgVolLevel, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_AlphaRfiFilterMains1, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_AlphaRfiFilterInv, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_AlphaRfiFilterMains2, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_PmcInvCurSnsL1, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcInvCurSnsL2, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcInvCurSnsL3, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcInvCurRmsL1, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcInvCurRmsL2, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcInvCurRmsL3, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1CurRmsL1, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1CurRmsL2, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1CurRmsL3, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PwrFactL1, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PwrFactL2, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PwrFactL3, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1RealPwrL1, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1RealPwrL2, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1RealPwrL3, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PeakCurL1, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PeakCurL2, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcMains1PeakCurL3, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcBattCurPos, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcBattCurNeg, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcOutVolRmsL1, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcOutVolRmsL2, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcOutVolRmsL3, (SYS_INFO_DATA_INT16, 3)),
        (eSysId_PmcInvCurSnsScaleItoQ, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcInvCurSnsScaleQtoI, (SYS_INFO_DATA_F32, 3)),
        (eSysId_PmcInvCurSnsScaleItoQmul2Pow16, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcInvCurSnsScaleQtoImul2Pow16, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_DevInfoFWversionMajor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFWversionMinor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFWversionDeviation, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFWversionBuild, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFPGAversionMajor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFPGAversionMinor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFPGAversionDeviation, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoFPGAversionBuild, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoHWrevision, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoHWconfiguration, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoHWidCode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoProductVersion, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart3, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart4, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart5, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart6, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart7, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoModelNrPart8, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoSerialNrPart1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoSerialNrPart2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoSerialNrPart3, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_DevInfoSerialNrPart4, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_PmcDevInfoFWversionMajor, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFWversionMinor, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFWversionDeviation, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFWversionBuild, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFPGAversionMajor, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFPGAversionMinor, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFPGAversionDeviation, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoFPGAversionBuild, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoHWrevision, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoHWconfiguration, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoHWidCode, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart1, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart2, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart3, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart4, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart5, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart6, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart7, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoModelNrPart8, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoSerialNrPart1, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoSerialNrPart2, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoSerialNrPart3, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoSerialNrPart4, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoHeartbeat, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcDevInfoCbusVersion, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcSurvHwStsReg, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcSurvLocalStsReg1, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcSurvLocalStsReg2, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcSurvSupplyStsReg, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcSurvTemperatureStsReg, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcFaultHandlerStsReg, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcInletTempStatus, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcOutletTempStatus, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns1Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns2Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns3Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns4Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns5Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns6Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns7Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp1Sns8Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns1Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns2Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns3Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns4Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns5Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns6Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns7Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmcHSTemp2Sns8Status, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_PmFaultHandlerPfcShutdownLocked, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmFaultHandlerInvShutdownLocked, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmFaultHandlerChgShutdownLocked, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmFaultHandlerPfcShutdown, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmFaultHandlerInvShutdown, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_PmFaultHandlerChgShutdown, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_SurvUcHwStsReg, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SurvInputFuseL1NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvInputFuseL2NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvInputFuseL3NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvOutputFuseL1NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvOutputFuseL2NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvOutputFuseL3NotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvBatFusePosNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvBatFuseNegNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvAdc0Fault, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvFpgaBcAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvFpgaEPsuNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvFpgaEpoAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvA24vNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvA5vNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvA5vNegNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvA15vNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvA15vNegNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvOnButtonAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvOffButtonAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvCbusPm1EnetLinkNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvCbusPm2EnetLinkNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvCbusPm3EnetLinkNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvCbusPm4EnetLinkNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvCbusPm5EnetLinkNotOk, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvPm1Present, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvPm2Present, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvPm3Present, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvPm4Present, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvPm5Present, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvUcEnabled, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvSbsPresent, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvUcHwStsReg1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SurvUcAmbTemperatureFault, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SurvUcAmbTemperatureHigh, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SurvUcOutVolSnsFaultL1, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvUcOutVolSnsFaultL2, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvUcOutVolSnsFaultL3, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_UcOperableStatus, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_FaultHandlerUcAnyFault, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_FaultHandlerUcShutdown, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_FaultHandlerUcShutdownLocked, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SurvDigIoOverrideEnOutputs, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_SurvDigIoOverrideValOutputs, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_SurvDigIoOverrideEnInputs, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SurvDigIoOverrideValInputs, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoFWversionMajor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoFWversionMinor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoFWversionDeviation, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoFWversionBuild, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoHWrevision, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoHWconfiguration, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoHWidCode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart3, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart4, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart5, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart6, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart7, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoModelNrPart8, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoSerialNrPart1, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoSerialNrPart2, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoSerialNrPart3, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDevInfoSerialNrPart4, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFwVerBootImageMajor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFwVerBootImageMinor, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFwVerBootImageDeviation, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFwVerBootImageBuild, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsOpMode, (SYS_INFO_DATA_INT32, 5)),
        (eSysId_SbsCtrlTransition, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcCmd, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsEconversionMode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcSerialNumber, (SYS_INFO_DATA_INT32, 16)),
        (eSysId_SbcModelNumber, (SYS_INFO_DATA_INT32, 16)),
        (eSysId_SbsCommunication, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFrameSize, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsStateInfo, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_EcoModeSbcReqHandler, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsTempError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsFanError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsHeartbeat, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsHeartbeatError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsBackFeedError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsInputFreqStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsErrorStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsSelfTestError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsSelfTestStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsOutputVoltageState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsScrFault, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsOutputFreqStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsDcErrorOnOutput, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsInputVoltageStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFirmwareVersionIncompatible, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcHardwareVersionIncompatible, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SbsPsuError, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcFwVersion, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_Bf2TripActive, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbcDevMgrState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsBfContactorActive, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UepProtocolVersion, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbsModuleDisabled, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_SbsConnectionStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_SbscDeviceVerification, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_CommunicationStatus, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_VoltageACRange, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_FwuSparepartUpdate, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_NumberOfParallelUpsSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_TransToSbsDisableSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_TransToSbsVolOutOfToleranceSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_EcoModeSbcReq, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ExtForceExtSyncInAct, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ExternalSyncModeSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ForceExternalSyncSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_Mains2TransitionTimePeriodSetting, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_EnableStaticBypStdbyInDualSyncSetting, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_ConfigManagerErrorCode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerWarningCode, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerExecuteState, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerExpectedPmPresentBF, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerUpsInstallationSizeKW, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerUpsSystemConfiguredBatteryNominalVoltage, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerUpsSystemTotalBatteryAhInstalled, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerUpsSystemDeratingFactor, (SYS_INFO_DATA_F32, 1)),
        (eSysId_ConfigManagerOperatingAltitudeAboveSeaLevel, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerPmRedundancyConfiguration, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerDetectedPmSizeKW, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_ConfigManagerDetectedPmType, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_ConfigManagerDetectedSbsSizeKW, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerDetectedSbsType, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerRFIDupsFrameSizeKW, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerRFIDupsFrameType, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerRFIDupsPmType, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerRFIDupsSbsType, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsTotalAvailablePower, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_UpsTotalDeratedAvailablePower, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_CbusProtocolConnectionState, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_CbusDataIntegrityStatus, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_MQTTEventLogPerformanceData, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTstartEventLogTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTstopEventLogTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTEventLogTestRateX100, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTperformanceData, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_MQTTstartPerfTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTstopPerfTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_MQTTPerfTestRateX100, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_LcmPmcElapsedTimeFanSetting, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_LcmPmcElapsedTimeData, (SYS_INFO_DATA_INT32, 3)),
        (eSysId_LcmPmcRestartFanCommand, (SYS_INFO_DATA_BOOL, 3)),
        (eSysId_LcmPmcRequestElapsedTimeCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_LcmSbsElapsedTimeFanSetting, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_LcmSbsElapsedTimeData, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_LcmSbsRestartFanCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_LcmSbsRequestElapsedTimeCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_LcmTestAccelerateTestActive, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_LcmStartAcceleratedTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_LcmStopAcceleratedTestCommand, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_BaseModelNumber, (SYS_INFO_DATA_INT32, 1)),
        (eSysId_ConfigManagerBaseModelWarning, (SYS_INFO_DATA_BOOL, 1)),
        (eSysId_WdiLatchStatus, (SYS_INFO_DATA_INT16, 1)),
        (eSysId_TransformerVolCompSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_TransformerPresentSetting, (SYS_INFO_DATA_INT8, 1)),
        (eSysId_MQTTHighEffScheduleWriterFLag, (SYS_INFO_DATA_BOOL, 1))
    )
)
