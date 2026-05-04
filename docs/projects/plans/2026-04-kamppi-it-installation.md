# Kamppi IT Installation — Plan & Retrospective
> Location: Kamppi, Helsinki, Finland
> District: Central 2/Finland | DM: Minna Kiira-Nymark | RM: Ricardo Moses
> Project: New Restaurant — Kamppi (Opening Spring 2026)
> Last updated: 2026-05-04
> **Status: Trip completed (Week 17, Apr 20–24, 2026). Grassfish + bookable-room streaming follow-up in week 19 (May 4–8, 2026).** The day-by-day checklist further down is preserved as the original plan; the *Trip Summary* below captures actuals.

---

## Trip Summary

| Field | Actual |
|------|-------|
| Trip dates | Apr 20–24, 2026 (Week 17) |
| Lead on-site | André Ejneborn |
| Network handover from Robert (Week 16) | **Did not fully hold up.** Most network work had to be redone or completed on-site by André during Week 17. Port assignments in the handed-over docs did not match real-world VLAN config; cabling between switches was wrong. New IP/port docs were produced on-site. |
| **Mon Apr 20** | Planning and preparation for Express kiosk install (layout, unboxing, sequencing) |
| **Tue Apr 21** | Express kiosks installed; networking documented and tested |
| **Wed Apr 22** | Express install finished; continued network work |
| **Thu Apr 23** | Effektgruppen sound/music install + config (Barix); KDS units installed in kitchen; further networking docs + tests |
| **Fri Apr 24** | POS sales testing — multiple networking issues surfaced, eventually resolved. Root cause: wrong cabling between switches + port docs not matching real VLAN config |
| Office Desktop PC + Monitor + Multi-Function Printer | Installed (backoffice) |
| Restaurant Laptop | Handed over to RM/ARM |
| Kitchen iPad | Handed over |
| Barix RetailPlayer | Installed by Effektgruppen (Thu Apr 23) |
| POS Workstations | 2 installed (final count) |
| KDS Units | 3 installed (Thu Apr 23) |
| Bookable-room streaming evaluation | **Outstanding** — TV streaming test in event room not yet done |
| Open at end of Week 17 | (1) Grassfish screens (14) — patching + install scheduled this week (W19, May 4–8); (2) Network patching for Grassfish; (3) Grassfish networking docs; (4) Event-room TV streaming test |

### Lessons Learned
- **Network IP/port documentation from Week 16 did not match real-world VLAN config.** Caused a full day of troubleshooting on Friday during POS testing. Going forward: validate port-to-VLAN mapping by spot-test before André arrives, not just on paper.
- **Electricians ran ~2 weeks behind on outlets.** Forced the on-site team to create their own outlet networking docs from scratch. For future openings: confirm electrical readiness before scheduling IT travel; build buffer or a fallback "docs from scratch" plan.
- **Effektgruppen + Barix** sound integration is now the standard pattern for new openings (Sonos legacy only).

---

## Timeline

| Week | Who | Planned Activity | Actual |
|------|-----|------------------|--------|
| **Week 16** (Apr 13–17) | Robert Beney | Network equipment installation | Done, but port/VLAN docs did not match real config — discovered Week 17 |
| **Week 17 Mon** (Apr 20) | André Ejneborn | Express Kiosk install (6 kiosks) | Planning & prep for kiosk install |
| **Week 17 Tue** (Apr 21) | André Ejneborn | Office PC / Monitor / Printer | Express kiosks installed + network docs/tests |
| **Week 17 Wed** (Apr 22) | André Ejneborn | (open) | Finished Express install + continued network work |
| **Week 17 Thu** (Apr 23) | André Ejneborn | (open) | Effektgruppen sound/music + KDS + network docs |
| **Week 17 Fri** (Apr 24) | André Ejneborn | (open) | POS testing — networking issues, root-caused & resolved |
| **Week 19** (May 4–8) | André Ejneborn | — | Grassfish patching + screen install; bookable-room TV streaming test |

---

## Week 16 — Network Installation (Robert Beney)

### Pre-Requisites
- [ ] Global Connect has delivered internet connection to the location
- [ ] Global Connect Site IP List document received and reviewed
- [ ] Switch/network hardware procured and shipped to Kamppi
- [ ] IP plan prepared (POS, kiosks, KDS, printer, office equipment)

### Installation Tasks
- [ ] Install and configure network switch(es)
- [ ] Verify internet connectivity
- [ ] Configure VLANs / network segmentation (if applicable)
- [ ] Test connectivity to Oracle Simphony cloud
- [ ] Test connectivity to FreshService, Ziik, Get Compliant, etc.
- [ ] Document IP assignments for all planned devices
- [ ] Configure firewall rules (if applicable)
- [ ] Verify Wi-Fi (if applicable for iPads, laptops, guest network)
- [ ] Hand over IP/MAC info to André for week 17 installation

