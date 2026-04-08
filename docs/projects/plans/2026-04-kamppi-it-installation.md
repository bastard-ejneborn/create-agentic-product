# Kamppi IT Installation Checklist
> Location: Kamppi, Helsinki, Finland
> District: Central 2/Finland | DM: Minna Kiira-Nymark | RM: Ricardo Moses
> Project: New Restaurant — Kamppi (Opening Spring 2026)
> Last updated: 2026-04-08

## Timeline

| Week | Who | Activity |
|------|-----|---------|
| **Week 16** (Apr 13-17) | **Robert Beney** | Network equipment installation |
| **Week 17** (Apr 20-24) | **André Ejneborn** | IT equipment installation |

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

## Week 17, Tuesday — Restaurant Office Equipment (André Ejneborn)

### Pre-Requisites
- [ ] Equipment shipped and on-site (laptop, iPad, printer, Barix player)
- [ ] Intune Autopilot profile configured for Kamppi device(s)
- [ ] Jamf NOW ready for iPad enrollment
- [ ] Caspeco location created for Kamppi
- [ ] Get Compliant location created for Kamppi
- [ ] Google Cloud Identity accounts created for Kamppi RM/ARM (for FO Navigator access)
- [ ] M365 F3 licenses available for Kamppi RM/ARM
- [ ] Entra ID accounts created for Kamppi RM/ARM
- [ ] Shared mailbox created for Kamppi restaurant in Exchange Online

### Restaurant Laptop
- [ ] Unbox laptop
- [ ] Connect to network (ethernet or Wi-Fi)
- [ ] Boot and run Windows Autopilot (BB-%SERIAL% naming)
- [ ] Verify Intune enrollment completes
- [ ] Verify M365 apps install (including Teams)
- [ ] Verify Microsoft Defender active (`mdatp health` equivalent for Windows)
- [ ] Verify access to shared mailbox
- [ ] Register in NinjaOne? (verify — laptops managed by Intune, not NinjaOne)
- [ ] **Test: Sign in with Kamppi RM account**

### Restaurant iPad
- [ ] Unbox iPad
- [ ] Enroll in Jamf NOW
- [ ] Install Caspeco app — configure for Kamppi location
- [ ] Install Get Compliant app — configure for Kamppi location
- [ ] Install Royal Streaming app (backup music player)
- [ ] **Test: Clock in/out via Caspeco**
- [ ] **Test: Open Get Compliant checklist**
- [ ] Mount iPad at designated location

### Multi-Function Printer
- [ ] Unbox and place printer
- [ ] Connect to network (ethernet or Wi-Fi)
- [ ] Verify IP address
- [ ] Configure on restaurant laptop (add as printer)
- [ ] **Test: Print test page from laptop**
- [ ] **Test: Scan test document**

### Barix RetailPlayer (Music)
- [ ] Unbox and connect to network
- [ ] Contact Royal Streaming to register device for Kamppi
- [ ] Verify playlist loads and plays
- [ ] Set volume to appropriate level
- [ ] **Test: Music playing through restaurant speakers**

### Restaurant PC (if Kamppi has office space)
- [ ] Unbox PC + 27" monitor + camera + speakers
- [ ] Connect to network
- [ ] Boot and run Windows Autopilot
- [ ] Verify Intune enrollment
- [ ] Verify M365 apps + Teams
- [ ] **Test: Teams video call works (camera + audio)**

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
- [ ] Connect each screen to Grassfish player unit
- [ ] Connect each player to network (ethernet)
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

Fill in after installation:

| Component | Count | Status | Issues |
|-----------|-------|--------|--------|
| Express Kiosks | | | |
| Payment Terminals (Planet) | | | |
| POS Workstations | | | |
| KDS Units | | | |
| Grassfish Screens | 14 | | |
| Grassfish Players | 14 | | |
| Restaurant Laptop | 1 | | |
| Restaurant iPad | 1 | | |
| Multi-Function Printer | 1 | | |
| Barix RetailPlayer | 1 | | |
| Restaurant PC | TBD | | |
| Network (Global Connect) | 1 | | |

### Issues Log
| # | Issue | Severity | Resolution | Status |
|---|-------|----------|-----------|--------|
| | | | | |

### Handover
- [ ] All equipment tested and working
- [ ] NinjaOne inventory updated
- [ ] FreshService asset records created (if applicable)
- [ ] Documentation updated (hierarchy, systems landscape)
- [ ] Kamppi RM/ARM trained on basic IT (login, iPad, kiosk reboot procedures)
- [ ] Emergency contacts provided (IT Support: Christian Ling, FreshService portal)
- [ ] Update Kamppi status in `docs/operations/hierarchy.md` from "Opening Spring 2026" to "Open"