### Handoff to André
- [ ] Network confirmed working
- [ ] IP assignment document shared
- [ ] Any issues or limitations documented
- [ ] Wi-Fi credentials (if applicable)

---

## Week 17, Monday — Express Kiosk Installation (André Ejneborn)

### Pre-Requisites (verify before travel)
- [ ] Network confirmed live by Robert (week 16 handoff)
- [ ] Simphony configured for Kamppi location (Petron Fernandes / Roopneet Bhalla)
- [ ] FO Navigator restaurant set up (Simon Brännström)
- [ ] Kiosk hardware shipped and on-site
- [ ] Payment terminals (Planet) shipped and on-site
- [ ] IP assignments received from Robert / Global Connect

### Per Kiosk — Installation Steps
- [ ] Unbox and physically mount kiosk
- [ ] Connect kiosk to network (ethernet to internal switch)
- [ ] Connect printer inside kiosk to network
- [ ] Verify IP address assigned correctly
- [ ] Install Future Ordering software (.msi package)
- [ ] Configure FO software with Kamppi restaurant settings
- [ ] Map kiosk to correct Simphony POS workstation
- [ ] Install NinjaOne agent for remote management
- [ ] Connect Planet payment terminal
- [ ] Map payment terminal to kiosk (IP/port config)
- [ ] **Test: Place a test order on kiosk**
- [ ] **Test: Verify order appears in Simphony**
- [ ] **Test: Verify payment terminal processes test payment**
- [ ] **Test: Verify receipt prints**
- [ ] Register kiosk in NinjaOne inventory

### Post-Installation Verification
- [ ] All kiosks powered on and responsive
- [ ] All kiosks showing correct menu (Kamppi location)
- [ ] All payment terminals paired and processing
- [ ] NinjaOne shows all kiosks as online
- [ ] FO Navigator shows Kamppi kiosks as active

---

## Week 17, Tuesday — Office PC / Monitor / Printer (André Ejneborn)

> **Primary Tuesday focus:** Install Office PC, Monitor, and Multi-Function Printer in the backoffice.

### Pre-Requisites
- [ ] Equipment shipped and on-site (Restaurant PC, monitor, printer)
- [ ] Intune Autopilot profile configured for Kamppi device(s)
- [ ] Entra ID accounts created for Kamppi RM/ARM
- [ ] M365 F3 licenses available for Kamppi RM/ARM
- [ ] Shared mailbox created for Kamppi restaurant in Exchange Online
- [ ] **Bring from Luleå HQ: wired USB keyboard + mouse** (for Office PC and ORS (Order Ready Screen) initial setup)

### Office PC (backoffice)
- [ ] Unbox PC + camera + speakers
- [ ] Connect to network (ethernet)
- [ ] Boot and run Windows Autopilot (BB-%SERIAL% naming)
- [ ] Verify Intune enrollment completes
- [ ] Verify M365 apps install (including Teams)
- [ ] Verify Microsoft Defender active
- [ ] **Test: Sign in with Kamppi RM account**
- [ ] **Test: Teams video call works (camera + audio)**
- [ ] **Test: Access to Kamppi shared mailbox**

### Monitor
- [ ] Unbox 27" monitor
- [ ] Mount/place at backoffice workstation
- [ ] Connect to Office PC (HDMI/DisplayPort)
- [ ] Connect power
- [ ] **Test: Display works at native resolution**
- [ ] Adjust brightness/orientation as needed

### Multi-Function Printer
- [ ] Unbox and place printer
- [ ] Connect to network (ethernet or Wi-Fi)
- [ ] Verify IP address (cross-check with Robert's IP plan)
- [ ] Add printer on Office PC
- [ ] **Test: Print test page from Office PC**
- [ ] **Test: Scan test document**

### Other Office Equipment (if time permits Tuesday — otherwise schedule separately)

#### Restaurant Laptop
- [ ] Unbox, network, Autopilot, verify Intune + M365 + Defender
- [ ] **Test: Sign in with Kamppi RM account**

#### Restaurant iPad
- [ ] Enroll in Jamf NOW
- [ ] Install Caspeco, Get Compliant, Royal Streaming
- [ ] **Test: Clock in/out via Caspeco**, Get Compliant checklist
- [ ] Mount iPad at designated location

#### Barix RetailPlayer (Music)
- [ ] Unbox, network, register with Effektgruppen/Royal Streaming for Kamppi
- [ ] Verify playlist plays through restaurant speakers
- [ ] Note: Kamppi uses **Effektgruppen + Barix** (new setup), not Sonos

---

## Grassfish Digital Signage (14 screens)

### Pre-Requisites
- [ ] Grassfish screens (14) shipped and on-site
- [ ] Grassfish player units shipped and on-site
- [ ] Network ports available for all 14 screens (verify with Robert's IP plan)
- [ ] Content/playlists prepared in Grassfish CMS for Kamppi
- [ ] Mounting positions confirmed with construction/design team

### Installation
- [ ] Mount all 14 screens at designated positions
- [ ] Connect each screen to network (ethernet) — player is built into the screen
- [ ] Power on and verify each screen displays correctly
- [ ] Register all 14 screens in Grassfish CMS
- [ ] Assign Kamppi location/playlist in Grassfish CMS
- [ ] **Test: Verify content/commercials displaying on all 14 screens**
- [ ] **Test: Verify remote content update works from CMS**
- [ ] Document screen positions and network assignments

### Post-Installation
- [ ] All 14 screens showing correct content
- [ ] Grassfish CMS shows all 14 Kamppi screens as online
- [ ] Brightness and orientation verified per screen

---

## Bookable Room — Streaming Solution
- [ ] Assess the room physically (TV location, network ports, power)
- [ ] Check Wi-Fi coverage in the room
- [ ] Note TV model and available ports (HDMI, USB)
- [ ] Evaluate which streaming solution fits (defer decision for now — task in project portfolio)
- [ ] Take photos for documentation

---

## Other Tasks While On-Site

### Deliverect
- [ ] Verify Deliverect URL updated for Kamppi (Kim Axelsson / Christian Ling)
- [ ] **Test: Place test order from a delivery platform** (if Deliverect is configured)

### KDS (Kitchen Display System)
- [ ] Install KDS unit(s) in kitchen
- [ ] Connect to network
- [ ] Configure with Simphony (order routing)
- [ ] Install NinjaOne agent
- [ ] **Test: Order from kiosk → appears on KDS**

### POS Workstation(s)
- [ ] Verify POS workstation(s) installed and configured (may be done by Petron/Roopneet or local Oracle partner)
- [ ] Verify POS ↔ kiosk integration working
- [ ] Verify POS ↔ Planet terminal working
- [ ] Verify POS ↔ KDS order routing
- [ ] Register in NinjaOne

### Como (Loyalty)
- [ ] Verify Como is configured for Kamppi location
- [ ] **Test: Loyalty scan/points accrual at POS or kiosk**

---

## Post-Installation Summary

| Component | Count | Status | Issues |
|-----------|-------|--------|--------|
| Grassfish Screens (w/ built-in player) | 14 | Pending (Week 19) | Network patching + Grassfish docs outstanding |
| Express Kiosks | 6 | Installed (Tue Apr 21, finished Wed Apr 22) | — |
| POS Workstations | 2 | Installed; tested Fri Apr 24 | Networking issues during testing — see Issue #1 |
| Planet Payment Terminals | 2 | Installed and paired with POS | — |
| KDS Units | 3 | Installed (Thu Apr 23) | — |
| Restaurant Laptop | 1 | Handed over to RM/ARM | — |
| Restaurant iPad (kitchen) | 1 | Handed over | — |
| Multi-Function Printer | 1 | Installed (backoffice) | — |
| Barix RetailPlayer | 1 | Installed by Effektgruppen (Thu Apr 23) | — |
| Office Desktop PC (backoffice) + 27" Monitor | 1 | Installed | — |
| Network (Global Connect) | 1 | Working — required re-cabling + new port/VLAN docs on-site | See Issue #1 |

### Issues Log
| # | Issue | Severity | Resolution | Status |
|---|-------|----------|-----------|--------|
| 1 | Network port assignments in Week-16 handover docs did not match real-world VLAN config; wrong cabling between switches | High | Re-cabled switches; produced new port/VLAN docs on-site; resolved during Friday Apr 24 POS testing | Resolved |
| 2 | Electricians ~2 weeks behind on outlets at handover | Medium | On-site team created own outlet networking docs from scratch | Worked around |
| 3 | Grassfish screens (14) not installed in Week 17 — depends on network patching + docs | Medium | Scheduled for Week 19 (May 4–8) | In progress |
| 4 | Bookable-room TV streaming test not completed in Week 17 | Low | Scheduled for Week 19 alongside Grassfish work | In progress |

### Handover
- [ ] All equipment tested and working
- [ ] NinjaOne inventory updated
- [ ] FreshService asset records created (if applicable)
- [ ] Documentation updated (hierarchy, systems landscape)
- [ ] Kamppi RM/ARM trained on basic IT (login, iPad, kiosk reboot procedures)
- [ ] Emergency contacts provided (IT Support: **IT Helpdesk via FreshService portal** — never route to individuals)
- [ ] Update Kamppi status in `docs/operations/hierarchy.md` from "Opening Spring 2026" to "Open"
